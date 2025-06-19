class GroupLimitError(Exception):
    def __init__(self, message="Неможливо додати більше 10 студентів до групи"):
        super().__init__(message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, {self.gender}, {self.age}, Record: {self.record_book}"

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(st) for st in self.group)
        return f'Group Number: {self.number}\n{all_students}'


# === Тест ===
gr = Group("PD1")

for i in range(10):
    st = Student("Male", 20+i, f"Name{i}", f"Last{i}", f"RB{i}")
    gr.add_student(st)

print(gr)

# 11-й студент
try:
    gr.add_student(Student("Female", 22, "Extra", "Student", "RB11"))
except GroupLimitError as e:
    print(f"Виняток: {e}")
