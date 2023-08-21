import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np
    
x = np.arange(0, 100 + 1)
probabilities = binom.pmf(x, 100, 0.5)

plt.plot(x, probabilities)
plt.show()
