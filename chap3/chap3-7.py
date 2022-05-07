# 사과나무(다이아몬드)
# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 
# 한그루의 사과나무가 심어져 있다. N의 크기는 항상 홀수 이다.
# 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할 떄
# 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨 놓는다.

# 만약 N이 5이면 
# X X O X X
# X O O O X
# O O O O O
# X O O O X
# X X O X X
# 이런 형싱으로 O 부분만 수확한다.
# 현수가 수확하는 사과의 총 개수를 출력하라.

# 내 풀이
n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]

point = n//2
sum = sum(apple[point])
for i in range(0, point):
    sum = sum+apple[i][point]
    sum = sum+apple[n-i-1][point]
    for j in range(i):
        sum = sum+apple[i][point-j-1]+apple[i][point+j+1]
        sum = sum+apple[n-i-1][point-j-1]+apple[n-i-1][point+j+1]

print(sum)

# 해설
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
