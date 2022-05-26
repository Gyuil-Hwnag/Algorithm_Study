# 수열 추측하기 라이브러리 사용
import itertools as it

n,f = map(int, input().split())
b=[1]*n

for i in range(1,n):
    b[i] = b[i-1]*(n-1)/i
a=list(range(1, n+1))

cnt = 0

# 조합으로 사용시 it.permutations(a, n)
for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break