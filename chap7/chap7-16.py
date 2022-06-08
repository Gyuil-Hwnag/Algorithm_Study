# 사다리 타기(DFS)

# 현수와 친구들은 과자를 사먹기 위해 사다리 타기를 합니다. 사다리 표현은 2차원 평면은 0으로 채워지고, 사다리는 1로 표현한다.
# 현수는 특정 도착지점으로 도착하기 위해서는 몇 번째 열에서 출발해야 하는지 알고 싶습니다. 특정 도착지점은 2로 표기된다.
# 사다리 지도가 10*10이면
# 0 1 2 3 4 5 6 7 8 9
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1   1 1 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 1 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 1 1 0 1
# 1 0 1 0 0 2 0 1 0 1
# 특정 목적지인 2에 도착하려면 7번 열 출발지에서 출발하면 된다.

# 입력설명
# 10*10 사다리 지도가 주어진다.
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 1 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 1 1 0 1
# 1 0 1 0 0 2 0 1 0 1

# 출력설명
# 출발지 열 번호를 출력
# 7

# 내풀이
board =[list(map(int, input().split())) for _ in range(10)]
start = 0
for i in range(10):
    if board[9][i] == 2:
        start = i
dx = [0, 0, -1]
dy = [-1, 1, 0]
def DFS(i, j):
    if i==0:
        print(j)
        return
    for k in range(3):
        xx = i+dx[k]
        yy = j+dy[k]
        if 0<=xx<=9 and 0<=yy<=9 and board[xx][yy]==1:
            board[xx][yy]=0
            DFS(xx, yy)
            break

DFS(9, start)

# 해설
def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)

if __name__=="__main__":
    board =[list(map(int, input().split())) for _ in range(10)]
    ch=[[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y]==2:
            DFS(9, y)