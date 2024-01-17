# numbers = input("Input number : ").split()
# n1 = int(numbers[0])
# n2 = int(numbers[1])
# if n1 > n2 :
#     n1, n2 = n2, n1
#
# for number in range(n1, n2+1):
#     is_prime = True
#
#     if number < 2:
#         pass
#     else: #for 문에서 while 문으로 변경
#         i = 2
#         while i*i <= number: # i 에서 i*i로 반복문의 횟수를 압도적으로 줄임
#             if number % i == 0:
#                 is_prime = False
#                 break
#             i = i + 1
#         if is_prime:
#             pass
#             print(number, end = ' ')
###while i * i <= number 를 사용하면 효율을 높일 수 있습니다.
# while i <= number 의 경우, i 의 최대값은 number 입니다. 따라서, 이 반복문은 number 가 제곱근이 1 이하인 경우에도 i 가 number 까지 반복하게 됩니다.
# while i * i <= number 의 경우, i 의 최대값은 number 의 제곱근입니다. 따라서, 이 반복문은 number 가 제곱근이 1 이하인 경우에도 i 가 number 의 제곱근까지만 반복하게 됩니다.
# 소수의 경우, 제곱근보다 큰 약수가 존재하지 않습니다. 따라서, i 가 number 의 제곱근까지만 반복하면 소수를 찾는 데 필요한 모든 약수를 검사할 수 있습니다.


# ## Tuple
# t1 = (5)
# t2 = 5,
# t3 = (5,)
# t4 = (5, 7)
# t5 = 5, 7
# print(type(t1), type(t2), type(t3), type(t4), type(t5)) #하나일 경우 int로 취급 반점이 있고 두개 이상일 경우 튜플이 됨  #꼭 소괄호가 필요한게 아니다!
# t6 = "python", "Kim" # packing
# print(type(t6), t6[1])
# subject, prof = t6 # unpacking
# print(prof, subject)
# t7 = ()
# t8 = tuple()
# print(type(t7), type(t8), type(9,), type((9,)))
# t9 = 1, 2, 3
# t10 = 1, 2
# print(t9 == t10)
# print(t9 >= t10)
# print(t9 > t10) # 튜플간의 비교연산이 가능
# t11 = 4.43,
# t12 = 3.97, 4.1, 3.2
# print(t11 + t12)
# print(id(t11), t11)
# t11 = t11 + t12
# print(id(t11), t11)


##List
# subjects = ["C++", "JAVA", "Python"]
# # subjects = subjects[::-1]
# subjects.reverse() # 위와 같이 자체의 값의 순서를 거꾸로 바꿔줌
# print(subjects)
# subjects.append("Database") # insert보다 append를 쓰는것을 추천!
# print(subjects)
# subjects.insert(5,"R") #위치와 뭘 넣을지
# print(subjects)
# others = ["Swift", "C"]
# subjects.extend(others) # 다른 list를 합칠수 있음
# print(subjects)
# #slice
# numbers = [1,2,3,4]
# numbers[1:3] = [8, 9] #1번과 2번을 8,9로 대체
# print(numbers)
# #delete
# del subjects[0]
# print(subjects)
# subjects.remove("C")
# print(subjects)
# subjects.pop() #맨 뒤에 있는 것을 삭제
# print(subjects)
# subjects.pop(0) #숫자를 넣으면 del 과 같은 기능
# print(subjects)
# subjects.clear() #싹 다 삭제
# print(subjects)
# #index
# subjects = ["C++", "데이터베이스", "리눅스" ,"Swift", "5" ,"HTML", "JAVA", "9" ,"Python"]
# print(subjects.index('Python'))
# # subjects.sort() # sort(reverse=True)는 거꾸로 , (숫자 영어 한글 순)
# copy_subjects = sorted(subjects)
# print(subjects, copy_subjects)
# #copy
# # subjects = ["a", "b", "c"]
# subjects = ["a", ["b", "c"], "d"]
# a = subjects
# b = subjects.copy()
# c = list(subjects)
# d = subjects[:]
# print(subjects, a, b, c, d)
# # subjects[1] = "x" Shallow copy
# # print(subjects, a, b ,c ,d)
# e = copy.deepcopy(a) # deep copy는 요소가 변형이 와도 반영하지않음/ 같은 값을 가진 다를 객체라 보면됨
# subjects[1][1] = "x" # 요소가 변형 객체이면 변형 객체의 특성을 그대로 가져옴
# print(subjects, a, b ,c ,d,e)
# #zip()
# eng =  "Monday", "Tuesday", "Wendnesday"
# kor = "월요일", "화요일", "수요일"
# print(list(zip(eng, kor)))
# print(dict(zip(eng, kor)))
#for문 리스트작성
# squares = list()
# for i in range(1,6 ,1):
#     squares.append((i*i))
# print(squares)
# #list comprehension
# squares = [i*i for i in range(1,6,1)]
# print(squares)
# even_squares = [i*i for i in range(1,6,1) if i % 2 ==0]
# print(even_squares)


