# 최대 부분 증가수열

# N개의 자연수로 이루어진 수열이 주어졌을 때, 그 중에서 가장 길게 증가하는(작은수에사 큰 수로) 원소들의 집합을 찾는 프로그램을 작성
# 예를 들어 2, 7, 5, 8, 6, 4, 7, 12, 3 이면 가장 길게 증가하도록 원소들을 차례대로 뽑아내면 2, 5, 7, 12를 뽑아내어
# 길이가 5인 최대 부분 증가수열을 만들 수 있다.

# 입력설명
# 첫째줄에 입력되는 데이터의 수 N을 의미하고, 둘째줄에는 N개의 입력데이터들이 주어진다.
# 8
# 5 3 7 8 6 2 9 4

# 출력설명
# 첫번째 줄에 부분증가수열의 최대 길이를 출력
# 4

# 내풀이
n = int(input())
num = list(map(int, input().split()))

dy = [0]*(n)
dy[0] = 1
res = 0
def DFS(L):
    global res
    if L==n:
        return
    else:
        max = 0
        for i in range(1, L):
            if num[L]>num[i] and dy[i]>max:
                max=dy[i]
        dy[L]=max+1
        if max+1 > res:
            res = max+1
        DFS(L+1)
DFS(1)
print(res)

# 해설
n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2, n+1):
    max=0
    for j in range(i-1, 1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]