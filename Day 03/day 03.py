#문자열, 줄바꿈
# print('give', "us\n", '''some''', """space""")

#raw string
# university = r"Inha\nUniversity!"
# print(university) #줄바꿈이 아닌 쓴 그대로 보여줌

#Duplicate with *
start = 'Na' *4 + '\n'
middle = 'Hey' *3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end) #문자열과 *는 함께 사용이 가능하다.