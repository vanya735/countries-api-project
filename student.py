class Student:
    def __init__(self, name, age, grade, average_score):
        self.name = name
        self.age = age
        self.grade = grade
        self.average_score = average_score

    def update_score(self, new_score):
        self.average_score = new_score

    def get_profile(self):
        return (
            f"Учень: {self.name}\n"
            f"Вік: {self.age}\n"
            f"Клас: {self.grade}\n"
            f"Середній бал: {self.average_score}\n"
        )


student1 = Student("Андрій", 14, "8-Б", 10.5)
student2 = Student("Марія", 13, "7-А", 11.2)
student3 = Student("Олег", 15, "9-В", 9.8)

student1.update_score(11.0)

print(student1.get_profile())
print(student2.get_profile())
print(student3.get_profile())
