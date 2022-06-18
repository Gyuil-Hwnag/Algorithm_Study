# 위상정렬(그래프 정렬)

# 위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘
# 각각의 일의 선후관계가 복잡하게 얽혀있을 때 각각 일의 선후관계를 유지하면서 전체 일의 순서를 짜는 알고리즘
# 만약 아래와 같은 일의 순서를 각각 지키면서 전체 일의 순서를 정한다면
# 1 4 // 1번일을 하고 난 후 4번일을 해야한다.
# 5 4
# 4 3
# 2 5
# 2 3
# 6 2
# 전체 일의 순서는 1, 6, 2, 5, 4, 3과 같이 정할 수 있다.
# 전체 일의 순서는 여러 가지가 있으며 그 중에 하나이다.

# 입력설명
# 첫번째 줄에 전체 일의 개수 N과 일의 순서 정보의 개수 M이 주어진다.
# 두번째 줄부터 M개의 정보가 주어진다.
# 6 6
# 1 4
# 5 4
# 4 3
# 2 5
# 2 3
# 6 2

# 출력설명
# 전체 일의 순서를 출력한다.
# 1 6 2 5 4 3

# 내풀이
from collections import deque
n, m = map(int, input().split())
pointList = [0]*(n+1)
d = [0]*(n+1)
dQ = deque()
for i in range(m):
    a, b = map(int, input().split())
    pointList[a] = b
    d[b] += 1

for i in range(1, n+1):
    if d[i]==0:
        dQ.append(i)

while dQ:
    res = dQ.popleft()
    print(res, end=' ')
    for i in range(1, n+1):
        if pointList[res] != 0:
            d[i] -= 1
            if d[i] == 0:
                dQ.append(i)

# 해설
n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)
dQ=deque()
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b]+=1
    degree[b]+=1
for i in range(1, n+1):
    if degree[i] == 0:
        dQ.append(i)
while dQ:
    x=dQ.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i]==1:
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)