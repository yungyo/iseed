import numpy as np

def costf(w, x, y):
    yp = w.T@x
    return (yp - y.T)@(yp - y.T).T

def gradJ(w):
    return np.array([8 * w[0] + 4 * w[1] + 4 * w[2] - 4, 4 * w[0] + 4 * w[1] + 2 * w[2] - 4, 4 * w[0] + 4 * w[1] + 4 * w[2] - 4])

def step_func(x):
   y = x > 0
   return 2 * y.astype(int) - 1

xi = np.array([[1, 1, 1, 1], [0, 1, 0, 1], [0, 0, 1, 1]])
yi = np.array([[-1], [1], [1], [1]])
wi = np.array([[0], [0], [0]])

alpha = 0.01
J = costf(wi, xi, yi)

while (True):
    JP = J
    delw = alpha * gradJ(wi)
    wi = wi - delw
    J = costf(wi, xi, yi)
    print(J, wi.T, step_func(wi.T @ wi))
    if (np.abs((J - JP) / J) < 0.000001): break

print(wi)