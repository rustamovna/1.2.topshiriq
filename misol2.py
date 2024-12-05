'''Quyidagi matn text.txt faylida yozilgan. Siz uning ichidagi har bir so’zning 
birinchi harfini katta harfga o’tkazib result.txt fayliga yozing.'''


file1 = "text.txt"
file2 = "result.txt"

try:
    with open(file1, 'r') as file:
        text = file.read()

    text = text.title()

    with open(file2, 'w') as file:
        file.write(text)


except FileNotFoundError:
    print(f"'{file1}' fayli topilmadi.")
