def find_unique_value(some_list):
    some_list.sort()
    if some_list[0] != some_list[1]:
        return some_list[0]
    if some_list[-1] != some_list[-2]:
        return some_list[-1]
    for i in range(1, len(some_list) - 1):
        if some_list[i] != some_list[i+1] and some_list[i] != some_list[i-1]:
            return some_list[i]


print(find_unique_value([1, 2, 1, 1]))

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
