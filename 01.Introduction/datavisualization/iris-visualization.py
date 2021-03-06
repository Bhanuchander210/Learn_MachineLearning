# Visualization of data

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import radviz

sns.set(style="white", color_codes=True)

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
iris = pd.read_csv("../../data/csv/iris.csv", names=names) # the iris dataset is now a Pandas DataFrame

# Head
print iris.head()

# Grouped Value
print iris["class"].value_counts()

# Pandas Plot

## Normal Plot with selected columns

iris.plot(kind="scatter", x="sepal-length", y="sepal-width")

plt.show()

iris.plot(kind="scatter", x="petal-length", y="petal-width")

plt.show()

sns.violinplot(x="class", y="petal-length", data=iris, size=6)

diagkinds = ['auto', 'hist', 'kde']

for dk in diagkinds:

    sns.pairplot(iris, hue="class", size=3, diag_kind=dk)
    plt.show()

radviz(iris, "class")
plt.show()

## Normal Histogram Plot

iris.hist()
plt.show()

# Correlation Matrix Plot

correlations = iris.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()

for n in names:
    if n != 'class':
        sns.violinplot(x="class", y=n, data=iris, size=6)
        plt.show()