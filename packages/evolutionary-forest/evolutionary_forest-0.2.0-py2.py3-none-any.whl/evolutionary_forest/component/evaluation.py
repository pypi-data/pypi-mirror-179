import enum
import random
import time
from typing import List

import dill
import numpy as np
import shap
from deap import base
from deap import creator
from deap import gp
from deap import tools
from deap.gp import PrimitiveTree, Primitive, Terminal
from numpy.testing import assert_almost_equal
from sklearn import model_selection
from sklearn.base import RegressorMixin, ClassifierMixin
from sklearn.datasets import make_regression
from sklearn.feature_selection import VarianceThreshold
from sklearn.inspection import permutation_importance
from sklearn.linear_model import RidgeCV, LogisticRegression
from sklearn.linear_model._base import LinearModel
from sklearn.metrics import make_scorer, accuracy_score, balanced_accuracy_score, precision_score, recall_score, \
    f1_score, r2_score
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split, KFold
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.tree import BaseDecisionTree

from evolutionary_forest.model.PLTree import SoftPLTreeRegressor, SoftPLTreeRegressorEM
from evolutionary_forest.multigene_gp import result_post_process, MultiplePrimitiveSet, quick_fill
from evolutionary_forest.sklearn_utils import cross_val_predict
from evolutionary_forest.utils import reset_random

reset_random(0)


