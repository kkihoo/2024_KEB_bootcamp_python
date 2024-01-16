# 1
num = []  # 빈 리스트 생성

for i in range(3, -1, -1):
    num.append(i)  # append로 요소 추가
print(num)
#-----------------------------------

num = [i for i in range(3,-1,-1)]
print(num)
#-----------------------------------

# 2
guess_me = 7
number = 1

while True :
    if number < guess_me :
        print("too low", number)

    elif number == guess_me :
        print('found it!', number)
        break

    else:
        print("oops")
        break
    number = number + 1

#-----------------------------------
# 3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low", number)

    elif number == guess_me:
        print('found it!', number)
        break

    else:
        print("oops")
        break