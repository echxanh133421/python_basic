#remove();xoa phan tu cu the
list1=['a','b','c']
list1.remove('b')
print(list1)
#pop():xoa phan tu the chi so
list2=['a','c','d']
list2.pop(1)
print(list2)
#del: 
#  cung xoa duoc index cu the
#  xoa hoan toan danh sach, danh sasch ko ton tai
list3=['d','c','f']
del list3[1]
print(list3)
del list3
#clear(): xoa phan tu nhhung khong xoa danh sasch
list4=['a','d','f']
list4.clear()
print(list4)