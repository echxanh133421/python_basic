#them module datetime
#vidu in ra thoi gian hieejn taji
import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))#tra lai ten cua ngay trong tuan %M: phut %D :ngay/thang/nam
y=datetime.datetime(2001,3,13)#ngay thang nam sinh xua phan huyen
print(y)
#method dtrftime()
z=datetime.datetime(2001,4,3)
print(z.strftime("%B"))#in ra thang duoi dang chu
#%a %A
#%w
#%d
#%B
#%m
#%y %Y
#%H.....