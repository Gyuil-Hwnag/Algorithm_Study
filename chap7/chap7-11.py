# 등산경로(DFS)

# 등산을 매우 좋아하는 철수는 마을에 있는 뒷산에 등산경로를 만들 계획을 세우고 있다. 
# 마을 뒷산의 형태를 나타낸 지도는 N*N 구역으로 나눠져 있으며, 각 구역에는 높이가 함께 나타나 있다. 
# N=5 이면 아래와 같이 표현된다.
# 2   23  92  78  93
# 59  50  48  90  80
# 30  53  70  75  96
# 94  91  82  89  93
# 97  98  95  96  100
# 어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동할 수 있도록 등산로 설계.
# 등산로의 출발지는 전체 영역에서 가장 낮은 곳이고, 목적지는 가장 높은 곳이다. 출발지와 목적지는 유일하다.
# 지도가 주어지면 출발지에서 도착지로 갈 수 있는 등산경로가 몇가지 인지 구하는 프로그램

# 입력설명
# 첫번째 줄에 N이 주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.
# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100

# 출력설명
# 등산경로의 가지수를 출력한다.
# 5

# 내풀이
n = int(input())
mount = list()
mount = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
cnt = 0
start = 2147000
end = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if start > mount[i][j]:
            start = mount[i][j]
            startX = i
            startY = j
        if end < mount[i][j]:
            end = mount[i][j]

def DFS(x, y):
    global cnt
    if mount[x][y] == end:
        cnt+=1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<n and 0<=yy<n and mount[x][y] < mount[xx][yy]:
                DFS(xx, yy)

DFS(startX, startY)
print(cnt)

# 해설
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx = x+dx[k]
            yy = y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__ == "__main__":
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    max = -21470000
    min = 21470000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j]<min:
                min = tmp[j]
                sx=i
                sy=j
            if tmp[j]>max:
                max=tmp[j]
                ex=i
                ey=j
            board[i][j] = tmp[j]
    ch[sx][sy]=1
    cnt=0