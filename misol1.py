"""Foydalanuvchidan matn kiritishini so’rang. Va uni .txt faylga yozing. 
Va undagi eng uzun so’zni result.txt fayliga yozib qo’ying."""

user_input = input("Matn kiriting: ")

with open("user_input.txt", "w") as file1:
    file1.write(user_input)

words = user_input.split()
uzun_soz = max(words, key=len)

with open("result.txt", "w") as file2:
    file2.write(uzun_soz)

