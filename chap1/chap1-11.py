# 함수 만들기

def add(a, b):
    return a+b

print(add(5,10))

# 튜플로 반환
def add(a,b):
    c = a+b
    d = a-b
    return c,d

print(add(20, 11))



def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]
for i in a:
    if isPrime(i):
        print(i, end=' ')
print()