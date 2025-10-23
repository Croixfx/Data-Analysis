import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# data = pd.DataFrame({'X':[1,2,3,4], 'Y': [10,20,25,30]})
# sns.scatterplot(x='X', y='Y', data = data)
# plt.show()

x = np.random.normal(size=50)
y = np.random.normal(size=50)

plt.scatter(x,y,color='red',alpha=0.5)
plt.title('Random Dots')
plt.xlabel('X-axix')
plt.show()