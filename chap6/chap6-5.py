# 바둑이 승차(DFS)
# 철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램을 넘게 태울수가 없다.
# 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
# N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울수 있는 가장 무거운 무게를 구하는 프로그램

# 입력설명
# 첫번째 줄에 자연수 C, N이 주어진다.
# 둘째줄부터 N 마리 바둑이의 무게가 주어진다.
# 259 5
# 81
# 58
# 42
# 33
# 61

# 출력설명
# 첫번째 줄에 가장 무거운 무게를 출력
# 242

# 내풀이
from unittest import result


c, n = map(int, input().split())
doglist = list()
for i in range(n):
    doglist.append(int(input()))

min = 0
def DFS(v, w):
    global min, n, c
    if w > c or v == n:
        if w>min and w<c:
            min = w
        return
    else:
        DFS(v+1, w+doglist[v])
        DFS(v+1, w)
        if w>min and w<c:
            min = w
            print("YES %d %d" %(v, w))
        else:
            print("NO %d %d" %(v, w))
DFS(0, 0)
print(min)

# 해설
def DFS(L, sum, t_sum):
    global result
    # 시간초과 때문에 넣어야 함
    if sum+(total-sum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
        else:
            DFS(L+1, sum+a[L], t_sum+a[L])
            DFS(L+1, sum, t_sum+a[L])

if __name__ == "__main__":
    c, n = map(int, input().split())
    a=[0]*n
    result=-2147000
    for i in range(n):
        a[i]=int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)