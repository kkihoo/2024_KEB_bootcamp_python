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
a = {1, 2}
b = {2, 3}
print(a & b) # 교집합 or a.intersection(b)
print(a | b) # 합집합 or a.union(b)
print(a - b) # 차집합 or a.difference(b)
print(a ^ b) # 대칭 차집합 or a.symmetric_difference(b)
print(a <= b) # 부분집합 or a.issubset(b)
print(a >= b) # 상위집합 or a.issuperset(b)

