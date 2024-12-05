"""Foydalanuvchidan bitta so’z kiritishini va keyin matn kiritishini so’rab
 oling. Agar kiritilgan so’z shu matn ichida bo’lsa uni faylga 
 yozyotganizda uning o’rniga * qo’ying. * lar soni so’zning uzunligiga teng 
 bo’lishi kerak."""



 
output_file = "result1.txt"

soz = input("So'z kiriting: ")
matn = input("Matn kiriting: ")

yulduzlar = '*' * len(soz)
ozgartirilgan_matn = matn.replace(soz, yulduzlar)


with open(output_file, 'w') as file:
    file.write(ozgartirilgan_matn)

print(f"Natija: {ozgartirilgan_matn}")
print(f"Natija '{output_file}' fayliga yozildi.")
