class Student:
    def __init__(self, roll_no,name,total):
        self.name = name
        self.roll_no = roll_no
        self.total = total
    def display(self):
        print(self.roll_no, self.name, self.total)
    
    def result(self):
        if self.total>120:
            print("pass")
        else:
            print("fail")
    
s1 = Student(1,"Bhuvnesh", 100)
s1.display()
s1.result()
# print(s1.name, s1.roll_no)

s2 = Student(2, "Harish", 150)
# print(s2.name, s2.roll_no)
s2.display()
s2.result()
