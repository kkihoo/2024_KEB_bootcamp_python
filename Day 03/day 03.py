#문자열, 줄바꿈
# print('give', "us\n", '''some''', """space""")

#raw string
# university = r"Inha\nUniversity!"
# print(university) #줄바꿈이 아닌 쓴 그대로 보여줌

#Duplicate with *
# start = 'Na' *4 + '\n'
# middle = 'Hey' *3 + '\n'
# end = 'Goodbye.'
# print(start + start + middle + end) #문자열과 *는 함께 사용이 가능하다.

#역방향 인덱싱
# letters = 'abcdefghijklmnopqrstuvwxyz'
# print(letters[-1])

#replace 함수
# name = "Henny"
# print(name.replace('H','P'))
# print('P' + name[1:]) #name[1:]은 0번 뒤인 1번부터 다 불러온다.

#슬라이스
# university = "Inha\nUniversity!"
# print(university[:4])
# print(university[:-12])
# print(len(university)) #몇글자인지
# print(university[0:len(university)]) # =(university[0:16])
# print(university[5:]) #5번부터 끝까지
# print(university[:16])#0번부터 16번까지
# print(university[::2]) #두칸씩 비우고 나타내줌
# print(university[0:16:3])#0부터 16번까지 3칸씩 띄워서 나타냄

# split()
# course = "2024 KEB Bootcamp"
# print(course.split())
# print(course.split('B'))

# numbers = input("FirstNumber SecondNumber : ").split() #input은 기본적으로 문자열을 출력함
# print(numbers[0] + numbers[1]) #concatenation 연속
# print(int(numbers[0]) + int(numbers[1])) # arithmetic operation 산술연산

# join()
# subjects = ["Python", "C++", "Database"]
# subjects_string = "/".join(subjects)
# print(subjects_string) #리스트에 있던 요소들이 /를 포함에서 한줄로 나타남


# 문자열 replace
# # course = "2024 KEB Bootcamp"
# # print(course.replace('KEB', 'Inha')) #replace를 썼을때 잠시만 바뀜
# # print(course)
# # course = course.replace('KEB', 'Inha') #할당해주면 바꾸기 가능
# # print(course)
#
# course = "KEB 2024 KEB Bootcamp"
# course = course.replace('KEB', 'Inha', 1) # .replace(바꿀 대상, 바뀔 문자, 몇개를 바꿀지)
# print(course)

# strip() 문자열과 공백을 제거
# blurt = "What the...!!?"
# print(blurt.strip('.?!')) # .?!를 없애고 나타냄

# url = 'https://www.daum.net'
# print(url.strip('https://')) # 뒤에 t까지 지워버림
# print(url.lstrip('https://')) # lstrip은 선행문자 하나만 지움
# print(url.rstrip('.net')) # rstrip은 후행문자만 지움

#특정문자 찾기
# course = "* KEB 2024# KEB! Bootcamp?."
# print(course.find('KEB')) # KEB가 몇번째에 있는지 세주는 함수
# print(course.rfind("KEB")) # 뒤에서부터 찾는 문자가 몇번째에 있는지
# print(course.startswith('KEB')) # 제일 앞에 있는 문자가 맞고 틀리는지 알려주는 함수
# print(course.endswith('.')) # 끝나는 문자가 맞는지 확인
# print(course.find('Inha')) # 찾는 문자가 없을때 -1를 출력
# print(course.index('Inha')) #ValueError: substring not found 에러가 뜸

# preview
# subjects = "python c++ database linux"
# print(subjects.isalnum()) # 영어, 한글 또는 숫자만 있을경우 True, 아니면 False ++때문에 False

# case 바꾸기
# setup = "a duck gose into a bar..."
# print(setup.capitalize()) # 맨 앞글자만 대문자로 바꿈
# print(setup.title()) # 각 단어마다 앞글자는 대문자로 변경
# print(setup.upper()) #모든 글 대문자로 변경
# print(setup.lower()) # 모든 문자 소문자로 변경

# %s %d %f (string, decimal, float)
# thing = 'woodchuck'
# print('%+12s' %thing) # 오른쪽 정렬
#
# thing = 91.58
# print('%+3f' %thing)

# Dictionary형 format
# subjects = {'python' : 'Kim', 'c++' : 'Sung', 'datastructure': 'Kim', 'database' : 'Kang' }
# print("{0[c++]} {0[datastructure]}".format(subjects))

#while문으로 소수 판독기 만들
# num = int(input("Input number : "))
# cnt = 0
# i = 1
# while i <= num :
#     if num % i == 0 :
#         cnt = cnt + 1
#     i = i + 1
# if cnt == 2:
#     print(f'{num} is prime number')
# else :
#     print(f'{num} is NOT prime number')


# prime number
# number = int(input("Input number : "))
# is_prime = True
#
# if number < 2:
#     print(f'{number} is NOT prime number!')
# else:
#     i = 2
#     while i < number:
#         if number % i == 0:
#             is_prime = False
#             break
#         i = i + 1
#
#     if is_prime:
#         print(f'{number} is prime number')
#     else:
#         print(f'{number} is NOT prime number!')

univ = 'inha'
i = 0
while i < len(univ):
    print(univ[i], end = ' ')
    i = i + 1

print()

for letter in univ :
    print(letter, end = ' ')

print()

for k in range(len(univ)): # 1은 1씩 증가한다는 뜻 2나 3같은 다른 수로 변경 가능 대부분 1은 생략 , 시작값도 0이 기본
    print(univ[k], end = ' ')

