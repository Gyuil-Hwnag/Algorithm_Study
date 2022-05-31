# 미로의 최단거리 통로(DFS)

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
# 위의 지도에서 출발점에서 도착점까지 갈 수 있는 방법의 수는 8가지이다.

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
# 첫번쨰 줄에 경로의 가지수를 출력한다.
# 8

# 내풀이
miro = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y):
    global cnt
    global ch
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            nowX = x+dx[i]
            nowY = y+dy[i]
            if 0<=nowX<=6 and 0<=nowY<=6 and miro[nowX][nowY] == 0:
                miro[nowX][nowY] = 1
                DFS(nowX, nowY)
                miro[nowX][nowY] = 0

miro[0][0] = 1
DFS(0, 0)
print(cnt)

# 해설
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and miro[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0

if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0,0)
    print(cnt)
