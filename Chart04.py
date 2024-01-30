import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.title('Histograma')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.hist(data, bins=30, edgecolor='grey')
plt.show()
