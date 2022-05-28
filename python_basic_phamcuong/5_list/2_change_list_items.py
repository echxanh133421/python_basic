#thay the 1 phaan tu
mylist=['a','b','c','d']
mylist[1]='c'
print(mylist)
#thay the nhieu phan tu
mylist[1:3]=['g','h']
print(mylist)
#thay the nhieu phan tu hon phan tu muon thay the
mylist[1:2]=['a','c']
print(mylist)
#thay the it phan tu hon phan tu muon thay the
mylist[1:3]=['d']
print(mylist)
#them phan tu moi
mylist.insert(3,'deptrai')
print(mylist)