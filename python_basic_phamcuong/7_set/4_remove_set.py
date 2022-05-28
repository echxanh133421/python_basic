#remove():xoa phan tu chi dinh, nhung se bi loi neu phan tu xoa khong ton tai
this_set={1,2,3,4,5}
this_set.remove(4)
print("remove()")
print(this_set)
#discard():xoa phan tu chi dinh, KHONG bi loi khi phan tu xoa khong ton tai
print("discard()")
this_set.discard(5)
print(this_set)
#pop():xoa phan tu cuoi cung
#khong birt phan tu cuoi cung do ctdl set
print("pop()")
this_set1={1,3,6,7,8}
x=this_set1.pop()
print(x)
print(this_set1)
#clear()
print("clear()")
this_set2={1,4,5,6,78,6}
this_set2.clear()
print(this_set2)
#del
print("del keyword")
del this_set1
print(this_set1)