a='cuong dep trai'
b=list(a)
print(b)
#list comprehension: giúp lấy ra 1 list phần tử theo mong muốn với các viet code ngắn gọn
#new_list[<action> for item in <interator> if<some condition>]
print("vidu1 ")
c=[b.upper() for b in a]
print(c)
print(type(c))
print("vidu2 lấy ra 1 list số lẻ từ 0-9")
d=[number for number in range(0,10) if number%2==1]
print(d)
print("vidu3: tính tiền sau VAT")
list_price=[100,120,80,50]
VAT=0.08

def price_product(price):
    return price*(1+VAT)
d=[price_product(price) for price in list_price]
print(d)
# không nenn sử dụng list_comprehension khi có nhiều điều kiện sau ìf
# vi dụ khoong dufngg được list_comprehension
list1=['a','b','c',1]
# lỗi vì không viết hoa được số 1
# list2=[x.upper() for x in list1]
# print(list2)
# nên viết vòng lặp XỬ LÝ NGOẠI LỆ
list2=[]
for x in list1:
    try:
        list2.append(x.upper())
    except AttributeError:
        pass
print(list2)