class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return super().__str__() + f", Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return super().__str__() + f" Subject: {self.subject}"


avichay=Teacher('avichay',35,'Devops')
print(avichay)