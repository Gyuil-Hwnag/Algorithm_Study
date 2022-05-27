# 휴가(삼성 SW역량 평가 기출문제 : DFS 활용)

# 카운셀러로 일하고 있는 현수는 오늘부터 N+1 일 째 되는날 휴가를 가기 위해서, 
# 남은 N일 동안 최대한 많은 상담을 해서 휴가비를 넉넉히 만들어 휴가를 떠나려 한다.
# 현수가 다니는 회사에 하루에 하나씩 서로 다른 사람의 상담이 예약되어 있다.
# 각각의 상담은 상담을 완료하는데 걸리는 날수 T 와 상담을 했을 때 받을 수 있는 금액 P 로 이루어져 있다.
# 만약 N = 7 이고, 아래와 같이 예약이 잡혀있다면
#     1   2   3   4   5   6   7
# T   4   2   3   3   2   2   1
# P   20  10  15  20  30  20  10
# 1일에 잡혀있는 상담은 총 4일이 걸리며, 상담했을 때 받을 수 있는 금액은 20이다. 
# 만약 1일에 예약된 상담을 하면 4일 까지는 상담을 할 수가 없다.
# 하나의 상담이 하루를 넘어가는 경우가 많기 때문에 현수는 예약된 모든 상담을 혼자 할 수 없어 최대 이익이 나는 상담 스케줄을 짜기로 한다.
# 휴가를 떠나기 전에 할 수 있는 상담의 최대 이익은 1일, 5일, 7일에 있는 상담을 하는 것이며, 이 때의 이익은 20 + 30 + 10 = 60 이다.
# 현수가 휴가를 가기 위해 얻을 수 있는 최대 수익을 구하는 프로그램

# 입력설명
# 첫째줄에 N 이 주어진다.
# 둘째줄 부터 1부터 N일 까지 순서대로 주어진다.
# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10

# 출력설명
# 첫째줄에 현수가 얻을 수 있는 최대 이익을 출력
# 60

# 내풀이
n = int(input())
work = list()

for i in range(n):
    d, p = map(int, input().split())
    work.append([d,p])

max = 0
def DFS(d, sum):
    global max
    if d > n:
        return
    if d == n:
        if sum > max:
            max = sum
    else:
        DFS(d+1, sum)
        DFS(d+work[d][0], sum+work[d][1])

DFS(0, 0)
print(max)

# 해설
def DFS(L, sum):
    global res
    if L==n+1:
        if sum > res:
            res = sum
    else:
        if L+T[L] <= n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n=int(input())
    T=list()
    P=list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -21470000
    T.insert(0,0)
    P.insert(0,0)
    DFS(1,0)
    print(res)