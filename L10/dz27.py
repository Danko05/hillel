def is_even(digit: int):
    """Перевірка чи є парним число"""
    if digit % 2 == 0:
        return True
    else:
        return False


print(is_even(1021))
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
