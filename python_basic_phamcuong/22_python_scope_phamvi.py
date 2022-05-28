#pham vi bien
#global
#local
#bien global va local cung ten , khi trong pham vi cua local thi bien local ghi de ra khoiopha vi local thi bien local duoc su dung
#key word global
#1: tao 1 bieesn global trong phajm vi local
def create_global_value():
    global x
    x=300
create_global_value()
print(x)
#2: xu dung bien global trong ham
x=300
def my_func():
    global x
    x=400
my_func()
print(x)