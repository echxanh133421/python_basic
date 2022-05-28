
#bien toan cuc
x='cuong dep trai'
def myfunction():
    #bien cuc bo
    x='dep trai'
    x+=' vai'
    print('tu nhan thay '+x)
#bien cuc bo duoc uu tien trong ham va bien toan cuc khong doi
myfunction()
#bien toan cuc khong doi
print(x)

#tu khoa global
def function():
    global c 
    c= 'cuong dep trai nhat xom'
    print(c)
function()
print(c)