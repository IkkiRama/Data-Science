data = "Ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
1. dengan menggunakan single quote '...'
1. dengan menggunakan double quote "..."

'''

data = 'Menggunakan single quote'
print(data)

data = 'Menggunakan double quote'
print(data)


print("'Hallo apa kabar?'")
print('"Hallo apa kabar?"')
print("hari ini adalah hari jum'at")



# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('hari ini adalah hari jum\'at')
print('g\'day, isn\'t it?')


# Backslash
print("c:\\user\\Rifki")


# Tab
print("Rifkit\t\t\tRomadhan, jauhan")


# Backspace
print("Rifki \bRomadhan")


# Newline
print("baris pertama.\nbaris kedua.") # LF -> Line Feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> Carriage Return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> Carriage Return Line Feed -> Windows



# 3. String Literal atau raw

# hati-hati
print("C:\new folder") #akan salah path nya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print(""" 

Nama : Rifki Romadhan
Jurusan : IESP

""")

# multiline literal string & raw
print(r""" 

Nama : Rifki Romadhan
Jurusan : IESP\new student

""")


