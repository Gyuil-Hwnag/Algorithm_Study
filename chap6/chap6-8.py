# 순열 구하기
# 1부터 N 까지 번호가 적힌 구슬이 있다. 이중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력

# 입력설명
# 첫번쨰 줄에 자연수 N, M 이 주어진다.
# 3 2

# 출력설명
# 첫번째 줄에 결과를 출력한다. 맨 마지막 총 경우의 수를 출력한다.
# 출력순서는 사전순으로 오름차순으로 출력
# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2
# 6

# 내풀이
n, m = map(int, input().split())

numlist = [0]*m
check = [0]*(n+1)
count = 0
def DFS(L):
    global numlist, count
    if L==m:
        for j in range(m):
            print(numlist[j], end=' ')
        print()
        count += 1
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                numlist[L]=i
                DFS(L+1)
                check[i] = 0

DFS(0)
print(count)

# 해설
def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0


if __name__ == "__main__":
    n,m=map(int, input().split())
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)
