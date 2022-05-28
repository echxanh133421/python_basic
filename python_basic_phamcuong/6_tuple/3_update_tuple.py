
#1.thay ddooir phaafn tuwr
#tuple không cho phép thay dổi sửa xóa phần tử
#cách làm là chuyển sang list rồi thay đổi trên list sau đó chuyển lại tuple

#2.theem phan tu : 2 cach: chuyen sang list
#                          add tuple to a tuple
this_tuple=('a','b','c')
y=('d',)
this_tuple+=y
print(this_tuple)
#3.xoas phan tu
#ep sang list dung remove
#xoa luon tuple, tuple ko ton tai nx, dùng del