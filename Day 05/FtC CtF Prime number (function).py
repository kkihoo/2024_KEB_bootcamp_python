def isprime(n) -> bool: # 화살표는 함수 리턴값의 주석 역할
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1
        return True
# help(isprime)
# print(isprime.__doc__)

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
        if isprime(number):
            print(f'{number} is NOT prime number!')
        else:
            print(f'{number} is prime number')

    elif menu == '4':
        numbers = input("Input number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if isprime(number):
                print(number, end= ' ')
        print()

    elif menu == '5':
        print('Terminate Program.')
        break
    else:
        print("Not valid number, Please Enter 1 to 5")