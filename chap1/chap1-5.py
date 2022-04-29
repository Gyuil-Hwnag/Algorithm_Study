n = int(input())

# 1~N까지 홀수
for i in range(1, n+1):
    if i%2==1:
        print(i)

# 1부터 N 까지 합
sum = 0
for i in range(1, n+1):
    sum = sum+i
print(sum)

# N의 약수
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')