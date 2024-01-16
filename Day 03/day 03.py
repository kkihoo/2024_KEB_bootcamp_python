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
