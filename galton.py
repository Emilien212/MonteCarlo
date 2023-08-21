import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np

n = 1000000
layers = 50
results = []

for _ in range(n):
    position = layers/2
    for _ in range(layers):
        if np.random.random() < 0.5:
            position += 0.5
        else:
            position -= 0.5

    results.append(int(position))


plt.hist(results, rwidth=0.5, bins=layers+1, range=(0, layers+1), density=True)

x = np.arange(0, layers + 1)
probabilities = binom.pmf(x, layers, 0.5)

plt.plot(x+0.5, probabilities, label="Binomial distribution")
plt.legend()
plt.savefig(f"galton_{n}")