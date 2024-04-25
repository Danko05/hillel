from student import Student
from group import Group
from exeption import UserException

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
sts = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

for i in sts:
    try:
        gr.add_student(i)
    except UserException as e:
        print(e.message)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')
assert gr.find_student('Jobs') == st1
print("OK")