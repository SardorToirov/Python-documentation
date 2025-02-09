import json
# json.dumps(x) dict ni json formatga otqazadi!
# #
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# sort the result alphabetically by keys:
# print(json.dumps(x, indent=4, sort_keys=True))

#-----------------------------------------------------
# """ PYTHONDAN JSONGA """
#
# bemorj = {
#   "ism": "Axmat Tolayev",
#   "yosh": 20,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }
# #
# with open('formtojson.json','w') as f:
#     a = json.dump(bemorj,f,indent=4)
#-----------------------------------------------------
# """JSONDAN PYTHONGA"""
# # bemor = json.loads(a)
# # print(bemor)
#
# filename = 'formtojson.json'
# with open(filename) as f:
#     bemors = json.load(f,indent=4)
# print(bemors)

#---------------------------
file = 'students.json'
with open(file) as f:
    d = json.load(f)
    print(d)
    with open('add.text','w') as p:
        g = json.dump(d,p,indent=4)

