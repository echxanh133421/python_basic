#đối tượng lặp
#vidu
my_list=['cuong','phan huyen','duy','tuan']
my_iter=iter(my_list)
print(type(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#1 string cũng là iterable objects
#for loop lặp qua đối tượng string, list, set.... :bản chất là tạo ra đối tượng lặp(iter) và nhảy tới đối tượng tiếp theo(next)
#class objects , iterator objects
#__next__() and __iter__()
class number:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x

my_class=number()
my_iter2=iter(my_class)
print(next(my_iter2))
print(next(my_iter2))
print(next(my_iter2))
print(next(my_iter2))
#lặp vô hạn
# for x in my_iter2:
#     print(x)
#stopiteration:thêm điều kiện dừng
class number2:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <= 20 :
            x=self.a
            self.a+=1
            return x
        else :
            raise StopIteration
my_number_class=number2()
my_iter_number=iter(my_number_class)
for x in my_iter_number:
    print(x)


