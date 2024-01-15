#while 반복문
while True :
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit  3) Quit program : ")
    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit:.2f}F, Celsius : {(fahrenheit - 32) * 5 / 9:.2f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius:.2f}C, Fahrenheit : {(celsius*9.0/5.0)+32.0:.2f}F')
    elif menu == '3':
        print('Terminate Program.')
        break
    else:
        print("Not valid number, Please Enter 1, 2 or 3")

#for 반복문

for menu in range(100000):
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit  3) Quit program : ")
    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit:.2f}F, Celsius : {(fahrenheit - 32) * 5 / 9:.2f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius:.2f}C, Fahrenheit : {(celsius * 9.0 / 5.0) + 32.0:.2f}F')
    elif menu == '3':
        print('Terminate Program.')
        break
    else:
        print("Not valid number, Please Enter 1, 2 or 3")
