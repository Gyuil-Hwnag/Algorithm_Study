# 역수열(디그리)
# 1부터 N 까지의 수를 한번씩만 사용하여 이루어진 수열이 있을 때, 1부터 N 까지 각각의 수 앞에 높여 있는 자신보다
# 큰 수들의 개수를 수열로 표현한 것을 역수열이라고 한다.
# 예를 들어 다음과 같은 수열의 경우 4 8 6 2 5 1 3 7
# 1 앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5 이렇게 5개 이고,
# 2 앞에 놓인 2보다 큰 수는 4, 8, 6 이렇게 3개,
# 3 앞에 높인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개
# 따라서 4 8 6 2 5 1 3 7 의 역수열은 5 3 4 0 2 1 1 0 이 된다.
# N 과 1부터 N 까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원리의 수열을 출력하는 프로그램

# 입력 설명
# 첫번쨰 줄에 자연수 N 이 주어지고, 두번째 줄에는 역수열이 숫자 사이에 한칸의 공백을 두고 주어진다
# 8
# 5 3 4 0 2 1 1 0

# 출력 설명
# 4 8 6 2 5 1 3 7

# 내 풀이
n = int(input())
numList = list(map(int, input().split()))
resList = [0]*n

for i in range(n):
    num = numList[i]
    count = 0
    print(resList)
    for j in range(n):
        if num == count:
            if resList[j] == 0:
                resList[j] = i+1
                break
        if resList[j] == 0:
            count+=1

for x in resList:
    print(x, end=' ')
print()

# 해설
n = int(input())
a = list(map(int, input().split()))
seq = [0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1
for x in seq:
    print(x, end=' ')
print()