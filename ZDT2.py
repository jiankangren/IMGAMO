# -*- coding: utf-8 -*-

import numpy as np
import imgamo as mo
import math

__author__ = "amarszalek"


def obj_func1(x):
    return x[0]


def fun_g(x):
    n = len(x)
    return 1.0 + 9.0 * np.sum(x[1:]) / (n - 1.0)


def obj_func2(x):
    g = fun_g(x)
    return g * (1.0 - (x[0]/g)**2)


def hiper_mutate(ind, pattern, bounds):
    r = np.random.random()
    if r < 0.45:
        ind = mo.uniform_mutate_in(ind, pattern, bounds)
    elif r < 0.9:
        ind = mo.gaussian_mutate(ind, pattern, bounds)
    else:
        ind = mo.bound_mutate(ind, pattern, bounds)
    return ind


"""
population_size:  int,                 default: 100
max_evaluations:  int,                 default: -1
max_iterations:   int,                 default: 1000
exchange_iter:    int,                 default: 3
change_iter:      int,                 default: 3
clone_number:     int,                 default: 15
distance_level_f: float,               default: 0.05
distance_level_x: float,               default: 0.01
mutate:           callable (function), default: uniform_mutate
individual_init:  callable (function), default: create_individual
distance:         callable (function), default: euclidean_distance
verbose:          bool,                default: True
"""
OPTIONS = mo.IMGAMOOptions(population_size=20, max_iterations=50, clone_number=20, exchange_iter=1, change_iter=1,
                           distance_level_f=0.05, distance_level_x=0.01, mutate=hiper_mutate, verbose=False)

OBJ_NUMS = 2
VAR_NUMS = 5
OBJ_FUNCS = [obj_func1, obj_func2]
OBJ_ARGS = [(), ()]
BOUNDS = tuple((0.0, 1.0) for i in range(VAR_NUMS)) + (0.1,)
PROBLEM = mo.IMGAMOProblem(OBJ_NUMS, VAR_NUMS, OBJ_FUNCS, OBJ_ARGS, BOUNDS)

solver = mo.IMGAMOAlgorithm(PROBLEM, OPTIONS)


import datetime
if __name__ == '__main__':
    res = solver.run_algorithm()
    print('Evaluation_count: ', res.evaluation_count)
    print('Front size: ', res.front_size)
    print('Elapsed time:', res.elapsed_time)
    res.plot_2d(0, 1)
    res = solver.run_algorithm()
    print('Evaluation_count: ', res.evaluation_count)
    print('Front size: ', res.front_size)
    print('Elapsed time:', res.elapsed_time)
    res.plot_2d(0, 1)

