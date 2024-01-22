# 재귀 함수
# def factorial_repetition(n) -> int:
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result
#
# def factorial_recursion(n):
#
#     if n == 1 :
#         return n
#     else:
#         return n * factorial_recursion(n-1)
#
# number = int(input("number : "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))

# #예외처리
# import random
#
# class OopsException(Exception):
#     pass
#
#
# numbers = [random.randint(1,100) for i in range(5)]
# print(numbers)
#
# try :
#     pick = int(input(f'Input index (0 ~ {len(numbers)-1}) : '))
#     print(numbers[pick])
#     print(5/2)
#     raise OopsException("Oops~") #강제로 에러 걸기
# except IndexError as err :# 먼저 디테일한 에러들을 처리해줌
#     print(f"Out of range : Wrong index number\n{err}")
# except ValueError as err : # as 'name' 하고 출력에 넣으면 에러뜬 이유를 텍스트로 보여줌
#     print(f"Input only Number!\n{err}")
# except ZeroDivisionError as err : #print(5/0)에 대한 예외처리
#     print(f'The denominator cannot be 0.\n{err}')
# except OopsException as err :
#     print(f'Oops Oops {err}')
# except Exception as err: # 보험식으로 맨 밑으로 가는것이 문법적으로 옳다
#     print(f"Error occurs\n{err}")
# else :
#     print(f'Program terminate')

#
# def desc(f):
#     def wrapper():
#         print("study")
#         f()
#     # print("a")
#     return wrapper
#
# def something():
#     print("do something")
#
# s = desc(something)
# s()

## 객체
# class Poketmon:
#     pass
# pikachu = Poketmon()
# squirtle = Poketmon()
# pikachu.name = "피카츄"
# pikachu.nemesis = squirtle
# print(pikachu.name)
# squirtle.name = "꼬부기"
# print(pikachu.nemesis.name) # squirtle.name 과 동일
# print(squirtle.name)
#
# #메소드 : 클래스 또는 객체의 함수.
# class Poketmon:
#     def __init__(self, name): # self는 자동으로 들어가는 매개변수 , # __init__ 는 개별 객체를 초기화 하는 매소드
#         self.name = name
#         print(f"{name} 포켓몬스터 생성")
#     def attack(self, target):
#         print(f'{self.name}이(가) {target.name}을(를) 공격했다...! 효과는 대단했다.')
#
# charizard = Poketmon("리자몽")
# pikachu = Poketmon("피카츄")
# squirtle = Poketmon("꼬부기")
# charizard.attack(squirtle)
# print(pikachu) #객체 주소가 나옴
# print(pikachu.name)
# print(squirtle.name)

## 상속 부모 클래스 자식 클래스
# class Pokemon:
#     def __init__(self, name):
#         self.name = name
#     def attack(self, target):
#         print(f'{self.name}이(가) {target.name}을(를) 공격했다.')
#
# class Pikachu(Pokemon):
#     def __init__(self, name, type):
#         super().__init__(name)
#         self.type = type
#     def attack(self, target):
#         print(f'{self.name}이(가) {target.name}에게 {self.type}공격! 효과는 대단했다.')
#     def electric_info(self):
#         print(f'{self.name}은(는) {self.type} 계열의 공격을 합니다.')
#
# class Squirtle(Pokemon):
#     pass
#
# class Agumon:
#     pass
#
# p1 = Pikachu("피카츄", "전기")
# p2 = Squirtle("꼬부기")
# p1.electric_info()
# p1.attack(p2)
# p2.attack(p1)
# print(p1.name, p1.type)
# print(issubclass(Pikachu,Pokemon))
# print(issubclass(Agumon,Pokemon))

# class Animal :
#     def says(self):
#         return 'I speak!'
#
# class Horse(Animal):
#     def says(self):
#         return 'Neigh!'
# class Donkey(Animal):
#     def says(self):
#         return 'Hee-haw!'
# class Mule(Donkey, Horse):
#     pass
# class Hinny(Horse, Donkey):
#     def says(self):
#         return 'Hinini'
#     # pass
#
# m1 = Mule()
# h1 = Hinny()
# print(m1.says(), h1.says())
# print(Hinny.__mro__)

class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 비행합니다."
class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영합니다."
class Pokemon:
    def __init__(self, name):
        self.__name = name

    def attck(self):
        print("공격~")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # name = property(get_name, set_name)


class Charizard(Pokemon,FlyingMixin):
    pass
class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
# print(c1.fly())
# print(g1.swim())
# c1.attck()
# Charizard.attck(c1) # 위와 같음, (c1) : 클래스중 어떤 속성이 실행하는지

# 프로퍼티
# g1.name = "잉어킹"
print(g1.name)
# print(g1.__name)
print(g1._Pokemon__name)

# print(g1.get_name())
# g1.set_name("잉어킹")
# print(g1.get_name())

#히든네임을 생성하는 이유는 외부에서 직접 접근하지 못하도록 하기 위해
