#map()
#syntax:
  #map(func,iterator)
  #thuc thi func voi doi tuong iterator
  #vidu
  #vidu1
def sum(x):
    return x+2
list_temp=[3,6,8,4,5]
list_result=list(map(sum,list_temp))
#cach1
print(list_result)
#cach2
print(list(map(lambda x:x+2,list_temp)))
#cach3
print(list(x+2 for x in list_temp))
#vidu2:viet hoa chu cai dau cua 1 list string
list_name=['cuong','huyen','mai']
#cach1:
print(list(map(lambda x:x.title(),list_name)))
#cach2:
def viethoa(x):
    return x.title()
print(list(map(viethoa,list_name)))
#cach3:
print(list(x.title() for x in list_name))#list_comprehension
#filter()
#synatx:
   #filter(func,iterator)
   #y nghia: loc iterrator khi ham func tra ra dung'
   #vidu: loc ra so le trong list
#cach1:
list_filter=list(filter(lambda x:x%2==1,list_temp))
print(list_filter)
#cach2:
print([x for x in list_temp if x%2==1])#list_comprehension
#cach3:
# print(list_temp)
def bool_odd(x):
    return x%2==1
print(list(filter(bool_odd,list_temp)))
#reduce()
#syntax:
   #reduce(function,iterator): ham co 2 gia tri truyen vao, reduce chi tra ra 1 gia tri
   #vidu:tinh tong 1 list number'
from functools import reduce
import re
list_1=[1,4,6,3,67,9]
#cach1
print(reduce(lambda x,y:x+y,list_1))
#cach2
def sum1(x,y):
    return x+y
print(reduce(sum1,list_1))
#vidu:tim so lon nhat cua list nuumber
#cach1:
print(reduce(lambda x,y:x if x>y else y,list_1))
#cach2:
def max(x,y):
    return x if x>y else y
print(reduce(max,list_1))
#vidu: tinh tong so le cua list number
#cach1: loc ra list cac so le, sau do tinh ton list nay
print(list_1)
print(reduce(lambda x,y:x+y,list(filter(lambda x:x%2==1,list_1))))

