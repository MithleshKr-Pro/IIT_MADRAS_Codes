class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        # self.__choice = choice    #__choice is private data member
    def display(self):
        print(self.name, self.age)
    
class Employee(Person):
    def __init__(self,name:str,age:int,salary:int):
        super().__init__(name,age)
        self.salary = salary
    def display(self):
        print(self.name, self.age, self.salary)

class Student(Person):
    def __init__(self, name: int, age:int, marks:int):
        super().__init__(name, age)
        self.marks = marks
    
    def display(self):
        super().display()
        print(self.marks)    
    
s1 = Student("Bhuvnesh", 19, 100)
s1.display()

e1 = Employee("Harish", 18, 15000)
e1.display()