def calculate_score(args):
    (X, Y, score_func, cv, other_parameters) = calculate_score.data
    # nn_prediction: prediction results of the neural network
    nn_prediction = other_parameters['nn_prediction']
    # dynamic_target: random generate cross-validation scheme
    dynamic_target = other_parameters['dynamic_target']
    original_features = other_parameters['original_features']
    # test_data_size: number of test data samples, which do not have the label
    test_data_size = other_parameters['test_data_size']
    pset = other_parameters['pset']
    # sklearn_format: model is in sklearn format
    sklearn_format = other_parameters['sklearn_format']
    cross_validation = other_parameters['cross_validation']
    feature_importance_method = other_parameters['feature_importance_method']
    filter_elimination = other_parameters['filter_elimination']

    pipe: Pipeline
    pipe, func = args
    if not isinstance(func, list):
        func = dill.loads(func)

    # only used for PS-Tree
    best_label = None
    altered_labels = None
    # GP evaluation
    start_time = time.time()

    if sklearn_format:
        Yp = quick_result_calculation(func, pset, X, original_features, sklearn_format)
        pipe = pipe_combine(Yp, pipe)
        Yp = X
        hash_result = None
    else:
        if hasattr(pipe, 'register'):
            Yp, hash_result = quick_result_calculation(func, pset, X, original_features, need_hash=True,
                                                       register_array=pipe.register)
        else:
            Yp, hash_result = quick_result_calculation(func, pset, X, original_features, need_hash=True)
        if nn_prediction is not None:
            Yp = np.concatenate([Yp, nn_prediction], axis=1)
        if test_data_size > 0:
            Yp = Yp[:-test_data_size]
        assert isinstance(Yp, np.ndarray)
        assert not np.any(np.isnan(Yp))
        assert not np.any(np.isinf(Yp))

        # only use for PS-Tree
        if hasattr(pipe, 'partition_scheme'):
            partition_scheme = pipe.partition_scheme
            assert not np.any(np.isnan(partition_scheme))
            assert not np.any(np.isinf(partition_scheme))
            Yp = np.concatenate([Yp, np.reshape(partition_scheme, (-1, 1))], axis=1)
    if hasattr(pipe, 'active_gene'):
        Yp = Yp[:, pipe.active_gene]

    gp_evaluation_time = time.time() - start_time

    # ML evaluation
    start_time = time.time()
    if 'CV' in score_func:
        # custom cross validation scheme
        if '-Random' in score_func:
            cv = StratifiedKFold(shuffle=True)
        else:
            cv = None

        if score_func == 'CV-Accuracy-Recall':
            custom_scorer = {'accuracy': make_scorer(accuracy_score),
                             'balanced_accuracy': make_scorer(balanced_accuracy_score),
                             'precision': make_scorer(precision_score, average='macro'),
                             'recall': make_scorer(recall_score, average='macro'),
                             'f1': make_scorer(f1_score, average='macro')}
            result = cross_validate(pipe, Yp, Y, cv=cv, return_estimator=True, scoring=custom_scorer)
        elif score_func == 'CV-F1-Score':
            result = cross_validate(pipe, Yp, Y, cv=cv, return_estimator=True,
                                    scoring=make_scorer(f1_score, average='macro'))
        elif score_func == 'CV-SingleFold':
            result = single_fold_validation(pipe, Yp, Y, index=random.randint(0, 4))
        else:
            result = cross_validate(pipe, Yp, Y, cv=cv, return_estimator=True)

        if score_func == 'CV-Accuracy-Recall':
            y_pred = np.array([np.mean(result['test_accuracy']),
                               np.mean(result['test_balanced_accuracy']),
                               np.mean(result['test_precision']),
                               np.mean(result['test_recall']),
                               np.mean(result['test_f1'])])
        else:
            y_pred = result['test_score']
        estimators = result['estimator']
    elif not cross_validation:
        pipe.fit(Yp, Y)
        y_pred = pipe.predict(Yp)
        estimators = [pipe]
    else:
        if sklearn_format:
            base_model = pipe['model']['Ridge']
        else:
            base_model = pipe['Ridge']
        regression_task = isinstance(base_model, RegressorMixin)
        if isinstance(base_model, RidgeCV):
            # Ridge CV
            pipe.fit(Yp, Y)
            y_pred, estimators = base_model.cv_values_[:, np.argmax(base_model.cv_values_.sum(axis=0))], [pipe]
        elif cv == 1:
            # single fold training (not recommend)
            indices = np.arange(len(Y))
            x_train, x_test, y_train, y_test, idx_train, idx_test = train_test_split(
                Yp, Y, indices, test_size=0.2)
            estimators = [pipe]
            pipe.fit(x_train, y_train)
            y_pred = np.ones_like(Y)
            y_pred[idx_test] = pipe.predict(x_test)
        else:
            # cross-validation
            if dynamic_target:
                cv = get_cv_splitter(base_model, cv, random.randint(0, int(1e9)))
            else:
                cv = get_cv_splitter(base_model, cv)

            if filter_elimination is not None:
                strategies = set(filter_elimination.split(','))
                mask = np.ones(X.shape[1], dtype=bool)
                if 'Variance' in strategies:
                    # eliminate features based on variance
                    threshold = VarianceThreshold(threshold=0.01)
                    threshold.fit(Yp)
                    indices = threshold.get_support(indices=True)
                    mask[indices] = False
                if 'Correlation' in strategies:
                    # eliminate features based on correlation
                    col_corr = []
                    corr_matrix = np.corrcoef(Yp)
                    for i in range(corr_matrix.shape[1]):
                        for j in range(i):
                            if abs(corr_matrix[i, j]) > threshold:
                                # highly correlated features
                                col_corr.append(i)
                                break
                    mask[col_corr] = False
                Yp = Yp[:, mask]

            if regression_task:
                y_pred, estimators = cross_val_predict(pipe, Yp, Y, cv=cv)
            else:
                y_pred, estimators = cross_val_predict(pipe, Yp, Y, cv=cv, method='predict_proba')

            if feature_importance_method == 'SHAP' and len(estimators) == cv.n_splits:
                for id, estimator in enumerate(estimators):
                    split_fold = list(cv.split(Yp, Y))
                    train_id, test_id = split_fold[id][0], split_fold[id][1]
                    if isinstance(estimator['Ridge'], (LinearModel, LogisticRegression)):
                        explainer = shap.LinearExplainer(estimator['Ridge'], Yp[train_id])
                    elif isinstance(estimator['Ridge'], BaseDecisionTree):
                        explainer = shap.TreeExplainer(estimator['Ridge'], Yp[train_id])
                    else:
                        raise Exception
                    if isinstance(estimator['Ridge'], BaseDecisionTree):
                        feature_importance = explainer.shap_values(Yp[test_id])[0]
                    else:
                        feature_importance = explainer.shap_values(Yp[test_id])
                    estimator['Ridge'].shap_values = np.abs(feature_importance).mean(axis=0)

            if feature_importance_method == 'PermutationImportance' and len(estimators) == cv.n_splits:
                # Don't need to calculate the mean value here
                for id, estimator in enumerate(estimators):
                    split_fold = list(cv.split(Yp, Y))
                    train_id, test_id = split_fold[id][0], split_fold[id][1]
                    r = permutation_importance(estimator['Ridge'], Yp[test_id], Y[test_id], n_jobs=1, n_repeats=1)
                    estimator['Ridge'].pi_values = np.abs(r.importances_mean)

            if np.any(np.isnan(y_pred)):
                np.save('error_data_x.npy', Yp)
                np.save('error_data_y.npy', Y)
                raise Exception

            if isinstance(base_model, SoftPLTreeRegressor) and not isinstance(base_model, SoftPLTreeRegressorEM):
                # determine the best partition scheme
                cv_label = other_parameters['cv_label']
                if cv_label:
                    best_label = np.zeros(len(Y))
                else:
                    partition_num = len(np.unique(pipe.partition_scheme))
                    best_label = np.zeros((len(Y), partition_num))
                for index, estimator in zip(cv.split(Y), estimators):
                    estimator: SoftPLTreeRegressor
                    if cv_label:
                        # determine the label of PS-Tree through cross-validation
                        train_index, test_index = index
                        X_test, y_test = Yp[test_index], Y[test_index]
                        best_label[test_index] = estimator.score(X_test, np.reshape(y_test, (-1, 1)))
                    else:
                        train_index, test_index = index
                        score = estimator.score(Yp[train_index], np.reshape(Y[train_index], (-1, 1)))
                        best_label[train_index, score] += 1
                if not cv_label:
                    best_label = np.argmax(best_label, axis=1)
                altered_labels = np.sum(pipe.partition_scheme != best_label)
    ml_evaluation_time = time.time() - start_time
    if altered_labels is not None:
        print('altered_labels', altered_labels)
    return y_pred, estimators, {
        'gp_evaluation_time': gp_evaluation_time,
        'ml_evaluation_time': ml_evaluation_time,
        'best_label': best_label,
        'altered_labels': altered_labels,
        'hash_result': hash_result,
    }


