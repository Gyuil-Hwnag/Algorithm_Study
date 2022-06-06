# 단지 번호 붙히기(DFS, BFS)

# 그림1과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# 그림2는 그림1을 단지별로 번호를 붙인것이다. 지도를 입력하여 단지수를 출력하고, 
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램
# 그림1        그림2
# 0110100     0110200
# 0110101     0110202
# 1110101     1110202
# 0000111     0000222
# 0100000     0300000
# 0111110     0333330
# 0111000     0333000

# 입력설명
# 첫번째줄에는 지도의 크기 N이 입력되고 그 다음줄 N에는 각각 N개의 자료(0, 1)이 입력된다.
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 출력설명
# 첫번째 줄에는 총 단지수를 출력한다. 그리고 각 단지내 집의수를 오름차순으로 정렬하여 한줄에 하나씩 출력한다.
# 3
# 7
# 8
# 9

# 내풀이
n = int(input())
apartlist = [list(map(int, input())) for _ in range(n)]
res = list()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def DFS(x, y):
    global cnt
    cnt += 1
    apartlist[x][y] = 0
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and apartlist[xx][yy]==1:
            DFS(xx, yy)

for i in range(n):
    for j in range(n):
        if apartlist[i][j] == 1:
            cnt = 0
            DFS(i, j)
            res.append(cnt)
res.sort()
print(len(res))
for i in res:
    print(i)


# 해설(BFS)
from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
board=[list(map(int, input())) for _ in range(n)]
cnt=0
res=[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            cnt=1
            while Q:
                tmp=Q.popleft()
                for k in range(4):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y]==0:
                        continue
                    board[x][y]=0
                    Q.append((x, y))
                    cnt+=1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)

