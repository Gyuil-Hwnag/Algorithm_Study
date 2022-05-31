# 미로의 최단거리 통로(BFS 활용)

# 7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력하는 프로그램. 경로수는 출발점에서 도착점까지 가는데 이동한 횟수를 의미.
# 출발점은 (1,1) 좌표이고, 탈출 도착점은 (7,7)좌표이다. 격자판의 1은 벽이도, 0은 도로이다.
# 격자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면
# 출 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 도
# 위와 같은 경로가 최단 경로이며 경로수는 12이다.

# 입력설명
# 7*7 격자판의 정보가 주어진다.
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0

# 출력설명
# 첫번쨰 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1을 출력한다.

# 내풀이
from collections import deque
miro = list()
for i in range(7):
    num = map(int, input().split())
    miro.append(num)
ch=[[0]*7 for _ in range(7)]

dq = deque()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dq.append((0, 0))

while dq:
    now = dq.popleft()
    for i in range(4):
        x = now[0]+dx[i]
        y = now[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and miro[x][y] == 0:
            miro[x][y]=1
            ch[x][y] = ch[now[0]][now[1]]+1
            dq.append((x,y))
if ch[6][6] == 0:
    print(-1)
else:
    print(ch[6][6])


# 해설
dx = [-1, 0, 1, 0]
dy =  [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0,0))
board[0][0]=1
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0 <=x<= 6 and 0 <=y<= 6 and board[x][y] == 0:
            board[x][y]=1
            dis[x][y] = dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