def pipe_combine(Yp, pipe):
    Yp = list(filter(lambda x: not isinstance(x, (int, float, np.ndarray, enum.Enum)), Yp))
    if len(Yp) == 0:
        pipe = Pipeline([
            ("feature", "passthrough"),
            ('model', pipe)
        ])
    else:
        pipe = Pipeline([
            ("feature", FeatureUnion(
                [(f'preprocessing_{id}', p) for id, p in enumerate(Yp)]
            )),
            ('model', pipe)
        ])
    return pipe


def single_fold_validation(model, x_data, y_data, index):
    # only validate single fold, this method is faster than cross-validation
    cv = model_selection.KFold(n_splits=5, shuffle=False, random_state=0)
    current_index = 0
    scores = []
    for train_index, test_index in cv.split(x_data):
        if current_index == index:
            # print("TRAIN:", train_index, "TEST:", test_index)
            X_train, X_test = x_data[train_index], x_data[test_index]
            y_train, y_test = y_data[train_index], y_data[test_index]
            model.fit(X_train, y_train)
            if isinstance(model['Ridge'], ClassifierMixin):
                scores.append(accuracy_score(y_test, model.predict(X_test)))
            elif isinstance(model['Ridge'], RegressorMixin):
                scores.append(r2_score(y_test, model.predict(X_test)))
            else:
                raise Exception
        else:
            scores.append(-1)
        current_index += 1
    assert np.any(scores != 0)
    return {
        'test_score': scores,
        'estimator': [model for _ in range(5)],
    }


def get_cv_splitter(base_model, cv, random_state=0):
    if isinstance(base_model, ClassifierMixin):
        cv = StratifiedKFold(n_splits=cv, shuffle=True, random_state=random_state)
    else:
        cv = KFold(n_splits=cv, shuffle=True, random_state=random_state)
    return cv


