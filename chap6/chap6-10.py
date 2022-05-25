# 조합 구하기
# 1부터 N까지 번호가 적힌 구슬이 있다. 이중 M개를 뽑는 방법의 수를 출력하는 프로그램

# 입력설명
# 첫번째 줄에 자연수 N, M 이 주어진다.
# 4 2

# 출력설명
# 첫번째 줄에 결과를 출력. 맨 마지막 총 경우의 수를 출력
# 출력 순서는 사전순으로 오름차순으로 출력

# 내 풀이
n, m = map(int, input().split())
ch = [0]*n
cnt = 0
num = list()

def DFS(v, s):
    global cnt
    if len(num) == m:
        cnt+=1
        for x in num:
            print(x, end=' ')
        print()
    else:
        for i in range(v, n):
            if ch[i] == 0:
                ch[i] = 1
                num.append(i+1)
                DFS(i, v+1)
                ch[i]=0
                num.pop()

DFS(0, 1)
print(cnt)

# 해설
def DFS(L, s):
    global cnt
    if L==m:
        for j in range(j):
            print(res[j], end=' ')
        cnt+=1
        print()
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1)

if __name__ == "__main__":
    n,m = map(int, input().split())
    res=[0]*(n+1)
    cnt=0
    DFS(0,1)
    print(cnt)
