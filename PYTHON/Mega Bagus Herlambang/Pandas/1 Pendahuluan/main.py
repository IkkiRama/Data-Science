# Pandas itu librari yang digunakan untuk mengolah data, terutama data yang berbentuk tabel. Dengan menggunakan Pandas, kita bisa dengan mudah melakukan berbagai operasi seperti filtering, grouping, dan manipulasi data lainnya.

# Untuk menggunakan Pandas, kita perlu mengimpor library tersebut terlebih dahulu. Berikut adalah contoh cara mengimpor Pandas:
import pandas as pd

data = pd.read_csv("kapal_titanic.csv")
print(data)

# Akan menampilkan 5 data pertama
print(data.head())

# Akan menampilkan 5 data terakhir
print(data.tail())

# %%
data.to_csv("Coba.csv", index=False)
data.to_excel("Coba.xlsx", index=False, sheet_name="Asik")

pd.read_csv("Coba.csv")
# %%
