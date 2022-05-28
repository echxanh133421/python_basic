'''
Xử lý tệp là một phần quan trọng của bất kỳ ứng dụng web nào.
Python có một số chức năng để tạo, đọc, cập nhật và xóa tệp.
'''

#hàm open():hàm chính làm việc với file
#hàm open có 2 tham số: filename, chế độ(mode)
#có 4 chế độ đọc khác nhau:
  #"r"- đọc, mở tệp đọc, lỗi nếu tệp ko tồn tại
  #"a"-append(nối), mở để thêm , tạo tệp nếu tệp ko tồn tại
  #"w"-write- mở file để ghi, tạo tẹp nếu tệp ko tồn tạio
  #"x"-create- tạo tệp được chủi định, trả về lỗi nếu tệp ko tồn tại
#ngoai ra còn chỉ định tệp nê được xử lí chế dộ nhị phân hay là văn bản
#"t"-text
#"b"_binary
#vidu
#mo de doc ce do text
#neu vi tri yep ko duoc dat tuong doi thi phai chi duong dan toi tep
f=open("file.txt","r")
#read(): doc file
#print(f.read())#doc toan bo file
#print(f.read(5))#doc 5 ki tu dau cua file
#doc 2 dong lien tiep goi 2 lenh readline
print(f.readline())#doc 1 dong
print(f.readline())#doc 1 dong
#lặp qua file line
for x in f:
  print(x)
#đóng file
f.close()
#"a": viết vào cuối tệp
#"w": viết từ đầu tệp , đè lên tất cả
#vidu  

# print("\n\n")
# f = open("file.txt", "a")
# f.write("Now the file has more content!")
# f.close()

#open and read the file after the appending:

# f = open("file.txt", "r")
# print(f.read())

#tao 1 file mới
'''
Để tạo một tệp mới bằng Python, hãy sử dụng phương thức open (), với một trong các tham số sau:
"x" - Create - sẽ tạo một tệp, trả về lỗi nếu tệp tồn tại
"a" - Nối - sẽ tạo một tệp nếu tệp được chỉ định không tồn tại
"w" - Write - sẽ tạo một tệp nếu tệp được chỉ định không tồn tại
'''
# f = open("myfile.txt", "w")
#xoa file
#để xóa file bạn import os va su dung function os.remove()
# from os import remove
# remove("myfile.txt")


#kiểm tra tệp có tồn tại không
#Để tránh gặp lỗi, bạn có thể muốn kiểm tra xem tệp có tồn tại hay không trước khi cố gắng xóa nó:

'''
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
'''

#xoa folder
#To delete an entire folder, use the os.rmdir() method:
'''
import os
os.rmdir("myfolder")
'''
#Lưu ý: Bạn chỉ có thể xóa các thư mục trống.