file1 = "text_data.txt"
file2 = "sorted_words.txt"

try:
    with open(file1, 'r') as file:
        text = file.read()

    words = [word.strip(".,!?;:") for word in text.lower().split()]

    words2 = sorted(set(words))

    with open(file2, 'w') as file:
        for word in words2:
            file.write(word + "\n")


except FileNotFoundError:
    print(f"'{file1}' fayli topilmadi. Iltimos, faylni yuklang.")
