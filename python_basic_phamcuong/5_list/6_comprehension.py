#viết code ngắn hơn'
   # code dài
fruits=['apple','banana','cherry','mango','kiwi']
newlist=[]
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)
   #code ngắn
newlist2=[x for x in fruits if 'a' in x]
print(newlist2)
#các đoạn code ví dụ
 #1
newlist3=[i for i in fruits if i !='apple']
print(newlist3)
 #2
newlist4=[x for x in fruits]
print(newlist4)
 #3
newlist5=[x for x in range(10)]
print(newlist5)
 #4
newlist6=[x.upper() for x in fruits ]
print(newlist6)
 #6
newlist7=['cuong' for x in fruits]
print(newlist7)
 #7
newlist8=[x if x!='banana' else 'orange' for x in fruits]
print(newlist8)
 #9
newlist9=[x if x=='kiwi'else 'orange' for x in fruits]
print (newlist9)