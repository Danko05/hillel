# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

my_list = [1, 2, 3]
list_len = len(my_list)
mid_list = list_len // 2
if mid_list % 2 == 1 and list_len > 3:
    first_list = my_list[0: mid_list]
    second_list = my_list[mid_list: 9]
else:
    first_list = my_list[0: 1 + mid_list]
    second_list = my_list[mid_list + 1: 9]
finally_list = [first_list] + [second_list]
print(finally_list)
