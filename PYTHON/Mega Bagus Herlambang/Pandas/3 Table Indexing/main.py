# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv("../kapal_titanic.csv")


data_age = data["age"]
print(data_age)
print(type(data_age))


data_age_2 = data.age
print(data_age_2)
print(type(data_age_2))
print(data.age.equals(data_age))

# <class 'pandas.Series'>

# %%

data_baru = data[["age", "sex"]]
print(data_baru)
print(type(data_baru))

# <class 'pandas.DataFrame'>

# %%

# iloc
# iloc[baris, kolom]
# sama kaya piton awal:akhir, tapi akhirnya itu di exclude.
# pakainya index
print(data.iloc[:11,:4])
print(data.iloc[1:,2:5])
print(data.iloc[:,0])



# 881    NaN
# 882    NaN
# 883    NaN
# 884    NaN
# 885    NaN
# 886    NaN
# 887      B
# 888    NaN
# 889      C
# 890    NaN
# Name: deck, dtype: str
print(data.iloc[-10:,-1])

print(data.iloc[-10:-2,-4:-1])


# print baris yang mau aja (selected)
print("\n\n", "="*20, "print baris yang mau aja (selected)", "="*20, "\n")

print(data.iloc[[0,2,4,10]])
print(data.iloc[[0,2,4,10],[1,3,6]])


# %%

data2 = pd.read_csv("../kapal_titanic.csv", index_col="embarked")


print(data2.loc["S"])
print(data2.loc["S", "age"])
print(data2.loc[["S", "Q"],["age", "fare"]])
print(data2.loc["S",["age", "fare"]])




