# 섬나라 아일랜드(BFS 활용)

# 섬나라 아일랜드의 지도가 격자판의 정보로 주어진다. 각 섬은 1로 표시되어 상하좌우와 대각선으로 연결되어 있으며, 0은 바다이다.
# 섬나라 아일랜드에 몇개의 섬이 있는지 구하는 프로그램
# 1100010
# 0110110
# 0100000
# 0001011
# 1101100
# 1000100
# 1010100

# 입력설명
# 첫째줄에 자연수 N이 주어진다.
# 둘째줄에 섬의 개수를 출력한다.
# 7
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0

# 출력설명
# 첫번째 줄에 섬의 개수를 출력한다.
# 5

# 내풀이
from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cnt = 0
res = list()
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            cnt = 1
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0]+dx[k]
                    y = tmp[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y]==0:
                        continue
                    board[x][y] = 0
                    Q.append((x, y))
                    cnt += 1
            res.append(cnt)

print(len(res))


# 해설
from collections import deque
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            while Q:
                tmp=Q.popleft()
                for k in range(8):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        board[x][y]=0
                        Q.append((x, y))
            cnt+=1
print(cnt)