# Dictionary {} dict()
# sugang = dict(python="kim", db="kang", cpp="sung")
# print(sugang)
# sugang['datastructure'] = 'kim' #add
# print(sugang)
# sugang['datastructure'] = 'park' #update
# print(sugang)
# print(sugang['db'])
# print(sugang.get('db')) #키의 값 리턴
# print(sugang.get('opensource'))
# print(sugang.get('opensource', 'not exist'))
# for subject, professor in sugang.items():
#     print(f'{subject} 과목 담당교수는 {professor}입니다.')
# for k in sugang.keys():
#     print(k)
# for v in sugang.values():
#     print(v)
# for s in sugang.items():
#     print(s)

import random
drinks_food = {"위스키" : "초콜릿", "와인" : "치즈", "소주" : "삼겹살", "고량주" : "양꼬치"}


# del drinks_food["위스키"]
# drinks_food["사케"] = "광어회"
japan_drinks_food = {"사케":"광어회", "위스키":"아이스크림"}
drinks_food.update(japan_drinks_food)
# drink = input(drinks_food.keys())
drinks_food_keys = list(drinks_food)

print(drinks_food)
print(drinks_food.pop("고량주"))
print(drinks_food) #.pop()은 벨류값을 리턴후 삭제 .remove()는 리턴해주지 않고 삭제
print(drinks_food_keys)

while True:
    drink = input(f'다음 술 중에 고르세요.\n1) {drinks_food_keys[0]} 2) {drinks_food_keys[1]} 3) {drinks_food_keys[2]} 4) {drinks_food_keys[3]} 5) {drinks_food_keys[4]} 6) 아무거나 추천 7) 종료\n 입력 : ')
    if drink == '1':
        print(f'추천 안주는 {drinks_food[drinks_food_keys[0]]} 입니다.')
    elif drink == '2':
        print(f'추천 안주는 {drinks_food[drinks_food_keys[1]]} 입니다.')
    elif drink == '3':
        print(f'추천 안주는 {drinks_food[drinks_food_keys[2]]} 입니다.')
    elif drink == '4':
        print(f'추천 안주는 {drinks_food[drinks_food_keys[3]]} 입니다.')
    elif drink == '5':
        print(f'추천 안주는 {drinks_food[drinks_food_keys[4]]} 입니다.')
    elif drink == '6':
        random_drink = random.choice(drinks_food_keys)
        print(f'술은 {random_drink}이고, 추천 안주는 {drinks_food[random_drink]} 입니다.')
    elif drink == '7':
        print(f'다음에 또 오세요~')
        break
    else:
        print('올바른 값을 선택해주세요.')

## {**a,**b} shallow copy
# first = {'a':'apple' , 'b':'blue'}
# second = {'b':'bike', 'c':'copy'}
# print({**first, **second})
# third = {'d' : 'donuts'}
# print({**first, **third, **second})
