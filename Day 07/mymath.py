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
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

def