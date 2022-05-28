#tính kế thừa cho phép chúng ta ta định nghĩa một lớp kế thừa tất cả cá phương thức và thuộc tính từ 1 lớp khác
#lớp cha
#tạo lớp cha như 1 lớp bình thường
# from tkinter import Y


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname+" "+self.lastname)
#lớp con 
#tạo lớp con: thêm lớp cha vào trong ngoặc
class student(person):
    pass
x=student("cuong","pham")
x.printname()
#khi tạo lớp con thì cần thêm __init__() method :khi đối tượng đưuọc tạo thì hàm __init__ được gọi tự động
#hàm __init__khồng được kế thừa từ lớp cha
#để giữ tính kế thừa của hàm cha thì ta cần thêm lệnh gọi hàm __init__ của cha
class Student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
#hàm super()
class Student2(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)  

z=Student2("cuong","pham")
z.printname()
#thêm properties,method
class Student3(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)  
        self.graduationyear=year
    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
x=Student3("cuong","pham",2023)
print(x.graduationyear)
