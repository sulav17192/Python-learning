# class Student:
#     name= "Sulav Aryal"
#     def __init__(self):
#         print("Hello World!!")

# s1= Student()



class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print("Hello World!!")

s1= Student("Sulav", 99)
print(s1.name, s1.marks)

s2= Student("Alex", 98)
print(s2.name, s2.marks)