# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

my_list = [1, 2, 3, 4, 5, 62, 3, 4, 5, 100, 120]
list_len = len(my_list)
mid_list = list_len // 2
if mid_list % 2 == 1 and list_len % 2 == 1:
    first_list = my_list[0: 1 + mid_list]
    second_list = my_list[mid_list + 1:]
    finally_list = [first_list] + [second_list]
    print(finally_list)

if mid_list % 2 == 1 and list_len % 2 == 0:
    first_list = my_list[0: mid_list]
    second_list = my_list[mid_list:]
    finally_list = [first_list] + [second_list]
    print(finally_list)

if mid_list % 2 == 0 and list_len % 2 == 0:
    first_list = my_list[0: mid_list]
    second_list = my_list[mid_list:]
    finally_list = [first_list] + [second_list]
    print(finally_list)

if mid_list % 2 == 0 and list_len % 2 == 1:
    first_list = my_list[0: mid_list + 1]
    second_list = my_list[mid_list + 1:]
    finally_list = [first_list] + [second_list]
    print(finally_list)
