# 인접행렬(가중치 방향 그래프)
# 그래프 정보를 인접행렬로 표현

# 입력설명
# 첫째 줄에는 정정의 수 N, 간선의 수 M 이 주어진다. 그 다음부터 M 줄에 걸쳐 연결정보와 거리비용이 주어진다.
# 6 9
# 1 2 7
# 1 3 4
# 2 1 2
# 2 3 5
# 2 5 5
# 3 4 5
# 4 2 2
# 4 5 5
# 6 4 5

# 출력설명
# 인접행렬을 출력하라.
# 0 7 4 0 0 0
# 2 0 5 0 5 0
# 0 0 0 5 0 0
# 0 2 0 0 5 0
# 0 0 0 0 0 0
# 0 0 0 5 0 0

# 내풀이
n, m = map(int, input().split())
graph =[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    num = map(int, input().split())
    graph[num[0]-1][num[1]-1] = num[2]

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()


# 해설
n,m = map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b]=c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()