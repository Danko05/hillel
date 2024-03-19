import random

my_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
first_el = my_list[0]
third_el = my_list[2]
two_from_the_end = my_list[-2]
new_list = [first_el, third_el, two_from_the_end]
print(my_list, "==", new_list)
