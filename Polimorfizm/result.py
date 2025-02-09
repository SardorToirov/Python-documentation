from add import add_num
from sub import sub_num
from mul import mul_num
from div import div_num
#x = ((i + j)*(j+45))/(10-i)

i = float(input("i ni kiriting: "))
j = float(input("j ni kiriting: "))
def calculat_res(i,j):
    p1 = add_num(i,j)
    p2 = add_num(j,45)
    p3 = mul_num(p1,p2)
    p4 = sub_num(10,i)

    return div_num(p3,p4)


x = calculat_res(i, j)
print("Natija:", x)
