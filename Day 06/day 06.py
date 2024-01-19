# 재귀 함수
# def factorial_repetition(n) -> int:
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result
#
# def factorial_recursion(n):
#
#     if n == 1 :
#         return n
#     else:
#         return n * factorial_recursion(n-1)
#
# number = int(input("number : "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))

# #예외처리
# import random
#
# class OopsException(Exception):
#     pass
#
#
# numbers = [random.randint(1,100) for i in range(5)]
# print(numbers)
#
# try :
#     pick = int(input(f'Input index (0 ~ {len(numbers)-1}) : '))
#     print(numbers[pick])
#     print(5/2)
#     raise OopsException("Oops~") #강제로 에러 걸기
# except IndexError as err :# 먼저 디테일한 에러들을 처리해줌
#     print(f"Out of range : Wrong index number\n{err}")
# except ValueError as err : # as 'name' 하고 출력에 넣으면 에러뜬 이유를 텍스트로 보여줌
#     print(f"Input only Number!\n{err}")
# except ZeroDivisionError as err : #print(5/0)에 대한 예외처리
#     print(f'The denominator cannot be 0.\n{err}')
# except OopsException as err :
#     print(f'Oops Oops {err}')
# except Exception as err: # 보험식으로 맨 밑으로 가는것이 문법적으로 옳다
#     print(f"Error occurs\n{err}")
# else :
#     print(f'Program terminate')

#
def desc(f):
    def wrapper():
        print("study")
        f()
    # print("a")
    return wrapper

def something():
    print("do something")

s = desc(something)
s()