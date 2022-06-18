# 알리바바와 40인의 도둑(Bottom-Up)

# 알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있었다. 
# 알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다.
# 계곡의 돌다리는 N*N개의 돌들로 구성되어 있다. 각 돌다리들은 넢이가 서로 다르다.
# 해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비된다. 이동은 최단거리 이동을 한다.
# 즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 한다.
# N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의 최소량을 구하는 프로그램.
# 만약 N=3이고, 계곡의 돌다리 격자 정보가 다음과 같다면
# 3 3 5
# 2 3 4
# 6 5 2
# (1, 1)좌표에서 (3, 3)좌표까지 가는데 드는 최소 에너지는 3+2+3+4+2=14 이다.

# 입력설명
# 첫번째 줄에는 자연수 N이 주어진다.
# 두번째 줄부터 계곡의 N*N 격자의 돌다리 높이 정보가 주어진다.
# 5
# 3 7 2 1 9
# 5 8 3 9 2
# 5 3 1 2 3
# 5 4 3 2 1
# 1 7 5 2 4

# 출력설명
# 첫번째 줄에 (1, 1) 출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.
# 25

# 내풀이
n = int(input())
stone = list()
for i in range(n):
    new = list(map(int, input().split()))
    stone.append(new)

ch = [[0]*n for _ in range(n)]
ch[0][0] = stone[0][0]

for i in range(1, n):
    ch[i][0] = ch[i-1][0]+stone[i][0]
    ch[0][i] = ch[0][i-1]+stone[0][i]

for i in range(1, n):
    for j in range(1, n):
        ch[i][j] = min(ch[i-1][j], ch[i][j-1])+stone[i][j]

# for i in range(n):
#     print(ch[i])

print(ch[n-1][n-1])

# 해설
if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    dy[0][0] = arr[0][0]
    for i in range(n):
        dy[0][i]=dy[0][i-1]+arr[0][i]
        dy[i][0]=dy[i-1][0]+arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i-1][j], dy[i][j-1])+arr[i][j]
    print(dy[n-1][n-1])