import math
import random
from typing import Union, Any
import numpy as np
from BatAlgorithm import *


def Fun(D, X):
    val = 0.0
    for i in range(D):
        val = (-(X[1] + 47) * np.sin(np.sqrt(abs(X[0] / 2 + (X[1] + 47)))) - X[0] * np.sin(
        np.sqrt(abs(X[0] - (X[1] + 47)))))
    return val

def f(D, X):
    for i in range(D):
       num = (np.sin((X[0] ** 2 + X[1] ** 2) ** 2) ** 2) - 0.5
       den = (1 + 0.001 * (X[0] ** 2 + X[1] ** 2)) ** 2
    y = 0.5 + num / den
    return y

def bat(pop,gen,app,clicked):

    if(clicked=="EggHolder"):
        Algorithm = BatAlgorithm(3, pop, gen, 0.5, 0.5, 0.0, 2.0, -512.0, 512.0, Fun, app)
        Algorithm.move_bat()
    elif(clicked=="SCHAFFER FUNCTION N. 2"):
        Algorithm = BatAlgorithm(3, pop, gen, 0.5, 0.5, 0.0, 2.0, -100, 100, f, app)
        Algorithm.move_bat()


