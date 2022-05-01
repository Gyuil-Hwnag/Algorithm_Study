# 뒤집은 소수
# N 개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램
# 예를들어 32를 뒤집으면 23이고 23은 소수이다. 그러면 23을 출력한다.
# 단 910을 뒤집으면 19로 숫자화 해야 한다.
# 첫 자리부터의 연속된 0은 무시한다.
# 뒤집는 한수인 def reverse(x), 소수인지 확인하는 def isPrime(x)를 반드시 작성

# 내 풀이
from typing import Tuple


num = list(map(int, input().split()))

def reverse(x):
    re = list()
    while x > 1:
        re.append(x%10)
        x = int(x/10)
    re.reverse()

    result = 0
    count = 1
    for i in re:
        result += i*count
        count = count*10

    return result

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x//2+1):
        if x%i == 0:
            return False

    return True

solve = list()
for i in num:
    a = reverse(i)
    if isPrime(a):
        solve.append(a)
    
for i in solve:
    print(i ,end=' ')
print()

# 해설
# n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10+t
        x = x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else: 
        return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')