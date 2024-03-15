# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

my_list = []
len_my_list = len(my_list)
if len_my_list == 0:
    print("Ваш список порожній:", my_list)
else:
    last_index = my_list[-1]
    my_list.insert(0, last_index)
    my_list.pop()
    print(my_list)
