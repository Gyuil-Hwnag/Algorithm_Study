# 창고 정리(그리디)
# 창고에 상자가 가로방향으로 일렬로 쌓여 있다. 
# 만약 가로가 7이라면 1열은 높이가 6으로 6개의 상자가 쌓여 있고, 2열은 3개의 상자, 3열은 9개의 상자가 쌓여 있으며 높이는 9라고 한다.
# 창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.
# 가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
# 위의 그림을 1회 높이 조정을 하면
# X X X X X X X
# X X O X X X X
# X X O X X O X
# X X O O X O X
# O X O O X O O
# O X O O X O O
# O X O O X O O
# O O O O X O O
# O O O O O O O
# O O O O O O O

# X X X X X X X
# X X X X X X X
# X X O X X O X
# X X O O X O X
# O X O O X O O
# O X O O X O O
# O X O O X O O
# O O O O O O O
# O O O O O O O
# O O O O O O O 
# (3, 9) -> (5, 3)
# 창고의 가로 길이와 각 열의 상자 높이가 주어진다. m 회의 높이 조정을 한 후 가장 높은 곳과 가장 낮은 곳의 차이를 출력하라

# 입력 설명
# 첫째줄에 창고 가로의 길이인 자연수 L 이 주어진다.
# 두번째 줄에 L 개의 자연수가 공백을 사이에 두고 입력된다. 각 자연수는 100을 넘지 않는다.
# 서벤째 줄에 높이 조정 횟수인 M 이 주어진다.
# 10 
# 69 42 68 76 40 87 14 65 81
# 50

# 출력 설명
# M 회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이를 출력
# 20

# 내 풀이
n = int(input())
block = list(map(int, input().split()))
count = int(input())

check = 0
while check < count:
    block.sort()
    # print(block)
    a = min(block[1]-block[0]+1, block[n-1]-block[n-2]+1)
    num = min(a, n)
    check += num
    # print(check)
    block[0] += num
    block[n-1] -= num

block.sort()
print(block)
print(block[n-1]-block[0])

# 해설
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()
for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()

print(a[L-1]-a[0])