#%, .format(), f-string
my_string="tôi la cuong"
age=21
money=10.45
hello="xin chao python %s ,%i tuoi co %.2f" %(my_string,age,money)
print(hello)
#2
hello2="xin chao python {} ,{} tuoi co {:0.2f}".format(my_string,age,money)
print(hello2)
#3 f-sstring
hello3=f"xin chao python {my_string} ,{age} tuoi co {money:0.2f}"
print(hello3)

