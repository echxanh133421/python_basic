#sap xep thuan
my_list=["orange",'mango','kiwi','pineapple','apple']
my_list1=[87,45,65,98,1543,23,67]
my_list.sort()
my_list1.sort()
print(my_list)
print(my_list1)
#sap xep nguoc
my_list1.sort(reverse=True)
print(my_list1)
#tuy chinh sap xep 
#sap xep gan theo muc do gan so 50
def fun(n):
    return abs(n-50)
my_list2=[100,50,65,83,23]
my_list2.sort(key=fun)
print(my_list2)
#sap xep khong phan biet hoa thuong
my_list3=['thanh','Cuong','tuan','Thang']
my_list3.sort(key=str.upper)#or lower
print(my_list3)
#dao nguoc chuoi
my_list4=['a','b','c','d']
my_list4.reverse()
print(my_list4)