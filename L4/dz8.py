# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

my_list = [1,3,6]
if len(my_list) == 0:
    print(my_list)
else:
    last_index = my_list[-1]
    lst = []
    for i, el in enumerate(my_list):
        if i % 2 == 0:
            lst.append(el)
            print(lst)
    summa = sum(lst)
    result = summa * last_index
    print(result)
