import string

hashtag = input("Введіть:")
result_string = ""
for i in hashtag:
    if i not in string.punctuation:
        result_string += i
result = "#" + "".join(result_string).title()
result1 = result.replace(" ", '')[:6]
print(result1)



