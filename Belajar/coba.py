import pandas as pd
import numpy as np

df = pd.read_csv("data_mahasiswa.csv")

df.head()
df.tail()
df.info()
df.describe()
df.columns
df.isnull().sum()