def is_even(number):
    number_srt = str(number)
    last_number = number_srt[-1]
    if int(last_number) in [1, 3, 5, 7, 9]:
        return False
    else:
        return True


print(is_even(1056897 ** 2))

assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('OK')
