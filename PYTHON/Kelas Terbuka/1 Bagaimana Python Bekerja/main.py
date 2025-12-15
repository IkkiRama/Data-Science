import time
start_time = time.time()

print("Hello World")

print("Hello")
print("World")

# Ini adalah komentar

a = 10 #ini adalah komen juga
print(a)

"""
INI ADALAH MULTI LINE KOMENTAR
"""

# print(b)
b = 11

"""
Kita bisa mengcompile python ke yang namanya byte code (lebih cepat)

python -m py_compile ./main.py
run the file in __pycache__
"""

print(time.time() - start_time)

