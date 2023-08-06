import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("C:/Users/dedic/Desktop/PyProject/Mall_Customers.csv")

df.head()

# Univariate Analysis
df.describe()

sns.distplot(df['Annual Income (k$)'])