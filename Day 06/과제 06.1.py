# 10.1 #클래스와 그 클래스의 출력값은 같은가?

class Thing:
    pass
example = Thing()
print(Thing)
print(example)
#같지 않다.

# 10.2

class Thing2:
    letters = 'abc'
print(Thing2.letters)

#10.3 클래스를 만들고 속성에 어떠한 값을 할당후 출력하기

class Thing3:
    def __init__(self):
        self.letters = 'xyz'

t = Thing3()
print(t.letters)

# 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
e = Element('Hydrogen', 'H', '1')
print(e.name)
# 10.5
el_dict = {'name' : 'Hydrogen','symbol' : 'H', 'number' : '1'}
e = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
e1 = Element(**el_dict) #딕셔너리로부터 직접 객체를 초기화
print(e1.symbol)

# 10.6
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(f'name : {self.name}, symbol : {self.symbol}, number : {self.number}')
e = Element(**el_dict)
e.dump()

# 10.7
print(e)
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        print(f'name : {self.name}, symbol : {self.symbol}, number : {self.number}')
e = Element(**el_dict)
e.dump()
