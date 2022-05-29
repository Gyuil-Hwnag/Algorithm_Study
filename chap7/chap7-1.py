# 최대점수 구하기(DFS)
# 이번 정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 풀려고 한다.
# 각 문제는 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어진다. 제한시간 M안에 N개의 문제중 최대점수를 얻을 수 있도록 해야 한다.
# (해당문제는 해당시간이 걸리면 푸는 걸로 간주한다. 한 유형당 한개만 풀 수 있다.)

# 입력설명
# 첫번쨰 줄에 문제의 개수 N, 제한시간 M 이 주어진다.
# 두번째 줄부터 N 줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어진다.
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4

# 출력설명
# 첫번째 줄에 제한시간안에 얻을 수 있는 최대 점수를 출력
# 41

# 내풀이
n, m = map(int, input().split())

num = list()
for i in range(n):
    s, c = map(int, input().split())
    num.append([s,c])

solve = list()
max = 0
def DFS(v, time):
    global max
    if time > m or v > n:
        if v > n and time < m:
            score = 0
            for i in range(len(solve)):
                score += solve[i][0]
            if score > max:
                print(solve)
                max = score
        else:
            score = 0
            for i in range(len(solve)-1):
                score += solve[i][0]
            if score > max:
                print(solve)
                max = score
    else:
        for i in range(v, n):
            solve.append(num[i])
            DFS(v+1, time+num[i][1])
            solve.pop()
            DFS(v+1, time)

DFS(0, 0)
print(max)

# 해설
def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

if  __name__ == "__main__":
    n,m = map(int, input().split())
    pv=list()
    pt=list()
    for i in range(n):
        a,b=map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -21470000
    DFS(0,0,0)
    print(res)

