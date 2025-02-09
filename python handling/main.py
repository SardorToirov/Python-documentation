
                             # """PYTHON HANDLING"""

# "r" - O'qish-standart qiymat. O'qish uchun faylni ochadi, agar fayl mavjud bo'lmasa xato
#
# "a" - Qo'shish-qo'shish uchun faylni ochadi, agar u mavjud bo'lmasa, faylni yaratadi
#
# "w" - Yozish-yozish uchun faylni ochadi, agar u mavjud bo'lmasa, faylni yaratadi
#
# "x" - Yaratish-belgilangan faylni yaratadi, agar fayl mavjud bo'lsa, xato qaytaradi

# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)

#---------------------------------------------------------
# f = open("test.py","r")
# print(f.read())

#---------------------------------
# f = open("demofile2.txt", "a")
# f.write("\nNow the file has more content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

#-------------------------------
# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
#
# #open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read())

#--------------------------------
#f = open("myfile.txt", "x")
# f = open("myfile.txt", "w")
# f.write("hello")
#-----------------------------------
                                        #Delete File

# import os
# os.remove("test.py")

#---------------------------------
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
#------------------------------------------
                                        #Delete Folder

# import os
# os.rmdir("myfolder")
