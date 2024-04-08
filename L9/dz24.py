def difference(*args):
    if not args:
        return 0
    else:
        if all(isinstance(arg, (int, float)) for arg in args):
            max_value = max(*args)
            min_value = min(*args)
            result = max_value - min_value
            return round(result, 2)
        else:
            return 0


print(difference((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
