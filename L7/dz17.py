def correct_sentence(text):
    first_letter = text[0]
    last_symbol = text[-1]
    if last_symbol != ".":
        sentence = first_letter.upper() + text[1:] + "."
    else:
        sentence = first_letter.upper() + text[1:]
    return sentence


result = correct_sentence("greetings, friends.")
print(result)

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
