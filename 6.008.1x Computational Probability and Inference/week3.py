import comp_prob_inference
import numpy as np

# how to determine whether two rv are independent

prob_W_I = np.array([[1 / 2, 0], [0, 1 / 6], [0, 1 / 3]])
prob_W = prob_W_I.sum(axis=1)
prob_I = prob_W_I.sum(axis=0)

x = np.outer(prob_W, prob_I)
print(x)
print(prob_W_I)