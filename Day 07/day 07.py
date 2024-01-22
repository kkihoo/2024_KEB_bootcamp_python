class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 비행합니다."
class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영합니다."
class Pokemon:
    def __init__(self, name, hp):
        self.__name = name
        self.hp = hp

    def attck(self):
        print("공격~")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
# name = property(get_name, set_name)

    #magic method
    def __str__(self):
        return self.__name + "입니다."
    def __add__(self, target):
        return '('+self.__name + ' + ' + target.__name + ") 입니다. " +  f"두 포켓몬 체력의 합은 {self.hp + target.hp} 입니다."

class Charizard(Pokemon,FlyingMixin):
    pass
class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스",95)
c1 = Charizard("리자몽", 78)
print(g1, c1)
print(g1 + c1)