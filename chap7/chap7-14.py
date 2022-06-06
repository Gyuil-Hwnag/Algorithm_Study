# 안전영역(BFS)

# 재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다.
# 먼저 어떤 지역의 높이 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 
# 최대 몇개가 만들어 지는지를 조사한다. 이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은
# 물에 잠긴다고 하자. 어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수
# 예를 들어, 다음 N=5인 지역의 높이 정보이다.
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
# 이제 위와 같은 지역에 많은비가 내려서 높이가 4이하인 모든 지점이 물어 잠겼다고 한다면
# 물에 잠기지 않은 안전한 영역이라 함은 물에 잠기지 않은 지점들이 위, 아래, 오른쪽, 왼쪽으로 인접해 있으며 그 크기가 최대인 영역
# 위의 경우에는 잠기지 않은 안전한 영역은 5개가 된다. 또한 위와 같은 지역에서 높이가 6이하인 지점을 모두 잠기게 만드는 많은 비가 내리면
# 물에 잠기지 않은 안전한 영역은 4개가 된다.
# 이와 같이 장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다.
# 위의 예와 같이 지역에서 내리는 비의 양에 따라서 모든 경우를 다 조사하면 물에 잠기지 않는 안전한 영역의 개수중에서 
# 최대인 경우는 5임을 알 수 있다.
# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램

# 입력설명
# 첫째줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2이상 100이하의 정수이다. 
# 둘째줄부터 N개의 각 줄에는 2차원 배열의 첫번쨰 행부터 N번쨰 행까지 순서대로 한행씩 높이 정보가 입려된다.
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

# 출력설명
# 첫째줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대개수를 출력한다.
# 5

# 내풀이
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
board =[list(map(int, input().split())) for _ in range(n)]
maxi = 0
for i in range(n):
    for j in range(n):
        if board[i][j] > maxi:
            maxi = board[i][j]

res = []
Q=deque()

for m in range(1, maxi):
    ch = [[0]*n]*n
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > m:
                ch[i][j]=1
                Q.append((i, j))
                cnt=1
                while Q:
                    tmp=Q.popleft()
                    for k in range(4):
                        x=tmp[0]+dx[k]
                        y=tmp[1]+dy[k]
                        if 0<=x<n and 0<=y<n and ch[x][y]==0:
                            ch[x][y]=1
                            Q.append((x, y))
                            cnt+=1
    res.append(cnt)
print(max(res))

# 해설(DFS)
import sys
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

# 시간 넘어갔을 경우 종료 시켜버리는 함수
# 설정 안하면 런타임 에러 발생
sys.setrecursionlimit(10**6)

def DFS(x, y, h):
    ch[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
            DFS(xx, yy, h)

if __name__=="__main__":
    n = int(input())
    cnt = 0
    res = 0
    board=[list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h:
                    cnt+=1
                    DFS(i, j, h)
        res=max(res, cnt)
        if cnt==0:
            break
    print(res)