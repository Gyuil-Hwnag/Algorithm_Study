# 플로이드 워샬 알고리즘(그래프 최단거리)

# N개의 도시가 주어지고, 각 도시들을 연결하는 도로와 해당 도로를 통행하는 비용이 주어질 때 
# 모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최솟값을 구하는 프로그램을 작성

# 입력설명
# 첫번째 줄에는 도시의 수: N, 도로의 수: M이 주어지고, M줄에 걸쳐 도로정보와 비용이 주어진다.
# 만약 1번 도시와 2번 도시가 연결되고 그 비용이 13이면 "1 2 13" 으로 주어진다.
# 5 8 
# 1 2 6
# 1 3 3
# 3 2 2
# 2 4 1
# 2 5 13
# 3 4 5
# 4 2 3
# 4 5 7

# 출력설명
# 0 5 3 6 13 // 1번 정점에서 2번 정점으로 5, 1에서 3번 정점으로 3, 1에서 4번 정점으로 6...
# M 0 M 1 8  // 2번 정점에서 1번 정점으로는 갈 수 없으므로 M...
# M 2 0 3 10
# M 3 M 0 7
# M M M M 0

# 해설  
if __name__=="__main__":
    n, m=map(int, input().split())
    dis=[[5000]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i]=0
    for i in range(m):
        a, b, c=map(int, input().split())
        dis[a][b]=c
    
    # 플로이드 워샬 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j]==5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()