#json la 1 cus phasp de  luu tru(storing) va trao doi(exchanging) data
#json la 1 text, duoc viet voi ki hieu doi tuong javascrip
#python cos 1 gois tich hop(built-in package) goij la json
#co the duoc su  dung lam viec voi du lieu
#import
import json
#phan tich cu phap json, chuyen doi tu json sang python
#neu co 1 chuoi json , thi co the phan tich cu phap bang cach su dung json.loads() method
#vidu
x='{"name":"cuong","age":21,"nationalyty":"vietnamese"}'
y=json.loads(x)
print(type(y))
print(y)
#chuyen tu python sansg json: json.dumps() method
x=[2,3,45,6,"cuong","21","vietnamese"]
y=json.dumps(x)
print(y)
print(type(y))#json is a text
# ban co the chuyen doi python object thuoc cac loai sau thanh chuoi json
   #dict
   #tuple
   #list
   #string
   #int
   #float
   #True
   #False
   #None
print("cac object chuyen doi sang json")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#kieu chuyen doi 
#python        json
#dict          Object
#list,tuple    Array
#str           String
#int,float     Number
#True          true
#False         false
#None          null


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y=json.dumps(x)
print(y)
print(type(y))
#json.dumps(): co them tham so de doc de hon, tham so xac dinh thut le
y=json.dumps(x,indent=4)
print(y)
z=json.dumps(x, indent=4, separators=(". ", " = "))#phan tach doi tuong bang dau . va thay dau : thanh dau =
print(z)
y=json.dumps(x,indent=4, sort_keys=True)# chi dinh co sap xep hay khong, sap xep alpahbet
print(y)