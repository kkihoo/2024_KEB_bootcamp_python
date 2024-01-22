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

# class FlyingBehavior: #컴포지션
#     def fly(self):
#         return f"비행합니다."
# class Nofly(FlyingBehavior):
#     def fly(self):
#         return f"비행이 불가합니다."
# class JetPack(FlyingBehavior):
#     def fly(self):
#         return f"아이템을 사용해 비행이 1회 가능합니다."
# class Flywithwings(FlyingBehavior):
#     def fly(self):
#         return f"비행이 가능합니다."
# class SwimmingBehavior:
#     def swim(self):
#         return f"{self.__name}이(가) 수영합니다."
# class Pokemon: # 상속
#     def __init__(self, name, hp, fly_behavior):
#         self.__name = name
#         self.hp = hp
#         self.fly = fly_behavior # aggregation (has-a)
#     def set_fly_behavior (self, fly) :
#         self.fly_behavior = fly
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
# class Charizard(Pokemon,FlyingBehavior):
#     pass
# class Pikachu(Pokemon, Nofly):
#     pass
# class Gyarados(Pokemon, SwimmingBehavior):
#     pass
#
# nofly = Nofly()
# p1 = Pikachu("피카츄", 35, nofly)
# print(p1.fly.fly())
# wings = Flywithwings()
# c1 = Charizard("리자몽", 78, wings)
# g1 = Gyarados("갸라도스",95,nofly)
# print(c1.fly.fly())
# print(p1.fly.fly())
# p1.set_fly_behavior(JetPack())
# print(p1.fly_behavior.fly())


# class FlyingBehavior: #컴포지션
#     def fly(self):
#         return f"비행합니다."
# class Nofly(FlyingBehavior):
#     def fly(self):
#         return f"비행이 불가합니다."
# class JetPack(FlyingBehavior):
#     def fly(self):
#         return f"아이템을 사용해 비행이 1회 가능합니다."
# class Flywithwings(FlyingBehavior):
#     def fly(self):
#         return f"비행이 가능합니다."
#
# class Pikachu:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         self.fly_behavior = Nofly() #composition
#
# p1 = Pikachu("피카츄", 35)
# print(p1.fly_behavior.fly())

# class FlyingBehavior:
#     def fly(self):
#         return f"하늘을 훨훨 날아갑니다~"
#
#
# class JetPack(FlyingBehavior):
#     def fly(self):
#         return f"로켓추진기로 하늘을 날아갑니다!"
#
#
# class NoFly(FlyingBehavior):
#     def fly(self):
#         return f"하늘을 날 수 없습니다."
#
#
# class FlyWithWings(FlyingBehavior):
#     def fly(self):
#         return f"날개로 하늘을 훨훨 날아갑니다"
#
#
#
# class Pikachu:
#     def __init__(self, name, hp, fly):
#         self.name = name
#         self.hp = hp
#         self.fly_behavior = fly  # aggregation
#
#
# nofly = NoFly()
# p1 = Pikachu("피카츄", 35, nofly)
# print(p1.fly_behavior.fly())

# 모듈
# import mymath as
from mymath import isprime, fahrenheit_to_celsius, celsius_to_fahrenheit

while True :
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit 3) Prime number checker 4) Prime number interval checker 5) Quit program : ")
    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit:.2f}F, Celsius : {fahrenheit_to_celsius(fahrenheit):.2f}C')

    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius:.2f}C, Fahrenheit : {celsius_to_fahrenheit(celsius):.2f}F')

    elif menu == '3':
        number = int(input("Input number : "))
        if isprime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is Not prime number')

    elif menu == '4':
        n1, n2 = map(int, input("Input first second number : ").split())
        n1 ,n2 = min(n1,n2), max(n1,n2)
        # numbers = input("Input first second number : ").split()
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])
        # if n1 > n2:
        #     n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if isprime(number):
                print(number, end= ' ')
        print()

    elif menu == '5':
        print('Terminate Program.')
        break
    else:
        print("Not valid number, Please Enter 1 to 5")