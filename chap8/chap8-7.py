# 가장 높은 탑 쌓기(LIS 응용)

# 밑면이 정사각형인 직윤면체 벽돌들을 사용하여 탑을 쌓고자 한다. 탑은 벽돌을 한개씩 아래에서 위로 쌓으면서 만들어 간다.

# 아래의 조건을 만족하면서 가장 높은 탑을 쌓을 수 있는 프로그램을 작성하라.
# 조건 1. 벽돌은 회전시킬 수 없다. 즉, 옆면을 밑면으로 사용할 수 없다.
# 조건 2. 밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다.
# 조건 3. 벽돌들의 높이는 같을 수도 있다.
# 조건 4. 탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
# 조건 5. 무게가 무거운 벽돌을 무게가 가벼운 벽돌위에 놓을 수 없다.

# 입력설명
# 첫째줄에는 입력될 벽돌의 수가 주어진다. 입력으로 주어지는 벽돌의 수는 최대 100개이다.
# 둘째줄부터는 각 줄에 한 개의 벽돌에 관한 정보인 벽돌 밑면의 넓이, 벽돌의 높이 그리고 무게가 차례대로 주어진다.
# 각 벽돌은 입력되는 순서대로 1부터 연속적인 번호를 가진다.
# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2

# 출력설명
# 첫번째 줄에 가장 높이 쌓을 수 있는 탑의 높이를 출력한다.
# 10

# 내풀이
n = int(input())
block = list()
res = 0
for i in range(n):
    s, h, w = map(int, input().split())
    block.append([s, h, w])
block.sort(reverse=True)

dy = [0]*(n)
dy[0] = block[0][1]

for i in range(1, n):
    max = 0
    for j in range(i):
        if block[i][0] < block[j][0] and block[i][2] < block[j][2] and max < dy[j]:
            max = dy[j]
    dy[i] = max+block[i][1]
    if dy[i] > res:
        res = dy[i]

print(res)

# 해설
if __name__ == "__main__":
    n=int(input())
    brick=[]
    for i in range(n):
        a, b, c = map(int, input().split())
        brick.append((a, b, c))
    brick.sort(reverse=True)
    dy=[0]*n
    dy[0]=brick[0][1]
    res=brick[0][1]
    for i in range(1,n):
        max_h=0
        for j in range(i-1, -1, -1):
            if brick[j][2]>brick[i][2] and dy[j]>max_h:
                max_h=dy[j]
        dy[i]=max_h+brick[i][1]
        res=max(res, dy[i])
    print(res)