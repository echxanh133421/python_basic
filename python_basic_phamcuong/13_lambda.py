#lambda la 1 ham an danh
#co the nhan bat ki gia tri doi so nao,nhung chi co the co 1 gia tri bieu thuc
#SYSTAX
#lambda arguments: expression
# vidu
x=lambda a:a*3
print("in ra so gap 3 lan so truyen vao")
print(x(int(input())))
#vidu
x ="GeeksforGeeks"
(lambda y : print(y))(x)
#suc manh cua lambda the hien qua khi dung no trongg 1 ham
#vidu
print("su dung lambda trong ham")
def Fun(n):
    return lambda a:a*n
mydouble=Fun(2)
mytriple=Fun(3)
print(mydouble(3))
print(mytriple(5))
#vidu2 sap xep theo rti tuyet doi
print("vidu 2 sap xep theo tri tuyet doi")
list2=[4,3,6,-4,0,-3,8,-6]
print(sorted(list2))
def FUN(list_sort):
    return abs(list_sort)
print(sorted(list2,reverse=True,key=FUN))
print(sorted(list2,reverse=True,key=lambda x: abs(x)))
#hàm sorted() có 3 tham số
#1. ddososi tượng set list, tuple ,dict, iterator
#2. reverse= true theo thứ tự ngược
#3.key so sánh với giá trị của key để sắp xếp , ko ghi thì mặc định giá trị của key là NONE
                                             #mot so vi du ve lambda
       #vidu1:
#tajo ra 1 list  goofm cac ham :
tables = [lambda y=y:y*10 for y in range(1, 11)]
for table in tables:
    print(table())

       #vidu2
Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))