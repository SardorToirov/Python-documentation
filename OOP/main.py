# 8. "MyClass8" nomli klass elon qililar. Bu klassdan "numbers" list o'zgaruvchisi bor.
# compare_lists(new_list) - bu funksiya klassdagi "numbers" ni elementlar yig'indisi
# "new_list" ni elementlar yig'indisidan katta aniqlab katta listni print qilsin.

# class MyClass8:
#     def __init__(self):
#         self.numbers = []
#
#     def compare_lists(self,new_list):
#         sum_numbers = sum(self.numbers)
#         sum_new_list = sum(new_list)
#
#         if sum_numbers > sum_new_list:
#             print(sum_numbers)
#         else:
#             print(sum_new_list)
#
# obj = MyClass8()
# obj.numbers = [1,2,3,4,5]
# obj.compare_lists([2,1,4,1,8,8])

# 10. "MyClass10" nomli klass elon qililar. Bu klass "numbers" list o'zgaruvchilari bor.
# divide(d) - bu funksiya klassadagi "numbers" list elementlarini "d" qoldiqsiz bo'linsa bitta list yig'sin funksiyani ichida.
# va funksiya oxirida bolinadigonlarni listini return qilsin.

# class MyClass10:
#     numbers = []
#
#     def divide(self,d):
#         result = [i for i in self.numbers if i % d == 0]
#         return result
# print("list malumotlari: [1,2,15,3,4,10,55,77]")
# b = int(input("son kiriting: "))
# obj = MyClass10()
# obj.numbers = [1,2,15,3,4,10,55,77]
# a = obj.divide(b)
# print(a)

# vorisdorlik-1:
#   "Texnika" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
#     info() - (brand, model, type) ni print qilib beradi.
#
#   "Notebooks" child klassi bor. Unda konstruktirida qo'shimcha (video_card, ram, display).
#     more_info() - (brand, model, type, video_card, ram, display) ni print qilib beradi.
#
#   "Televisions" child klassi bor. Unda konstruktirida (size, display) parametrlari bor.
#     more_info() - (brand, model, type, size, display) ni print qilib beradi.
#
#   "Smartphones" child klassi bor. Unda konstruktirida (size, sim_count) parametrlari bor.
#     more_info() - (brand, model, type, size, sim_count) ni print qilib beradi.
#
# class Texnika:
#     def __init__(self,brand, model, type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         info = f"brand nomi:{self.brand}\n" \
#                    f"modeli: {self.model}\n" \
#                    f"type: {self.type}\n"
#         print(info)
#
# class Notebooks(Texnika):
#     def __init__(self,brand, model,type,video_card, ram, display):
#         super().__init__(brand, model, type)
#         self.video_card = video_card
#         self.ram = ram
#         self.display = display
#
#     def more_info(self):
#         more = f"Brand: {self.brand}\n Model: {self.model}\n Type: {self.type}\n " \
#                f"Video Card: {self.video_card}\n RAM: {self.ram}\n Display: {self.display}"
#         print(more)
#
#
#
# obj = Texnika("BMW","E34",True)
# obj.info()
#
# obj1 = Notebooks("HP","Victus",True,"RTX 4050","8GB","180x150")
# obj1.more_info()






