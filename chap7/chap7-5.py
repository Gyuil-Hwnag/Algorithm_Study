# 동전 분배하기(DFS)

# N 개의 동전을 A, B, C 세명에게 나누어 주려고 한다. 세명에게 적절히 나누어 주어, 세명이 받은 각각의 총액을 계산해,
# 총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 한다.
# 단 세사람의 총액은 서로 달라야 한다.

# 입력설명
# 첫째줄에 동전의 개수 N 이 주어진다.
# 7
# 8
# 9
# 11
# 12
# 23
# 15
# 17

# 출력설명
# 총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력
# 5

# 내풀이
n = int(input())
coin = list()
for i in range(n):
    coin.append(int(input()))

a = list()
b = list()
c = list()

res = sum(coin)

def DFS(L):
    global res
    if L == n:
        if sum(a) == sum(b) or sum(b) == sum(c) or sum(a) == sum(c):
            return
        else:
            if res > (max(sum(a), sum(b), sum(c)) - min(sum(a), sum(b), sum(c))):
                res = max(sum(a), sum(b), sum(c)) - min(sum(a), sum(b), sum(c))
    else:
        a.append(coin[L])
        DFS(L+1)
        a.pop()
        
        b.append(coin[L])
        DFS(L+1)
        b.pop()

        c.append(coin[L])
        DFS(L+1)
        c.pop()

DFS(0)
print(res)

# 해설
def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]

if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0]*3
    res = 21470000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)