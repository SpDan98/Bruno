import random

from abc import ABC,abstractmethod

class Hero(ABC):
    @abstractmethod
    def beat(self):
        pass

class Sword:
    def __init__(self,name,attack) -> None:
        self.name=name
        self.attack=attack


class Bow:
    def __init__(self,name,attack) -> None:
        self.name=name
        self.attack=attack

class Armor:
    def __init__(self,defence) -> None:
        self.defence=defence

class Warrior:
    def __init__(self,name,hp,attack,sword,armor) -> None:
        self.name=name
        self.sword=sword
        self.attack=attack
        self.hp=hp
        self.armor=armor
    def beat(self,other:'Warrior'):
        if other.armor==0:
            other.hp-=self.attack+self.sword.attack
        else:
            other.armor-=self.attack+self.sword.attack
        

class Archer(Hero):
    def __init__(self,name,hp,attack,bow,chance,armor) -> None:
        self.name=name
        self.bow=bow
        self.hp=hp
        self.attack=attack
        self.chance=chance
        self.armor=armor
    def beat(self,other:'Archer'):
        check=random.randint(1,100)
        if check<=self.chance:
            attack=self.attack*2
            print('Критическая атака')
        else:
            attack=self.attack
        if other.armor==0:
            other.hp-=attack+self.bow.attack
        else:
            other.armor-=attack+self.bow.attack

class Batle:
    @staticmethod
    def batle(p1,p2):
        while True:
            if p1.hp<=0:
                print(f'{p2.name} победил')
                break
            if p2.hp<=0:
                print(f'{p1.name} победил')
                break
            who=random.randint(0,1)
            if who==0:
                p1.beat(p2)
                print(f'{p1.name} бьет {p1.attack} {p2.armor} {p2.hp}')
            elif who==1:
                p2.beat(p1)
                print(f'{p2.name} бьет {p2.attack} {p1.armor} {p1.hp}')
w1=Warrior('Aragorn',500,10,Sword('Anduril',50),500)
w2=Archer('Legolas',500,10,Bow('BowWw',50),30,300)

Batle.batle(w1,w2)