class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def show(self):
        print(f"hello {self.name} \nyour roll is: {self.roll}")

class Ex_Student(Student):
    def playing(self):
        print("they can playing guitar")


std = Student("vibek", 13)
std.show()

stx = Ex_Student("rakesh", 15)
stx.show()
stx.playing()