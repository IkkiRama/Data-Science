import pandas as pd

data = pd.read_csv("kapal_titanic.csv")

# Melihat 10 data pertama, default nya itu 5
print("\n","="*20, "Melihat 10 data pertama, default nya itu 5", "="*20)

print(data.head())
print(type(data.head()))

# Melihat 10 data terakhir, default nya itu 5
print("\n","="*20, "Melihat 10 data terakhir, default nya itu 5", "="*20)

print(data.tail(10))
print(type(data.tail()))


# Print seluruh data
print("\n","="*20, "Print seluruh data", "="*20)

print(data)
print(type(data))



# Melihat info data
print("\n","="*20, "Print seluruh data", "="*20)

# <class 'pandas.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 9 columns):
#  #   Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   survived  891 non-null    int64  
#  1   pclass    891 non-null    int64  
#  2   sex       891 non-null    str    
#  3   age       714 non-null    float64
#  4   sibsp     891 non-null    int64  
#  5   parch     891 non-null    int64  
#  6   fare      891 non-null    float64
#  7   embarked  889 non-null    str    
#  8   deck      203 non-null    str    
# dtypes: float64(2), int64(4), str(3)

print(data.info())
# %%

# Cara melihat summary secara matematis (stat deskriptif)
print("\n","="*20, "Melihat summary secara matematis (stat deskriptif)", "="*20)

print(data.describe())

#          survived      pclass         age       sibsp       parch        fare
# count  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
# mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# std      0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
# min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
# 25%      0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
# 50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
# 75%      1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
# max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200


# survived rata" 38% yang selamat
# rata" class = 2-3
# umur rata" = 29
# punya saudara = 52%, dll

# Persentil 25 = Q1 = 25%
# Persentil 50 = Q2 = 50% (median)
# Persentil 75 = Q3 = 75%



# Untuk data" yang bersifat non numerik
print("\n","="*20, "Untuk data' yang bersifat non numerik", "="*20)

print(data.describe(include="O"))














