import random
class Pokemon:
    def __init__(self, name, hp, offense, defense):
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense
class Red:
    def __init__(self,name):
        self.name = name
class Green:
    def __init__(self,name):
        self.name = name

class Grass:
    def grass(self):
        return f"{self.name}는 풀 속성 포켓몬 입니다."
class Water:
    def water(self):
        return f"{self.name}는 물 속성 포켓몬 입니다."
class Fire:
    def fire(self):
        return f"{self.name}는 불 속성 포켓몬 입니다."

class Bulbasaur(Pokemon, Grass):
    pass
class Charmander(Pokemon, Fire):
    pass
class Squirtle(Pokemon, Water):
    pass

b1 = Bulbasaur("이상해씨", 45, 49,49)
c1 = Charmander("파이리", 39, 52,43)
s1 = Squirtle("꼬부기", 44,48,65)

while True:
    pokemon_select = 0
    check = None
    pokemon_select = int(input("포켓몬을 골라주세요 1) 이상해씨 2) 파이리 3) 꼬부기 : "))
    if pokemon_select == 1 :
        check = int(input("이상해씨를 선택 하시겠습니까? 1) 예  2) 아니오 : "))
        if check == 1 :


