import math

MaxSteps = 30
Tolerance = 0.0001

def example_f(x):
    "x^2 + 2x + 1"
    return (x**2) + 2 * x + 1

def example_deriv(x):
    "2x + 2 + cos x"
    return 2 * x + 2
