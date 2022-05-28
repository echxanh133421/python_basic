def input_name():
    name=input("nhap ten: ")
    print(f"ten cua ban la :{name}")
def input_age():
    age=input("nhap tuoi: ")
    print(f"tuoi cua ban la: {age}")
def chuongtrinh():
    input_name()
    input_age()
#nếu không có dòng code phía dưới thì khi ta chỉ import 1 hàm input_name() trong file main2.py
#thì cả file subfile2.py đều chạy 
print("chay file subfile2.py")
if __name__=="__main__":
    
    chuongtrinh()