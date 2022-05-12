# 가장 큰수
# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m 개의 숫자를 제거하여 가장 큰 수를 만들라고 한다. (숫자의 순서는 유지)
# 만약 5276823 이 주어지고 3개의 자리수를 제거한다면
# 7823 이 가장 큰 숫자가 된다.

# 입력 설명
# 첫째 줄에 숫자와 제거해야할 자릿수의 개수가 주어진다.
# 5276823 3

# 출력 설명
# 7823

# 내 풀이
n, m = map(int, input().split())
n = str(n)
numList = list()
for i in range(len(n)):
    numList.append(int(n[i]))

resList = list()
count = 0

for i in numList:
    while count<m and len(resList)>0 and i>resList[-1]:
        resList.pop()
        count+=1
    resList.append(i)
if m > count:
    resList = resList[:-(m-count)]
for i in resList:
    print(i, end='')
print()

# 해설
num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack = stack[:-m]

res=''.join(map(str, stack))
print(res)