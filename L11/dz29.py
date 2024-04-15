def is_prime(nums):
    if nums <= 1:
        return False
    if nums == 2:
        return True
    if nums % 2 == 0:
        return False
    i = 3
    while i * i <= nums:
        if nums % i == 0:
            return False
        i += 2
    return True


def prime_generator(end):
    num = 2
    while num <= end:
        if is_prime(num):
            yield num
        num += 1


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
