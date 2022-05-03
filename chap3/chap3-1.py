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

for i in range(n):
    x = input()
    result = check(x)
    print("#%d %s" %(i+1, str(result)))