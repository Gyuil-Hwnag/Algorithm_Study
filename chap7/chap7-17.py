# 피자 배달 거리(삼성 SW역량 평가 기출문제 : DFS활용)

# N*N 크기의 도시지도가 있다. 도시지도는 1*1크기의 격자칸으로 이루어져 있다. 각 격자칸에는 0은 빈칸, 1은 집, 2는 피자집으로 표현된다.
# 각 격자칸은 좌표(행, 열)로 표현된다. 행번호는 1부터 N번까지이고, 열 번호도 1부터 N까지이다.
# 도시에는 각 집마다 "피자 배달 거리"가 있는데 각 집의 피자배달거리는 해당 집과 도시의 존재하는 피자집들과의 거리중 
# 최소값을 해당집의 "피자 배달 거리"라고 한다.
# 집과 피자집의 피자배달거리는 |x1-x2|+|y1-y2| 이다.
# 예를 들어, 도시의 지도가 아래와 같다면
# 0 1 0 0
# 0 0 2 1
# 0 0 1 0
# 1 2 0 2
# (1,2)에 있는 집과 (2,3)에 있는 피자집과의 피자 배달 거리는 |1-2|+|2-3|=2가 된다. 최근 도시가 불경기에 접어들어
# 우후죽순 생겼던 피자집들이 파산하고 있다. 도시 시장은 도시에 있는 피자집 중 M개만 살리고 나머지는 보조금을 주고 폐업시키려고 한다.
# 시장은 사리고자 하는 피자집 M개를 선택하는 기준으로 도시의 피자배달거리가 최소가 되는 M개의 피자집을 선택하려고 한다.
# 도시의 피자 배달 거리는 각 집들의 피자 배달 거리를 합한 것을 말한다.

# 입려설명
# 첫째줄에 N과 M이 주어진다.
# 둘째줄 부터는 도시 정보가 입력된다.
# 4 4
# 0 1 2 0
# 1 0 2 1
# 0 2 1 2
# 2 0 1 2

# 출력설명
# 첫째줄에 M개의 피자집이 선택되었을 때 도시의 최소 피자 배달 거리를 출력한다.
# 6

# 내풀이
n, m = map(int, input().split())
board =[list(map(int, input().split())) for _ in range(n)]
house = list()
pizza = list()
check = [0]*m
res = 10000

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            house.append((i, j))
        elif board[i][j]==2:
            pizza.append((i, j))

def DFS(L,s):
    global res
    if L==m:
        sum = 0
        for i in range(len(house)):
            num = 100000
            for j in range(len(pizza)):
                num = min(num, abs(house[i][0]-pizza[j][0])+abs(house[i][1]-pizza[j][1]))
            sum+=num
        if res > sum:
            res = sum
    else:
        for i in range(s, len(pizza)):
            check[L] = i
            DFS(L+1, i+1)
DFS(0, 0)
print(res)

# 해설
def DFS(L, s):
    global res
    if L==m:
        sum=0
        for j in range(len(hs)):
            x1=hs[j][0]
            y1=hs[j][1]
            dis=2147000
            for x in ch:
                x2=pz[x][0]
                y2=pz[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum += dis
        if sum<res:
            res=sum
    else:
        for i in range(s, len(pz)):
            ch[L]=i
            DFS(L+1, i+1)


if __name__ == "__main__":
    n, m=map(int, input().split())
    board =[list(map(int, input().split())) for _ in range(n)]
    hs=[]
    pz=[]
    ch=[0]*m
    res=21470000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i, j))
            elif board[i][j]==2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)