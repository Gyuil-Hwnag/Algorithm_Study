# 곳감(모래시계)
# 현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있다.
# 현수의 마당은 N*N 격자판으로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정한다.
# 그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않는다.
# 그래서 현수는 격자의 행을 기준으로 왼쪽, 오른쪽으로 회전시켜 모든 감을 잘 마르게 한다.
# 만약 회전명령 정보가 2 0 3 이면 2번째 행을 왼쪽으로 3만큼 회전시키는 명려 

# 2행 12 39 30 23 11 -> 23 11 12 39 30
# 첫번째 수는 행번호, 두번째 수는 방향 0이면 왼쪽 1이면 오른쪽 세변째 수는 회전하는 격자의 수
# M 개의 회전 명령을 실행하고 난후 모래시계 모양의 영역에는 감이 총 몇개인지 출력

# O O O O O
# X O O O X
# X X O X X
# X O O O X
# O O O O O
# 이렇게 O 부분의 감의 갯수

# 입력예제
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4

# 내 풀이
from tkinter import E


n = int(input())
gam = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    a, b, c = map(int, input().split())
    if b == 1:
        before = [0]*(c)
        for i in range(n):
            before.append(gam[a-1][i])
        for i in range(len(before)):
            gam[a-1][i%n] = before[i]    
    else:
        gam[a-1].reverse()
        before = [0]*(c)
        for i in range(n):
            before.append(gam[a-1][i])
        for i in range(len(before)):
            gam[a-1][i%n] = before[i]
        gam[a-1].reverse()

res = gam[n//2][n//2]
start = 0
end = n
point = n//2
for i in range(n//2):
    for j in range(start, end):
        res = res+gam[i][j]
        res = res+gam[n-1-i][j]
    start+=1
    end-=1

print(res)

# 해설
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k=map(int, input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)