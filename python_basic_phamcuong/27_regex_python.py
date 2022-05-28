#viet at cua regular expression: bieu thuc chinh quy, la 1 chuoi ki tu tao thanh mot mau tim kiem
#cos the duoc dung ke kiem tra xem 1 chuoi co chua mau tim kiem duoc chi dinh hay khong
import re
#su dung khi lam viex voi bieu thuc chinh quy
#vi du : tim kiem chuoi de xem lieu no ca bat dau ban"the"  va ket thuc bawnfg "spain" hay khong
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
#type x : re.Match
y=bool(x)
print(y)
#1 soos ham regex:
 #findall
 #search
 #split
 #sub
#mecharacters: laf nhuwnxg ky tu co y nghia dac biet
#sets: taajp hop cac ki tu ben trong dau ngoac vuong voi 1 y nghia dac biet



#findall function; tra ve 1 list chua cac gia tri phu hop
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#search function:
#vi du tra ve vi tri dau tien xuat hien khoang trang
txt = "The rain in Spain"
x = re.search("\s", txt)#match object
print(x)
print("The first white-space character is located in position:", x.start()) 
#split function: tra ve danh sach chuoi da duoc tach
#vidu: cat chuoi khi thay dau cach
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# cat chuoi :2 lan gap dau cach
#vidu: thay dau cach bang so 9
txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)



#sub function:thay the ket qua phu hop bang doan text cua ban
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#chi dunh so lan thay the la 2
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#match object:doi tuong phu hop(đối sánh)
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
'''
Đối tượng Match có các thuộc tính và phương thức được sử dụng để truy xuất thông tin về tìm kiếm và kết quả:
.span () trả về một bộ giá trị chứa các vị trí bắt đầu và kết thúc của kết quả khớp.
.string trả về chuỗi được truyền vào hàm
.group () trả về một phần của chuỗi đã có một kết quả khớp
'''
#vidu:
'''
In vị trí (vị trí bắt đầu và kết thúc) của lần xuất hiện đối sánh đầu tiên.
Biểu thức chính quy tìm kiếm bất kỳ từ nào bắt đầu bằng chữ hoa "S":'''
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

