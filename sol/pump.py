import numpy as np
from example import analyze

def fit_curve(Q, H):
    cols = [Q**2, Q, Q**0]
    alpha, sse = analyze.fit(cols, H)
    alpha2, alpha1, alpha0 = alpha
    return alpha2, alpha1, alpha0


def draw_curve(alpha2, alpha1, alpha0, Qmin, Qmax):
    x = np.linspace(Qmin, Qmax)
    y = alpha2 * x**2 + alpha1 * x + alpha0
    analyze.plot(x, y, xlabel='Q', ylabel='H', figsize=(20, 5))

    
def draw_scatter(alpha2, alpha1, alpha0, Q, H):
    y = alpha2 * Q**2 + alpha1 * Q + alpha0
    analyze.scatter(H, y, xlabel='H (measured)', ylabel='H (estimted)', figsize=(20, 5), add_bisector=True)
    