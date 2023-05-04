# a=10
# word='Hello'
# print(type(a),type(word))

# class Person:
#     name='Dan'
#     age=24
# me=Person()
# print(me.age)

# class Person:
#     name=''
#     age=0
#     def go(self):                                 #метод
#         print('go')
#     def jump(self):                               #метод
#         print('jump')
# p1=Person()
# p1.name='Misha'
# p1.age=22
# p2=Person()
# p2.name='Dan'
# p2.age=24
# print(p1.name,p1.age)
# print(p2.name,p2.age)
# p1.go()
# p2.go()
# p1.jump()
# p2.jump()

# class Point:
#     def __init__(self) -> None:
#         print('it is init magic method')
# p=Point()

# class Point:
#     def __init__(self,x,y) -> None:                     #конструктор
#         self.x=x
#         self.y=y
#     def __str__(self) -> str:                           #конструктор
#         return str(f'{self.x},{self.y}')
#     def __add__(self,other):
#         return Line(self,other)
# # p=Point(1,2)
# # print(p)

# class Line:
#     def __init__(self,p1:Point,p2:Point) -> None:
#         self.p1=p1
#         self.p2=p2
#     def __str__(self) -> str:
#         return self.p1.__str__() + ' x ' + self.p2.__str__()
# p1=Point(1,2)
# p2=Point(3,4)
# l=Line(p1,p2)
# print(l)
# p3=p1+p2
# print(p3)

class Cart:
    def __init__(self,wheels,price,body) -> None:
        self.price=price
        self.wheels=wheels
        self.body=body


# class Car:
#     def __init__(self,wheels,price,engine,body) -> None:
#         self.price=price
#         self.wheels=wheels
#         self.engine=engine
#         self.body=body


from abc import ABC,abstractclassmethod

class Transport(ABC):
    @abstractclassmethod
    def move(self):
        pass
    

class Car(Cart):
    def __init__(self,wheels,price,engine,body) -> None:
        super().__init__(wheels,body,price)
        self.engine=engine
    def move(self):
        print('move')
        

class Wheel:
    def __init__(self,d,disk,tire) -> None:
        self.d=d
        self.disk=disk
        self.tire=tire
    def move(self):
        print('move')

class Engine:
    def __init__(self,power,cylinder) -> None:
        self.power=power
        self.cylinder=cylinder

class Cylinder:
    def __init__(self,num) -> None:
        self.num=num

class Disk:
    def __init__(self,title) -> None:
        self.title=title

class Tire:
    def __init__(self,title) -> None:
        self.title=title

wheel=Wheel(15,Disk('d1'),Tire('summer'))
engine=Engine(300,Cylinder('6'))
car=Car([wheel,wheel,wheel,wheel],1000,engine,'body')
print(car.engine.cylinder.num)