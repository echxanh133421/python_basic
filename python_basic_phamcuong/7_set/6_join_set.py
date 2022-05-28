#union()
#update()
#dung de noi cac set lai voi nhau
#xoa bat cu phan tu nao bi trung lap
print("uinon()")
set1={1,3,4}
set2={5,6,7}
set3=set1.union(set2)
print(set3)
print("update()")
set1.update(set2)
print(set1)
#intersection_update(): chi giu lai cac phan tu giong nhau
print("intersection_update()")
set1={1,2,3}
set2={2,3,4}
set1.intersection_update(set2)
print(set1)
#intersection():tra ra 1 set co cac phan tu trung lap o 2 set cu
print("intersection()")
set1={1,2,3}
set2={2,3,4}
set3=set1.intersection(set2)
print(set3)
print(set1.intersection(set2))
#symmectric_difference_update()
print("symmectric_difference_update()")
set1={1,2,3,4,5}
set2={3,4,6}
set1.symmetric_difference_update(set2)
print(set1)
#symmectric_difference()
print("symmectric_difference()")
set1={1,2,3,4,5}
set2={3,4,6}
set3=set1.symmetric_difference(set2)
print(set3)
print(set1.symmetric_difference(set2))