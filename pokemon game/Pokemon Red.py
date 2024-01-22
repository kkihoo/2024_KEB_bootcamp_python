class Pokemon:
    def __init__(self, name, hp, offense, defense):
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense
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
