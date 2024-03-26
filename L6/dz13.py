import string

letters = string.ascii_letters
first_letter = input("Введіть 1 букву:")
second_letter = input("Введіть 2 букву:")
print("Ваш діапазон:", first_letter + "-" + second_letter)
index_first_letters = letters.index(first_letter)
index_second_letters = letters.index(second_letter)


print(letters[index_first_letters:index_second_letters+1])
