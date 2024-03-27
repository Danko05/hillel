import string

letters = string.ascii_letters

letters_range = input("Введіть діапазон букв:")
first_letter = letters_range[0]
second_letter = letters_range[-1]
print("Ваш діапазон:", first_letter + "-" + second_letter)
index_first_letters = letters.index(first_letter)
index_second_letters = letters.index(second_letter)


print(letters[index_first_letters:index_second_letters+1])
