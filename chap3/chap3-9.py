# 봉우리
# 지도정보가 N * N 격자판에 주어진다. 각 격자에는 그 지역의 높이가 쓰여있다.
# 각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리의 지역이다.
# 봉우리 지역이 몇 개 있는지 알아내는 프로그램
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
# 만약 N = 5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개 이다.

# 입력 예시
# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2

# 출력 예시
# 10

# 내 풀이
n = int(input())
mount = [list(map(int, input().split())) for _ in range(n)]
mount.insert(0, [0]*n)
for x in mount:
    x.insert(0, 0)
    x.append(0)
mount.append([0]*(n+1))
print(mount)

count = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        max = mount[i][j]
        if max > mount[i-1][j] and max > mount[i+1][j] and max > mount[i][j-1] and max > mount[i][j+1]:
            count+=1

print(count)

# 해설
# 방향성
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)
cnt = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)





