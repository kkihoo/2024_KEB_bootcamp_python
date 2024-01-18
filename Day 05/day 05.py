# Dictionary comprehensions

# player = 'Lionel Messi'
# count_alphabet = {letter: player.count(letter) for letter in player}
# print(count_alphabet)

# player = 'Minjae Kim'
# count_alphabet = dict()
# for letter in player :
#     count_alphabet[letter] = player.count(letter)
# print(count_alphabet)

#set
#연산자
# a = {1, 2}
# b = {2, 3}
# print(a & b) # 교집합 or a.intersection(b)
# print(a | b) # 합집합 or a.union(b)
# print(a - b) # 차집합 or a.difference(b)
# print(a ^ b) # 대칭 차집합 or a.symmetric_difference(b)
# print(a <= b) # 부분집합 or a.issubset(b)
# print(a >= b) # 상위집합 or a.issuperset(b)

# frozenset() 수정이 불가능한 객체
# fs = frozenset([5,1,2])
# print(fs)
# fs.add(4) # 추가 안됨 에러 뜸

## 함수
# def squares(*n)->list:
#     """
#     넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
#     :param n: tuple
#     :return: list
#     """
#     return [pow(i, 2) for i in n]
#     # return n*n
#
# def run_function(f, *number):
#     return f(*number)
#
# print(squares(7,5,2,6,3))
# print(run_function(squares, 9,10))

# numbers = ['7', '-11', '3']
# hap = 0
# for number in numbers :
#     hap = hap +int(number)
# print(hap)
#
# numbers = ['7', '-11', '3'] # map 함수
# print(sum(map(int, numbers)))

# lambda 함수
# def squares(n):
#     return n * n
even_numbers = [i for i in range(51) if i % 2 == 0]
print(even_numbers)
# print(tuple(map(squares, even_numbers)))
print(tuple(map(lambda x : x**2, even_numbers)))
# 또는
z = lambda x :pow(x,2)
print(tuple(map(z, even_numbers)))