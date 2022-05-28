#toan tu cong +
list1=[1,2,3]
list2=['a', 'b', 'c']
list3=list2+list1*2
print(list3)
#dung append
list4=list(list1)#list4=list1.copy()
for x in list2:
    list4.append(x)
print(list4)
#method extend
list5=list1.copy()
list5.extend(list2)
print(list5)