from exeption import UserException


class Group:
    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if len(self.group) >= 10:
            raise UserException
        self.group.append(student)
        return self.group

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)
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
