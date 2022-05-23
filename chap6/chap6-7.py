# 동전교환
# 다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환해주려면 어떻게 주면 되는가?
# 각 단위의 동전은 무한정 쓸  수 있다.

# 입력설명
# 첫번째 줄에는 동전의 종류개수 N이 주어진다. 두번째 줄에는 N개의 동전의 종류가 주어지고,
# 그 다음줄에는 거슬러 줄 금액 M이 주어진다. 각 동전의 종류는 100원을 넘지 않는다.
# 3
# 1 2 5
# 15

# 출력설명
# 첫번째 줄에 거슬러 줄 동전의 최소개수를 출력
# 3

# 내풀이
n = int(input())
coinlist = list(map(int, input().split()))
coinlist.sort(reverse=True)
max = int(input())

min = max
def DFS(v, sum, count):
    global min
    if min < count:
        return
    if sum > max or v == n:
        return
    elif sum == max:
        if min > count:
            min = count
    else:
        DFS(v, sum+coinlist[v], count+1)
        DFS(v+1, sum+coinlist[v], count+1)
        DFS(v+1, sum, count)

DFS(0, 0, 0)
print(min)

# 해설
def DFS(L, sum):
    global res
    if L>res:
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__ == "__main__":
    n = int(input())
    a=list(map(int, input().split()))
    m=int(input())
    res=-21470000
    a.sort(reverse=True)
    DFS(0,0)
    print(res)
