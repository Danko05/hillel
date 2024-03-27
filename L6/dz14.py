while True:
    nums = input("Введіть ціле число: ")
    product_of_numbers = 1
    while len(nums) > 1 or int(nums) > 9:
        product_of_numbers = 1
        for digit in nums:
            if digit != 0:
                product_of_numbers *= int(digit)
        nums = str(product_of_numbers)

    print(product_of_numbers)
    if product_of_numbers <= 9:
        break
