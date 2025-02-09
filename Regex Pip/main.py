
#https://ihateregex.io/

import re

#
# txt = "The rain sardor in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)
#
em = "te text your password: toirovsardor62@gmail.com emile adress"

em = re.search("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+",em)
print(em)



