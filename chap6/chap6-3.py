# 부분집합 구하기(DFS)
# 자연수 N 이 입력되면 1부터 까지의 
# 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램

# 입력설명
# 자연수 N 이 입력
# 3

# 출력설명
# 첫번째 줄부터 차례대로 하나씩 부분집합을 출력
# 1 2 3
# 1 2
# 1 3
# 1
# 2 3
# 2
# 3

# 내 풀이
n = int(input())
num = [0]*(n+1)
def DFS(v):
    if v > n:
        for i in range(1, n+1):
            if num[i] == 1:
                print(i, end=' ')
        print()
    else:
        num[v] = 1
        DFS(v+1)
        num[v] = 0
        DFS(v+1)
DFS(1)

# 해설
def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)
        
if __name__ ==  "__main__":
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)