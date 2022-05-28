#có thể khia báo list trong list
#phép gán là tham chiếu : tức là nếu thay đổi 1 list thì list còn lại cũng sẽ thay đổi

list1=["cuong",2,True]
print(list1)
list2=list1
list2[0]='phan huyen'
print("tham chiếu")
print(list1)
print(list2)
#neesu không muiooosn bị tham chiếu thì làm như sau
list3=list1[:]
list1[0]="pham cuong"
print("fix tham chiếu")
print(list1)
print(list3)