# 합이 같은 부분집합(DFS : 아마존 인터뷰)
# N 개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때
# 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 "YES"를 출력하고, 그렇지 않으면 "NO"를
# 출력하는 프로그램을 작성하시오.
# 둘로 나뉘는 두 부분집합은 서로소의 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어야 한다.
# 예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10}으로 
# 두 부분집합의 합이 16 으로 같은 경우가 존재하는 것을 알 수 있다.

# 입력설명
# 첫줄에 자연수 N, 두번째 줄에 집합의 원소 N개가 주어진다. 원소는 중복 X
# 6
# 1 3 5 6 7 10

# 출력설명
# YES or NO
# YES

# 내풀이
n = int(input())
numlist = list(map(int, input().split()))
check = [0]*(n)
sum = 0
print(numlist)
for i in numlist:
    sum += i
res = False
def DFS(v):
    global res
    if res:
        return
    if v == n:
        checksum = 0
        for i in range(n):
            if(check[i] == 1):
                checksum += numlist[i]
        if checksum == (sum-checksum):
            res = True
            return
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)
DFS(0)
if res:
    print("YES")
else:
    print("NO")

# 해설
import sys
def DFS(L, sum):
    if sum>total//2:
        return
    if L == n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0,0)
    print("NO")