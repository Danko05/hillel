class Rectangle:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __mul__(self, other):

        new_weight = self.weight
        new_height = self.height * other
        return Rectangle(new_weight, new_height)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_height = self.height + other.height + other.weight
            new_weight = self.weight
            return Rectangle(new_weight, new_height)
        else:
            raise TypeError("other не належить класу Rectangle")

    def get_square(self):
        return self.height * self.weight

    def __str__(self):
        return (f'Прямокутник з висотою: {self.height}\n'
                f'шириною: {self.weight}\n'
                f'його площа: {self.get_square()}')


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
r5 = r2 * 5
print(r5)
assert r4.get_square() == 32, 'Test4'
assert r5.get_square() == 90, 'Test6'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print('Ok')
