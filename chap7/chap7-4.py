# 동전 바꿔주기(DFS)

# 명보네 동네 가게의 현금 출납기에는 K 가지 동전이 각각 n1, n2, n3, ... , nk개씩 들어있다.
# 가게 주인은 명보에게 T원의 지폐를 동전으로 바꿔주려고 한다. 이때, 동전 교환 방법은 여러가지가 있을 수 있다.
# 예를 들어 10원, 5원, 1원 짜리 동전이 각각 2, 3, 5개씩 있을 때, 20원짜리 지폐를 다음과 같은 4가지 방법으로 교환이 가능하다.
# 20 = 10*2
# 20 = 10*1 + 5*2
# 20 = 10*1 + 5*1 + 1*5
# 20 = 5*3 + 1*5
# 입력으로 지폐의 금액 T, 동전의 가지수 K, 각 동전 하나의 금액 Pi와 개수 ni가 주어질 때
# 지폐를 동전으로 교환하는 방법의 가지수를 계산하는 프로그램을 작성

# 입력설명
# 첫쨰줄에는 지폐의 금액 T, 둘째줄에는 동전의 가지수 K, 셋째줄부터 마지막줄 까지는 각 줄에 동전의 금액 Pi, 개수 ni가 주어진다.
# 20
# 3
# 5 3
# 10 2
# 1 5

# 출력설명
# 첫번째 줄에 동전 교환 방법의 가지수를 출력
# 4

# 내풀이
from numpy import intp


t = int(input())
k = int(input())

coin = list()
for i in range(k):
    n, c = map(int, input().split())
    coin.append([n,c])

res = 0
def DFS(L, sum):
    global res
    if sum > t:
        return
    if L == k:
        if sum == t:
            res+=1
    else:
        for i in range(coin[L][1]+1):
            DFS(L+1, sum+(coin[L][0]*i))

DFS(0, 0)
print(res)

# 해설

def DFS(L, sum):
    global cnt
    if T < sum:
        return
    if L==k:
        if sum==T:
            cnt+=1
    else:
         for i in range(cn[L]+1):
             DFS(L+1, sum+(cv[L]*i))

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)