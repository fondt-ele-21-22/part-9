import numpy as np
from example import analyze

def fit_bingham(DGAMMA, TAU):
    cols = [DGAMMA, DGAMMA**0]
    alpha, sse = analyze.fit(cols, TAU)
    a, b = alpha
    return a, b, sse


def fit_newton(DGAMMA, TAU):
    cols = [DGAMMA]
    a, sse = analyze.fit(cols, TAU)
    return a, sse


def fit_powerlaw(DGAMMA, TAU):
    cols = [np.log(DGAMMA), DGAMMA**0]
    alpha, sse = analyze.fit(cols, np.log(TAU))
    a, log_b = alpha
    b = np.exp(log_b)
    return a, b, sse
    