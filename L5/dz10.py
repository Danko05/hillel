import keyword
import string
while True:
    name = input('Введіть назву: ')

    valid = True

    if name[0].isdigit():
        valid = False

    if name.isdigit():
        valid = False

    if name in keyword.kwlist:
        valid = False

    for char in name:
        if char.isupper() or char in string.punctuation.replace('_', ''):
            valid = False
        if char == " ":
            valid = False

    if name.count('__') > 0:
        valid = False

    print(valid)
