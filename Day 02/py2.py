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