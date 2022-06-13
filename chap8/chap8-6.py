# 최대 선 연결하기(LIS 응용)

# 왼쪽의 번호와 오른쪽의 번호가 있는 그림에서 같은 번호끼리 선으로 연결하려고 한다.
# 왼쪽 번호는 무조건 위에서부터 차례로 1부터 N까지 오름차순으로 나열되어 있다.
# 오른쪽 번호 정보가 위부터 아래 순서로 주어지지만 서로 선이 겹치지 않고 최대 몇개의 선을 연결할 수 있는지 구하는 프로그램을 작성

# 입력설명
# 첫줄에 자연수 N이 주어진다.
# 두번째 줄에 1부터 N까지의 자연수 N개의 오른쪽 번호 정보가 주어진다. 순서는 위쪽번호부터 아래쪽 번호 순으로이다.
# 10
# 4 1 2 3 9 7 5 6 10 8

# 출력셜명
# 첫줄에 겹치지 않고 그을수 있는 최대선의 개수를 출력
# 6

# 내풀이
n = int(input())
num = list(map(int, input().split()))
dy = list()
res = 0

for i in range(1, len(num)+1):
    dy.append([1, num.index(i)])

for i in range(1, n):
    max = 0
    for j in range(i):
        if dy[j][1]<dy[i][1] and max<dy[j][0]:
            max = dy[j][0]
    dy[i][0] = max+1

    if dy[i][0] > res:
        res = dy[i][0]

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
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]
print(res)

