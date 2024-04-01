def common_elements():
    list_krat_3 = {i for i in range(0, 100) if i % 3 == 0}
    print(list_krat_3)

    list_krat_5 = {i for i in range(0, 100) if i % 5 == 0}
    print(list_krat_5)

    result = list_krat_3.intersection(list_krat_5)
    return result


print(common_elements())
