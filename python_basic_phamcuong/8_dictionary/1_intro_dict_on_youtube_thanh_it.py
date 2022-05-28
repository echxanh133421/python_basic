#dict
#khai báo 
x={}
print(type(x))
#key and value
x={'key':3.5,'key2':['a','b'],2:8}
print(x)
print(x['key'])
x[2]=9
x['cuong']="nho phan huyen"
print(x)
#kiem tra xem cai key cos thuoojc x khongo
print(2 in x)
#lay ra key cua dict
print(x.keys())
list1=list(x.keys())
print(list1)
#laasy ra value
print(list(x.values()))
#xoa 1 key vaf ca value cua no
del x['key']
print(x)
#in ra key va value
#c1
print("duyet dict\nc1")
for key,value in x.items():
    print(key, value)
#c2
print("c2")
for key in x.keys():
    print(key,x[key])