class Student:
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print("Меня зовут ", self.name)

class Direction:
    def __init__(self, name):
        self.name = name
    def dir(self):
        print("Направление", self.name)

class Exception:
    def __init__(self, name, school):
        self.name = name
        self.school = school
    def display_info(self):
        print(self.name, "учится в ", self.school)
        
class Exception1:
    def __init__(self, name, university):
        self.name = name
        self.university = university
    def display_info(self):
        print(self.name, "окончил ", self.university)