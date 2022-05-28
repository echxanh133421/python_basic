#python la 1 ngon ngu lap trinh huong đối tượng
#hầu hết mọi thứ trong python đều là 1 dối tượng, với các thuộc tính và phương thức
# tạo 1 class:
class Myclass:
    x=5
#tạo 1 object
p0=Myclass()
print(p0.x)
#hàm __init__()
#tất cả các class đều có hàm __init__(),nó đưuọc thực thi khi lớp đang được khởi tạo
#vidu
class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
p1=Person("Cuong",21)
print(p1.name)
print(p1.age)
#hàm __init__() được gọi tự động khi lớp được sử dụng để tạo một đối tượng mới
#method in objects
#vidu
class Person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello my name is "+self.name)
p2=Person2("cuong",21)
p2.myfunc()
#tham số self là 1 tham chiếu đến đối tượng hiện tại được dùng để truy cập đến các biến của class
#nó không nhất thiết phải được đặt tiên riêng,bạn có thể gọi bất cứ thứ gì bạn thích, nhưng nó phải là tham số ddaaafu tiên của bất kỳ hàm nào trong lớp
#vidu
class person3:
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age
    def myfunc(abc):
        print("hello my name is "+abc.name)
p3=person3("cuong",21)
p3.myfunc()
#sua đoi thuoc tinh doi tuong
p3.age=22
#xoa thuoc tính đối tượng , thuoojc tính mất luôn và không còn tồn tại
del p3.age
#định nghĩa class không được để trống , nếu không muốn ghi gì thì ghi pass
class person4:
    pass

