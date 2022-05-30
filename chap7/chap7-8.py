# 사과나무(BFS)

# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어져 있다. N의 크기는 항상 홀수이다.
# 가을이 되어 사과를 수확해야 하는데 현수는 격자판의 사과를 수확할 때 다이아몬드 모양의 격자판만을 수확하고 
# 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
# 만약 N이 5이면 아래그림과 같이 진한 부분의 사과를 수확한다.
# 10    13     10()   12    15
# 12    39()   30()   23()  11
# 11()  25()   50()   53()  15()
# 19    27()   29()   37()  27
# 19    13     30()   13    19
# 현수가 수확하는 사과의 총 개수를 출력

# 입력설명
# 첫째줄에 자연수 N(홀수)가 주어진다.
# 두번째 줄부터 N줄에 걸쳐 N개의 자연수가 주어진다. 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
# 각 격자안의 사과의 개수는 100을 넘지 않는다.
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# 출력설명
# 수확한 사과의 총 개수를 출력
# 379

# 내풀이
from collections import deque
n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
print(apple)
L = n//2
sum = 0
while True:
    if L<0:
        break
    for i in range(-L, L+1):
        sum += apple[L][n//2-i]
        ch[L][n//2-i] = 1
        if L != n//2:
            sum += apple[n-L-1][n//2-i]
            ch[n-L-1][n//2-i] = 1
    L -= 1
print(ch)
print(sum)

# 해설
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
sum = 0
Q = deque()
ch[n//2][n//2] = 1
sum+=a[n//2][n//2]
Q.append((n//2, n//2))
L = 0
while True:
    if L==n//2:
        break
    size=len(Q)
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x,y))
    L+=1
print(sum)