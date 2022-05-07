# 스도쿠 검사
# 스도쿠는 매우 간단한 숫자 퍼즐이다. 9x9 크기의 보드가 있을 때, 
# 각 행과 각 열 그리고 9개의 3x3 크기의 보드에 1부터 9까지의 숫자가
# 중복 없이 나타나도록 보드를 채우면 된다.
# 주어진 스도쿠가 완벽하게 풀었으면 YES, 잘못풀었으면 NO 를 출력

# 내 풀이
n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]

def checkSudoku(sudoku):
    for i in range(n):
        my_set = set(sudoku[i])
        if len(my_set) != n:
            print("NO")
            return False
    for i in range(n):
        a = list()
        for j in range(n):
            a.append(sudoku[j][i])
        my_set = set(a)
        if len(my_set) != n:
            print("NO")
            return False
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            a = list()
            for k in range(i, i+3):
                for s in range(j, j+3):
                    a.append(sudoku[k][s])
            my_set = set(a)
            if len(my_set) != n:
                print("NO")
                return False
    print("YES")
    return True

checkSudoku(x)

# 해설
def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[i][j]]=1
        if sum(ch1) != 9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
