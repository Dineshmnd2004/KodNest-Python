class Student:
    def study(self):
        print(self.name, "is Studying")

s1 = Student()
s1.roll = int(input())
s1.name = input()
s1.age = int(input())
s1.marks = int(input())

print(s1.roll)
print(s1.name)
print(s1.age)
print(s1.marks)
s1.study()

s2 = Student()
s2.roll = int(input())
s2.name = input()
s2.age = int(input())
s2.marks = int(input())

print(s2.roll)
print(s2.name)
print(s2.age)
print(s2.marks)
s2.study()