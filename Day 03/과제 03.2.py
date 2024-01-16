# 1 for 문으로 리스트 [3,2,1,0]를 출력해보자
num = []  # 빈 리스트 생성

for i in range(3, -1, -1):
    num.append(i)  # append로 요소 추가
print(num)
#-----------------------------------

num = [i for i in range(3,-1,-1)]
print(num)
#-----------------------------------

# 2 guess_me 변수에 7을 할당하고, number 변수에 1을 할당한다. number와 guess_me를 비교하는 while 문을 작성해보자. number가 guess_me보다 작으면 'too low'를 출력한다.
# 같으면 'found it!'을 출력하고 반복문을 종료하고, 크면 'oops'를 출력하고 반복문을 종료한다. 반복문의 마지막에 number를 1씩 증가시킨다.
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
# 3 guess_me에 변수에 5를 할당하고, for 문을 사용하여 range(10)에서 number 변수를 사용한다. number가 guess_me보다 작으면 'too low' 를 출력
# 같으면 'found it!' 크면 'oops'를 출력하고 반복문을 종료한다.
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