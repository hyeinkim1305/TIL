# def sum(a,b):
#     print(a-b)
#     print(a*b)
#     result = a+b
#     return result
# # sum(5,1)
# print(sum(5,1))


# # 모든 함수는 return을 만나면 종료되고 결과가 반환된다.
# def sum(a,b):
#     result = a+b
#     return result
#     print(a-b)
#     print(a*b)
# # sum(5,1)
# print(sum(5,1))   ### 여기서 결과값이 print는 안나와 . return만나서 끝남


# def mul(a,b):
#     return a*b

# print(mul(3,5)*2)


def is_even(n):
    if n % 2 == 1:
        result = False
    else:
        result = True
    return result       ### return 꼭 있어야 한다!

print(is_even(4))
print(is_even(7))