def quick_result_calculation(func: List[PrimitiveTree], pset, data, original_features=False,
                             sklearn_format=False, need_hash=False, register_array=None):
    if sklearn_format:
        data = enum.Enum('Enum', {f"ARG{i}": i for i in range(data.shape[1])})
    # quick evaluate the result of features
    result = []
    hash_result = []
    if hasattr(pset, 'number_of_register'):
        register = np.ones((data.shape[0], pset.number_of_register))
        for id, gene in enumerate(func):
            input_data = np.concatenate([data, register], axis=1)
            quick_result = quick_evaluate(gene, pset, input_data)
            quick_result = quick_fill([quick_result], data)[0]
            if isinstance(quick_result, np.ndarray):
                hash_result.append(hash(quick_result.tostring()))
            else:
                hash_result.append(hash(str(quick_result)))
            register[:, register_array[id]] = quick_result
        result = register.T
    elif isinstance(pset, MultiplePrimitiveSet):
        for id, gene in enumerate(func):
            quick_result = quick_evaluate(gene, pset.pset_list[id], data)
            quick_result = quick_fill([quick_result], data)[0]
            if isinstance(quick_result, np.ndarray):
                hash_result.append(hash(quick_result.tostring()))
            else:
                hash_result.append(hash(str(quick_result)))
            result.append(quick_result)
            data = np.concatenate([data, np.reshape(quick_result, (-1, 1))], axis=1)
    else:
        for gene in func:
            feature: np.ndarray = quick_evaluate(gene, pset, data)
            if isinstance(feature, np.ndarray):
                hash_result.append(hash(feature.tostring()))
            else:
                hash_result.append(hash(str(feature)))
            result.append(feature)
    if not sklearn_format:
        result = result_post_process(result, data, original_features)
        # result = np.reshape(result[:, -1], (-1, 1))
    if not need_hash:
        return result
    else:
        return result, hash_result


def quick_evaluate(expr: PrimitiveTree, pset, data, prefix='ARG'):
    result = None
    stack = []
    for node in expr:
        stack.append((node, []))
        while len(stack[-1][1]) == stack[-1][0].arity:
            prim, args = stack.pop()
            if isinstance(prim, Primitive):
                result = pset.context[prim.name](*args)
            elif isinstance(prim, Terminal):
                if prefix in prim.name:
                    if isinstance(data, np.ndarray):
                        result = data[:, int(prim.name.replace(prefix, ''))]
                    elif isinstance(data, (dict, enum.EnumMeta)):
                        result = data[prim.name]
                    else:
                        raise ValueError("Unsupported data type!")
                else:
                    result = prim.value
            else:
                raise Exception
            if len(stack) == 0:
                break  # If stack is empty, all nodes should have been seen
            stack[-1][1].append(result)
    return result


def minimal_task():
    # A minimal task for SR
    x, y = make_regression(n_samples=1000)
    pset = gp.PrimitiveSet("MAIN", x.shape[1])
    pset.addPrimitive(np.add, 2, name="vadd")
    pset.addPrimitive(np.subtract, 2, name="vsub")
    pset.addPrimitive(np.multiply, 2, name="vmul")
    pset.addPrimitive(np.negative, 1, name="vneg")
    pset.addPrimitive(np.cos, 1, name="vcos")
    pset.addPrimitive(np.sin, 1, name="vsin")
    pset.addEphemeralConstant("rand101", lambda: random.randint(-1, 1))
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)
    toolbox = base.Toolbox()
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=2, max_=8)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)
    pop = toolbox.population(n=10000)
    st = time.time()
    avg_a = np.zeros(x.shape[0])
    for ind in pop:
        avg_a += quick_evaluate(ind, pset, x)
    print('time', time.time() - st)
    st = time.time()
    avg_b = np.zeros(x.shape[0])
    for ind in pop:
        func = gp.compile(ind, pset)
        avg_b += func(*x.T)
    print('time', time.time() - st)
    assert_almost_equal(avg_a, avg_b)


def minimal_feature_importance():
    from sklearn.datasets import load_diabetes
    from sklearn.linear_model import Ridge

    diabetes = load_diabetes()
    X_train, X_val, y_train, y_val = train_test_split(
        diabetes.data, diabetes.target, random_state=0)
    model = Ridge(alpha=1e-2).fit(X_train, y_train)
    model.score(X_val, y_val)
    r = permutation_importance(model, X_val, y_val,
                               n_repeats=30,
                               random_state=0)
    print(r.importances_mean)
    for i in r.importances_mean.argsort()[::-1]:
        if r.importances_mean[i] - 2 * r.importances_std[i] > 0:
            print(f"{diabetes.feature_names[i]:<8}"
                  f"{r.importances_mean[i]:.3f}"
                  f" +/- {r.importances_std[i]:.3f}")


if __name__ == '__main__':
    # minimal_task()
    minimal_feature_importance()
