# 중복순열 구하기
# 1부터 N까지 번호가 적힌 구슬이 있다. 이중 중복을 허용하여 M 번을 뽑아 일렬로 나열하는 방법을 모두 출력

# 입력설명
# 첫번째 줄에 N, M 이 주어진다.
# 3 2

# 출력설명
# 첫번째줄에 결과를 출력. 맨 마지막 총 경우의 수를 출력
# 출력순서는 사전순으로 오름차순으로 출력

# 해설
def DFS(L):
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)

if __name__ == "__main__":
    n,m = map(int, input().split())
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)
