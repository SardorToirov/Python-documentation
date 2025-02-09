# 3.1
#   "University" - parent klass. Konstruktorida esa (university) parametrlari bor.
#     info() - (university) ni print qilib beradi.
#
#   "Staff" - child klass. Unda konstruktirida qo'shimcha (first_name, last_name, age) parametrlari bor.
#     staff_info() - (university, first_name, last_name, age) ni print qilib beradi.
#
#   "Student" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (group) parametrlari bor.
#     more_info() - (university, first_name, last_name, age, group) ni print qilib beradi.
#
#   "Teacher" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position, subject) parametrlari bor.
#     more_info() - (university, first_name, last_name, position, subject) ni print qilib beradi.
#
#   "OtherStaff" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position) parametrlari bor.
#     more_info() - (university, first_name, last_name, position,) ni print qilib beradi.
#
# 3.2
# "Object" - child klass. U "University" dan vorislik oladi. Unda konstruktirida qo'shimcha (name) parametrlari bor.
#     object_info() - (university, name) ni print qilib beradi.
#
#   "Computer" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, tizimi, holati) parametrlari bor.
#     object_more_info() - (university, name, soni, tizimi, holati) ni print qilib beradi.
#
#   "Mebel" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, turi, holati) parametrlari bor.
#     object_more_info() - (university, name, soni, turi, holati) ni print qilib beradi.

# class University:
#     def __init__(self,university):
#
#         self.university = university
#     def info(self):
#         print(self.university)
#
# class Staff(University):
#     def __init__(self,university,first_name, last_name, age):
#         super().__init__(university)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def  staff_info(self):
#         print(self.university,self.first_name,self.last_name,self.age)
#
# class Student(Staff):
#     def __init__(self, university, first_name, last_name, age, group):
#         super().__init__(university,first_name,last_name,age)
#         self.group = group
#     def more_info(self):
#         print(self.university,self.first_name,self.last_name,self.age,self.group)



