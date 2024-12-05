from datetime import datetime


"""Foydalanuvchidan ismini va istalgan matnni kiritishini so’ng. 
Va har bir kiritilgan matnni uning vaqti bilan birga chat.txt fayliga saqlang."""

fayl_nomi = "chat.txt"

ism = input("Ismingizni kiriting: ")

print("matn kiriting: ")

while True:
    matn = input(f"{ism}: ")
    
   
    if matn.lower() == "chiqish":
        print("Chat tugatildi.")
        break

    vaqt = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    chat_qatori = f"{vaqt} {ism}: {matn}\n"

    with open(fayl_nomi, 'a') as fayl:
        fayl.write(chat_qatori)

    print(chat_qatori.strip())

