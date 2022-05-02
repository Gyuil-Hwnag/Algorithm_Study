# 주사위 게임
# 1 ~ 6 까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는게임이 있다.
# 규칙 1. 같은눈이 3개가 나오면 10,000+(같은 눈)*1,000원의 상금
# 규칙 2. 같은눈이 2개 나오면 1,000+(같은 눈)*100원의 상금
# 규칙 3. 모두 다른 눈이 나오면 (그 중 가장 큰눈)*100원의 상금
# 예를 들어 3개의 눈 3,3,6이 나오면 상금은 1,000+(3*100) = 1,300
# 3개의 눈 2,2,2이 나오면 10,000+(2*1,000) = 12,000원
# 3개의 눈 6,2,5이 나오면 (6*100) = 600원
# N 명이 주사위 게임에 참여할 때 가장 많은 상금을 받는 사람의 상금을 출력하는 프로그램

# 내풀이
n = int(input())

def price(a, b, c):
    if a == b and b == c:
        return a*1000+10000
    elif a == b or a == c:
        return a*100+1000
    elif b ==c:
        return b*100+1000
    else:
        return max(a,b,c)*100

result = list()
for i in range(n):
    num = input().split()
    a,b,c = map(int, num)
    result.append(price(a,b,c))

print(max(result))

# 해설
n = int(input())
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b ,c = map(int, tmp)
