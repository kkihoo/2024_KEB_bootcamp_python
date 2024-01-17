numbers = input("Input number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])
if n1 > n2 :
    n1, n2 = n2, n1

for number in range(n1, n2+1):
    is_prime = True

    if number < 2:
        pass
    else: #for 문에서 while 문으로 변경
        i = 2
        while i*i <= number: # i 에서 i*i로 반복문의 횟수를 압도적으로 줄임
            if number % i == 0:
                is_prime = False
                break
            i = i + 1
        if is_prime:
            pass
            print(number, end = ' ')
###while i * i <= number 를 사용하면 효율을 높일 수 있습니다.
# while i <= number 의 경우, i 의 최대값은 number 입니다. 따라서, 이 반복문은 number 가 제곱근이 1 이하인 경우에도 i 가 number 까지 반복하게 됩니다.
# while i * i <= number 의 경우, i 의 최대값은 number 의 제곱근입니다. 따라서, 이 반복문은 number 가 제곱근이 1 이하인 경우에도 i 가 number 의 제곱근까지만 반복하게 됩니다.
# 소수의 경우, 제곱근보다 큰 약수가 존재하지 않습니다. 따라서, i 가 number 의 제곱근까지만 반복하면 소수를 찾는 데 필요한 모든 약수를 검사할 수 있습니다.

