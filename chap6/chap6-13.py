# 경로 탐색(그래프 DFS)
# 방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램
# 1 2 3 4 5
# 1 2 5
# 1 3 4 2 5
# 1 4 2 5
# 1 4 5
# 는 총 6가지 이다.
# 그래프에서 경로란 방문한 노드는 중복해서 방문하지 않는다.

# 입력설명
# 첫째줄에 정점의 수 N, 간선의 수 M 이 주어진다. 그 다음부터 M 줄에 걸쳐 연결정보가 주어진다.
# 5 9
# 1 2
# 1 3 
# 1 4
# 2 1
# 2 3 
# 2 5
# 3 4
# 4 2
# 4 5

# 출력설명
# 총 가지수를 출력한다.
# 6

# 내풀이
n, m = map(int, input().split())
graph =[[0]*(n) for _ in range(n)]
for i in range(m):
    before, to = map(int, input().split())
    graph[before-1][to-1] = 1
check=[0]*(n)

path = list()
count = 0

def DFS(v):
    global count
    print(path)
    if v == n:
        count+=1
    else:
        for i in range(n):
            if graph[v][i] != 0:
                path.append(v)
                graph[v][i] = 0
                DFS(i)
                path.pop()
                graph[v][i] = 1
DFS(0)
print(count)

# 해설
def DFS(v):
    global cnt
    if v == n:
        cnt+=1
        for i in path:
            print(i, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0

if __name__ == "__main__":
    n, m=map(int, input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for i in range(m):
        a,b=map(int, input().split())
        g[a][b]=1
    cnt=0
    path=[]
    path.append(1)
    ch[1]=1
    DFS(1)
    print(cnt)
