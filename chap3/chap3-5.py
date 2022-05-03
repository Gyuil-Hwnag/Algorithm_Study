# 수들의 합
# N개의 수로 된 수열 A[1], A[2], ... , A[N]이 있다.
# 이 수열의 i 번째 수부터 j 번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]
# 가 M 이 되는 경우의 수를 구하는 프로그램
# 총갯수 합
# 배열
# 이런식으로 입력값이 들어온다.

# 내 풀이
m, n = map(int, input().split())
num = list(map(int, input().split()))

count = 0
for i in range(len(num)):
    sum = 0
    for j in range(i, len(num)):
        sum = sum+num[j]
        if sum > n:
            break
        elif sum == n:
            count+=1
            print("%d %d" %(i, j))
            break

print(count)

# 해설
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)