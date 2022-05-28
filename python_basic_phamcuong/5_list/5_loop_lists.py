#lặp qua 1 chuỗi
my_list=['a' ,'b' ,'c']
for i in my_list:
    print(i)
#dùng chỉ số 
for i in range(len(my_list)):
    print(my_list[i])
#dùng vòng lặp while
i=0
while i<len(my_list):
    print(my_list[i])
    i+=1
#list_comprehension
[print(x) for x in my_list]