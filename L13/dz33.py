class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender},{self.age}, {self.first_name}, {self.last_name}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()},{self.record_book}"


class UserException(Exception):
    def __init__(self, message= "Максимум 10 людей у групу"):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise UserException
        self.group.add(student)
        return self.group

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.discard(student_to_delete)
            return self.group

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students = ''.join(str(student))
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st4 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st5 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st7 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st8 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st9 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st10 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st11 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')
print("OK")
