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
def squares(*n)->list:
    """
    넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    """
    return [pow(i, 2) for i in n]
    # return n*n

def run_function(f, *number):
    return f(*number)

print(squares(7,5,2,6,3))
print(run_function(squares, 9,10))