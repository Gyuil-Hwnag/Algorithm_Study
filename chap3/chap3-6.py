# 격자판 최대합
# 5*5 격자판에 숫자가 적혀있다.
# N*N 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합중
# 가장 큰 합을 출력하라.

# 입력 예제
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# 출력 예제
# 155

# 내풀이
n = int(input())

pan = ([0]*n)*n
for i in range(n):
    pan[i] = list(map(int, input().split()))

max = 0
# 행
for i in range(n):
    if max < sum(pan[i]):
        max = sum(pan[i])
# 열
for i in range(n):
    sum = 0
    for j in range(n):
        sum = sum+pan[j][i]
    if sum > max:
        max = sum
# 대각선
sum = 0
for i in range(n):
    sum = sum+pan[i][i]
if max > sum:
    sum = max
for i in range(n):
    sum = sum+pan[i][n-1-i]
if max > sum:
    sum = max

print(max)

# 해설

