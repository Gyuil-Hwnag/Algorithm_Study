# 수들의 조합
# N 개의 정수가 주어지면 그 숫자들 중 K 개를 뽑는 조합의 합이 임의의 정수 M 의 배수인 개수는 몇개가 있는지 출력하는 프로그램

# 입력설명
# 첫줄에 정수의 개수 N 과 임의의 정수 K 가 주어지고,
# 두번째 줄에는 N 개의 정수가 주어진다.
# 세번째 줄에 M 이 주어진다.
# 5 3
# 2 4 5 8 12
# 6

# 출력설명
# 총 가지수를 출력한다.
# 2

# 내풀이
n, k = map(int, input().split())
numlist = list(map(int, input().split()))
ba = int(input())

max = sum(numlist)
check = [0]*(max+1)

num = list()
def DFS(v):
    if v == n:
        if len(num) == k:
            numCheck = sum(num)
            # print(numCheck)
            if check[numCheck] == 0:
                check[numCheck] = 1
            return
    elif v > n:
        return
    if len(num) == k:
        numCheck = sum(num)
        # print(numCheck)
        
        if check[numCheck] == 0:
            check[numCheck] = 1
        return
    else:
        for i in range(v, n):
            num.append(numlist[v])
            DFS(i+1) 
            num.pop()
            DFS(i+1)

DFS(0)
count=0
for i in range(ba, max+1, ba):
    if check[i] == 1:
        count+=1
print(count)

# 해설
def DFS(L, s, sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])

if __name__ == "__main__":
    n, k = map(int, input().split())
    a=list(map(int, input().split()))
    m=int(input())
    cnt=0
    DFS(0,0,0)
    print(cnt)