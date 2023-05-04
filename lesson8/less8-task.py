from bidict import bidict

class Matches:
    matches=bidict({1:'I',5:'V',10:'X',50:'L',100:'C'})

class RomanValueError(Exception):
    def __init__(self,message) -> None:
        self.message=message
    def __str__(self) -> str:
        return self.message


class Converter:
    @staticmethod
    def from_arab_to_rom(value):
        ms=Matches
        temparr1=[]
        
        return RomanNum(value)
    @staticmethod
    def from_rom_to_arab(value):
        ms=Matches()
        temparr=[]
        for i in value:
            temparr.append(ms.matches.inverse[i])
        i=len(temparr)-1
        while i!=0:
            if temparr[i]>temparr[i-1]:
                temparr[i-1]=-temparr[i-1]
            i-=1
        return int(sum(temparr))

class RomanNum:
    def __init__(self,romanvalue) -> None:
        self.romanvalue=romanvalue
    def __str__(self) -> str:
        return self.romanvalue

print(Converter.from_rom_to_arab('XCIX'))

