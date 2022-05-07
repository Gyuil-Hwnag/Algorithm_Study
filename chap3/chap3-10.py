# 격자판 회문수
# 1 부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는
# 세로방향으로 길이 5자리 회문수가 몇개 있는지 구하는 프로그램
# 회문수란 13231 같이 앞에서나 뒤어서 읽어도 같은수
# 단 구부러진 경우는 포함X

# 내 풀이
a = [list(map(int, input().split())) for _ in range(7)]

def check(x):
    if x[0]==x[4] and x[1]==x[3]:
        return True
    else:
        return False

count = 0
for k in range(7):
    for i in range(0, 3):
        num = list()
        for j in range(i, i+5):
            num.append(a[k][j])
        if check(num):
            count+=1
            print(num)

for k in range(7):
    for i in range(0, 3):
        num = list()
        for j in range(i, i+5):
            num.append(a[j][k])
        if check(num):
            count+=1
            print(num)

print(count)

# 해설
board = [list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
