# class FlyingMixin:
#     def fly(self):
#         return f"{self.__name}이(가) 비행합니다."
# class SwimmingMixin:
#     def swim(self):
#         return f"{self.__name}이(가) 수영합니다."
# class Pokemon:
#     def __init__(self, name, hp):
#         self.__name = name
#         self.hp = hp
#
#     def attck(self):
#         print("공격~")
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
# # name = property(get_name, set_name)
#
#     #magic method
#     def __str__(self):
#         return self.__name + "입니다."
#     def __add__(self, target):
#         return '('+self.__name + ' + ' + target.__name + ") 입니다. " +  f"두 포켓몬 체력의 합은 {self.hp + target.hp} 입니다."
#
# class Charizard(Pokemon,FlyingMixin):
#     pass
# class Gyarados(Pokemon, SwimmingMixin):
#     pass
#
# g1 = Gyarados("갸라도스",95)
# c1 = Charizard("리자몽", 78)
# print(g1, c1)
# print(g1 + c1)

# Aggregation and Composition

class FlyingBehavior: #컴포지션
    def fly(self):
        return f"비행합니다."
class Nofly(FlyingBehavior):
    def fly(self):
        return f"비행이 불가합니다."
class JetPack(FlyingBehavior):
    def fly(self):
        return f"아이템을 사용해 비행이 1회 가능합니다."
class Flywithwings(FlyingBehavior):
    def fly(self):
        return f"비행이 가능합니다."
class SwimmingBehavior:
    def swim(self):
        return f"{self.__name}이(가) 수영합니다."
class Pokemon: # 상속
    def __init__(self, name, hp, fly_behavior):
        self.__name = name
        self.hp = hp
        self.fly = fly_behavior # aggregation (has-a)
    def set_fly_behavior (self, fly) :
        self.fly_behavior = fly

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

class Charizard(Pokemon,FlyingBehavior):
    pass
class Pikachu(Pokemon, Nofly):
    pass
class Gyarados(Pokemon, SwimmingBehavior):
    pass

nofly = Nofly()
p1 = Pikachu("피카츄", 35, nofly)
print(p1.fly.fly())
wings = Flywithwings()
c1 = Charizard("리자몽", 78, wings)
g1 = Gyarados("갸라도스",95,nofly)
print(c1.fly.fly())
print(p1.fly.fly())
p1.set_fly_behavior(JetPack())
print(p1.fly_behavior.fly())