## là 1 khối code
#cách tạo 1 hàm vidu1: tinh tong 2 so
def sum1(a,b):
    return a+b
#caschgoij ham
#vidu
print(sum1(3,4))
#đối số và tham số(parameter and arguments)
#số lượng đối số trong lời gọi hàm phải trùng với với tham số trong phần định nghĩa
# đối số tùy tiện:(arbitrary arguments)
     #nếu không biết có bao nhiêu đối số được chuyền vào hàm, thì dùng dấu * trước tham số trong phần điịnh nghĩ hàm
     # ví dụ1
def myFun(*Kid):
    for x in Kid:
        print(x,end=" ")
myFun('cuong','tuan','thanh','thang')
print("\n")
     #VIDU2
def Fun8(a,b,*args):
    print(a,b)
    for x in args:
        print(x,end=" ")
Fun8(3,"cuong",4,7,"rd")
print("\n")
Fun8(1,2)
print("\n")
#keyword arguments: đi kèm với tên tham số ;
def show(a,b,c):
    print(a)
    print(b)
    print(c)
show(b="cuong",c='pham',a='nho huyen')
print("\n")
#arbitrary keyword arguments
   #khi ban khongbiet co bao nhieu doi so keyword argument
   #them 2 dấu * vào 
   #vidu
def Fun2(**kids):
    print('his last name is '+kids['fname'])
Fun2(fname='pham',lname='tran')
   #vidu2
def Fun9(x,y,**kwargs):
    print(x,y)
    #cach in dict: key and value
    for x,y in kwargs.items():
        print(x,y)
    #cach in dict 2
    for x in kwargs.keys():
        print(x,kwargs[x])
Fun9(1,2,cuong='huyen',huyen='cuong')
#default parameter Value: tham số mặc địn
def Fun3(name='cuong'):
    print("xin chao "+name)
Fun3("huyen")
Fun3()
#truyền danh sách(list) như 1 đối số
def Fun5(food):
    for x in food:
        print(x)
Fun5(['apple','banana','cherry'])
#trả về giá trị từ khóa return 
#pass statement:
#đệ quy: recursion
#hàm trả về nhiều giá trị: 
   # giải nén trong python
#ham co the viet trong 1 ham khac
