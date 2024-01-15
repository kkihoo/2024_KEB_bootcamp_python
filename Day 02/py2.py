### 변수 (Variable)
#
# - a~z / A~Z
# - 0~9, _ 만 가능
# - 숫자가 아닌 문자나 언더바로 시작
# - 예약어(키워드)는 사용할 수 없음
# help("keyword") # 예약어 조회 가능

#기본함수
# base_number = int(input('Input base number : '))
# exponent_number = int(input('Input exponent number: '))
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')

#파워함수
# base_number = int(input('Input base number : '))
# exponent_number = int(input('Input exponent number: '))
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number,exponent_number)}')
#f' (에프스트링 f-string : 파이썬 3.6 이상부터 사용) : {}중괄호는 변수 또는 함수 [최신버젼]
#format function [전버젼]
# print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(base_number, exponent_number, pow(base_number,exponent_number)))
#c like[전전버젼]
# print('밑은 %d, 지수는 %d, 결과 값은 %d' %(base_number, exponent_number, base_number**exponent_number))


# first_number = int(input("First number : "))
# second_number = int(input("Second number : "))
# quotient = first_number // second_number
# remainder = first_number % second_number
# print(f'몫은 {quotient}, 나머지는 {remainder} 입니다.')
# print(f'몫은 {divmod(first_number, second_number)[0]}, 나머지는 {divmod(first_number,second_number)[1]} 입니다.')
# print(divmod(9,5)) 위처럼 몫과 나머지를 한번에 나타내주는 함수

# print(-5**2) # 25가 아니라 -25로 출력

#10진수, 8진수, 16진수, 2진수
# dec = 65
# octal = 0o101
# hexadecimal = 0x41
# binary = 0b01000001
# print(dec, octal, hexadecimal, binary)
# print(chr(binary)) #ascii코드
# print(chr(dec), chr(octal), chr(hexadecimal), chr(binary))
# print(bin(dec), bin(octal), bin(hexadecimal), bin(binary))
# print(ord('B'), ord('Z'), ord('a'), ord('2'))

#화씨에서 섭씨 바꿔보기
# fahrenheit = float(input('Input Fahrenheit : '))
# print(f'Fahrenheit : {fahrenheit}F, Celsius : {(fahrenheit - 32) * 5 / 9:.4f}C') #.4f 소수점 4번째 자리까지 나타내기
menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit  3) Quit program : ")

if menu == '1' :
    fahrenheit = float(input('Input Fahrenheit : '))
    print(f'Fahrenheit : {fahrenheit}F, Celsius : {(fahrenheit - 32) * 5 / 9:.2f}C')
elif menu == '2' :
    celsius = float(input('Input Celsius : '))
    print(f'Celsius : {celsius}C, Fahrenheit : {(celsius*9.0/5.0)+32.0:.2f}F')

#앞에 넣고 뒤에 몇진법을 10진수로 나타낼건지
# print(int('1F', 16))

# print(float(True)) #1.0
# print(float(False)) #0.0
# print(5 + 2.0) #정수와 소수형 섞어 사용 가능