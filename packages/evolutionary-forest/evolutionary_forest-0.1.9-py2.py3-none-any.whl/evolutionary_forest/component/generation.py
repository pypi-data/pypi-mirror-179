import random

import numpy as np
from deap.gp import mutUniform
from scipy.stats import pearsonr, spearmanr

from evolutionary_forest.component.evaluation import quick_evaluate


def varAndPlus(population, toolbox, cxpb, mutpb, gene_num, limitation_check,
               semantic_check_tool=None, varOr=False):
    @limitation_check
    def mutation_function(*population):
        offspring = [toolbox.clone(ind) for ind in population]
        crossed_individual = set()

        # Apply crossover and mutation on the offspring
        # Support both VarAnd and VarOr
        i = 0
        while i < len(offspring):
            # Execute mutation and selection operator N-times
            for c in range(gene_num):
                if i % 2 == 0 and random.random() < cxpb:
                    offspring[i], offspring[i + 1] = toolbox.mate(offspring[i], offspring[i + 1])
                    del offspring[i].fitness.values, offspring[i + 1].fitness.values
                    crossed_individual.add(offspring[i])
                    crossed_individual.add(offspring[i+1])

                if random.random() < mutpb and (not varOr or (i not in crossed_individual)):
                    offspring[i], = toolbox.mutate(offspring[i])
                    del offspring[i].fitness.values

            if semantic_check_tool is not None:
                # check by semantics
                x = semantic_check_tool['x']
                y = semantic_check_tool['y']
                pset = semantic_check_tool['pset']
                correlation_threshold=semantic_check_tool.get('correlation_threshold', 0.2)
                correlation_mode=semantic_check_tool.get('correlation_mode', 'Pearson')
                index = np.random.randint(0, len(x), 20)
                for k, g in enumerate(offspring[i].gene):
                    y_hat = quick_evaluate(g, pset, x[index])
                    c = 0
                    function = {
                        'Pearson': pearsonr,
                        'Spearman': spearmanr,
                    }[correlation_mode]
                    while (not isinstance(y_hat, np.ndarray)) or (y_hat.size != y[index].size) or \
                        (np.abs(function(y_hat, y[index])[0]) < correlation_threshold):
                        c += 1
                        offspring[i].gene[k] = mutUniform(g, toolbox.expr_mut, pset)[0]
                        del offspring[i].fitness.values
                        y_hat = quick_evaluate(g, pset, x[index])
                        if c > 100:
                            print('Warning!')
                            break
            i += 1
        return offspring

    return mutation_function(*population)
