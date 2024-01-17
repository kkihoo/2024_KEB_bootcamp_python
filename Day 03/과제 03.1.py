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