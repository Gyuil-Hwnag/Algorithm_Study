# 회문 문자열 검사
# N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을때나 같은 경우
# (회문 문자열) 이면 YES 출력 아닐경우 NO를 출력하는 프로그램

# 내 풀이
n = int(input())

def check(x):
    check = True
    for i in range(len(x)//2):
        if x[i] == x[len(x)-1-i]:
            check = True and check
        else:
            check = False and check
    return check

resultList = list()
for i in range(n):
    x = input()
    resultList.append(check(x.upper()))

for i in range(len(resultList)):
    print("#%d %s" %(i+1, str(resultList[i])))

# 해설 1
n = int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d No" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

# 해설 2 왠만하면 1로 하기
n = int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))