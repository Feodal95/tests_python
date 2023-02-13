from test11_1 import Student, Direction, Exception, Exception1

student1 = Student("Tom")
student1.display_info()
direction1 = Direction("Python")
direction1.dir()
student2 = Student("Bob")
student2.display_info()
direction2 = Direction("Java")
direction2.dir()

sam = Exception("Sam", "School №9")
sam.name = "Sam"
sam.school = "School №9"
sam.display_info()
alice = Exception1("Alice", "Synergy")
alice.name = "Alice"
alice.university = "Synergy"
alice.display_info()