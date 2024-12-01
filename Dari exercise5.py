class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return(f'Hi i am {self.name} and i am {self.age} years old')

class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def __str__(self):
        return f"Hi, I am {self.name}, I am {self.age} years old, and my grade is {self.grade}."
    

# class student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
        
#     def __str__(self):
#         return f"Hi, I am {self.name}, I am {self.age} years old, and my grade is {self.grade}."
    
        
    

rahamim=person('yosi',24)
yosi=student(rahamim.name,rahamim.age,99)
print(yosi)



        