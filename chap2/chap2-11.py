# 점수 계산
# OX문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말한다.
# 여러개의 OX문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에는 
# 가산점을 주기 위해서 다음과 같이 점수 계산을 한다.
# 1번문제가 맞은경우 1점. 앞의 문제를 틀리다가 처음 답을 맞는 경우는 1점
# 또한 연속으로 답을 맞는 경우 두번째는 2점 세번째는 3점... k번째는 k점으로 계산
# 틀린경우 0점으로 계산

# 내 풀이
n = int(input())
result = list(map(int, input().split()))

count = 1
score = 0
for i in range(n):
    if result[i] == 1:
        score = score+count
        count = count+1
    else: 
        count = 1

print(score)

# 해설
n  = int(input())
a = list(map(int, input().split()))
sum=0
cnt=0
for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
print(sum)