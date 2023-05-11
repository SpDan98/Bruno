class StringVar:
    def __init__(self,value) -> None:
        self.value=value
    def get(self):
        return self.value
    def set(self,value):
        self.value=value
sv=StringVar('value')


class Point:
    def __init__(self,x,y) -> None:                     #конструктор
        self.x=x
        self.y=y
    def __str__(self) -> str:                           #конструктор
        return str(f'{self.x},{self.y}')
    def __add__(self,other):
        return Line(self,other)
# p=Point(1,2)
# print(p)
