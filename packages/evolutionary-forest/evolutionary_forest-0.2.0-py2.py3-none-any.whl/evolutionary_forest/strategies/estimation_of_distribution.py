import numpy as np
from deap.gp import Primitive, Terminal
from deap.tools import HallOfFame
from mlxtend.evaluate import feature_importance_permutation

from evolutionary_forest.component.evaluation import quick_result_calculation, get_cv_splitter


class EstimationOfDistribution():
    def __init__(self):
        self.pset = None
        self.mutation_scheme: str = None
        self.hof: HallOfFame = None
        self.primitive_prob: np.ndarray = None
        self.terminal_prob: np.ndarray = None

    def permutation_importance_calculation(self, X, Y, individual):
        # The correct way is to calculate the terminal importance based on the test data
        estimators = individual.estimators
        kcv = get_cv_splitter(estimators[0]['Ridge'], self.cv)
        all_importance_values = []
        for id, index in enumerate(kcv.split(X, Y)):
            def prediction_function(X):
                # quickly calculate permutation importance
                Yp = quick_result_calculation(individual.gene, self.pset, X, self.original_features)
                return estimators[id].predict(Yp)

            train_index, test_index = index
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = Y[train_index], Y[test_index]
            # get permutation importance
            importance_value = feature_importance_permutation(X_test, y_test, prediction_function, 'r2')[0]
            all_importance_values.append(importance_value)
        all_importance_values = np.mean(all_importance_values, axis=0)
        all_importance_values = np.clip(all_importance_values, 0, None)
        individual.terminal_importance_values = all_importance_values

    def update_frequency_count(self, best_pop, factor, importance_weight):
        # count the frequency of primitives and terminals
        primitive_dict = {}
        for k in self.pset.primitives.keys():
            primitive_dict.update({v.name: k for k, v in enumerate(self.pset.primitives[k])})
        terminal_dict = {}
        for k in self.pset.terminals.keys():
            terminal_dict.update({v.name: k for k, v in enumerate(self.pset.terminals[k])})
        for h in best_pop:
            for importance, g in zip(h.coef, h.gene):
                for x in g:
                    if importance_weight:
                        weight = importance
                    else:
                        weight = 1
                    weight *= factor
                    if isinstance(x, Primitive):
                        self.primitive_prob_count[primitive_dict[x.name]] += weight
                    elif isinstance(x, Terminal):
                        if x.name not in terminal_dict:
                            # constant
                            self.terminal_prob_count[-1] += weight
                        else:
                            self.terminal_prob_count[terminal_dict[x.name]] += weight
                    else:
                        raise Exception

    def frequency_counting(self, importance_weight=True):
        if self.mutation_scheme == 'EDA-Terminal-PMI':
            # Permutation importance based probability estimation (Slow!)
            for h in self.hof:
                if not hasattr(h, 'terminal_importance_values'):
                    self.permutation_importance_calculation(self.X, self.y, h)
            self.primitive_prob_count = np.ones(self.pset.prims_count)
            self.terminal_prob_count = np.mean([x.terminal_importance_values for x in self.hof], axis=0)
        else:
            ### Feature Importance based on frequency
            self.primitive_prob_count = np.ones(self.pset.prims_count)
            self.terminal_prob_count = np.ones(self.pset.terms_count)
            if self.hof == None:
                return
            if self.mutation_scheme == 'EDA-Terminal-Balanced':
                # Separate individuals to two groups, good ones and bad ones
                positive_sample = list(sorted(self.hof, key=lambda x: x.fitness.wvalues[0]))[len(self.hof) // 2:]
                negative_sample = list(sorted(self.hof, key=lambda x: x.fitness.wvalues[0]))[:len(self.hof) // 2]
                self.update_frequency_count(positive_sample, 1, importance_weight)
                self.update_frequency_count(negative_sample, -1, importance_weight)
                min_max_scaling = lambda v: (v - v.min())
                self.primitive_prob_count = min_max_scaling(self.primitive_prob_count) + 1
                self.terminal_prob_count = min_max_scaling(self.terminal_prob_count) + 1
            else:
                if 'Population' in self.mutation_scheme:
                    self.update_frequency_count(self.pop, 1, importance_weight)
                else:
                    self.update_frequency_count(self.hof, 1, importance_weight)

    def probability_sampling(self):
        # Sampling primitive and terminal nodes based on the probability matrix
        if self.mutation_scheme == 'probability-TS':
            self.primitive_prob[:] = np.random.dirichlet(self.primitive_prob_count)
            self.terminal_prob[:] = np.random.dirichlet(self.terminal_prob_count)
        elif self.mutation_scheme == 'EDA-Primitive':
            self.primitive_prob[:] = np.random.dirichlet(self.primitive_prob_count)
            self.terminal_prob /= np.sum(self.terminal_prob)
        elif self.mutation_scheme in ['EDA-Terminal']:
            self.primitive_prob /= np.sum(self.primitive_prob)
            self.terminal_prob += self.terminal_prob_count / np.sum(self.terminal_prob_count)
        elif self.mutation_scheme in ['EDA-Terminal-Balanced', 'EDA-Terminal-PMI']:
            self.primitive_prob[:] = self.primitive_prob_count / np.sum(self.primitive_prob_count)
            if self.mutation_scheme == 'EDA-Terminal-PMI':
                # add the probability of constant nodes
                terminal_prob = np.append(self.terminal_prob_count, np.mean(self.terminal_prob_count))
            else:
                terminal_prob = self.terminal_prob_count
            assert np.all(terminal_prob >= 0)
            if np.sum(terminal_prob) == 0:
                # When there are no important features
                self.terminal_prob[:] = np.full_like(terminal_prob, 1 / len(terminal_prob))
            else:
                self.terminal_prob[:] = terminal_prob / np.sum(terminal_prob)
        elif self.mutation_scheme.startswith('EDA-PM'):
            self.primitive_prob[:] = self.primitive_prob_count / np.sum(self.primitive_prob_count)
            self.terminal_prob[:] = self.terminal_prob_count / np.sum(self.terminal_prob_count)
            if self.verbose:
                print('primitive_prob', self.primitive_prob)
                print('terminal_prob', self.terminal_prob)
        elif self.mutation_scheme.startswith('EDA-Terminal-PM') or self.mutation_scheme in \
            ['weight-plus-threshold-EDA', 'EDA-Terminal-SameWeight', 'EDA-Terminal-PM-Tournament']:
            self.primitive_prob /= np.sum(self.primitive_prob)
            self.terminal_prob[:] = self.terminal_prob_count / np.sum(self.terminal_prob_count)
            ## Eliminate trivial terminals
            # self.terminal_prob[self.terminal_prob < np.mean(self.terminal_prob) / 10] = 0
            # self.terminal_prob[self.terminal_prob > 0] = 1
            # self.terminal_prob[:] = self.terminal_prob / np.sum(self.terminal_prob)
        else:
            raise Exception
        if self.verbose:
            print('terminal_prob', self.terminal_prob)
