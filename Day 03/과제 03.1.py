while True :
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit 3) Prime number checker 4) Prime number interval checker 5) Quit program : ")
    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit:.2f}F, Celsius : {(fahrenheit - 32) * 5 / 9:.2f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius:.2f}C, Fahrenheit : {(celsius*9.0/5.0)+32.0:.2f}F')
    elif menu == '3':
        number = int(input("Input number : "))
        is_prime = True

        if number < 2:
            print(f'{number} is NOT prime number!')
        else:
            i = 2
            while i < number:
                if number % i == 0:
                    is_prime = False
                    break
                i = i + 1

            if is_prime:
                print(f'{number} is prime number')
            else:
                print(f'{number} is NOT prime number!')

    elif menu == '4':
        numbers = input("Input number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                pass
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime: print(number, end=' ')
        print()
    elif menu == '5':
        print('Terminate Program.')
        break
    else:
        print("Not valid number, Please Enter 1 to 5")


### 과제 문제점 알아보기 :
# 중복 코드가 존재한다 -> 차후 함수, 모듈을 통해 해결
# 4번 숫자를 하나만 입력했을 때 에러가 나면서 종료
# 코드 간소화 해야함
# 소수판독기에서 숫자가 커질 경우 그 앞에 숫자까지 끊임없이 돌아가서 돌리기 힘들어진다.(최적화 문제)
