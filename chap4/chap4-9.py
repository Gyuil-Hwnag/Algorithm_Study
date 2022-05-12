# 증가수열 만들기 (그리디)
# 1부터 N 까지의 모든 자연수로 구성된 길이 N 의 수열이 주어진다.
# 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자중 하나를 가져와 나열하여 가장 긴 증가수열을 만든다.
# 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝) 는 그 수열에서 제거된다.
# 예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4이다.
# 맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고 왼쪽 끝에서 4, 왼쪽 끝에서 5를 가져와 
# 2 3 4 5 증가수열을 만들 수 있다.

# 입력 설명
# N 이 주어지고 두번째 줄에는 N 개로 구성된 수열이 주어진다.

# 첫째줄에 최대 증가수열의 길이를 출력
# 두번째 줄에 가져간 선서대로 왼쪽 끝이면 L 오른쪽 끝이면 R를 써간 문자열 출력

# 내 풀이

n = int(input())
numList = list(map(int, input().split()))
res = ""
check = 0

check = min(numList[0], numList[-1])
while True:
    if numList[0] < numList[-1]:
        if numList[0] >= check:
            res+="L"
            check = numList[0]
            numList.pop(0)
        else:
            if numList[-1] >= check:
                res+="R"
                check = numList[-1]
                numList.pop()
            else:
                break
    else:
        if numList[-1] >= check:
            res+="R"
            check = numList[-1]
            numList.pop()
        else:
            if numList[0] >= check:
                res+="L"
                check = numList[0]
                numList.pop(0)
            else:
                break

print(len(res))
print(res)


# 해설
n = int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res+=tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1] == 'L':
            lt+=1
        else:
            rt-=1
    tmp.clear()

print(len(res))
print(res)

