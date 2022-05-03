# 숫자만 추출
# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만든다.
# 만들어진 자연수와 그 자연수의 약수의 갯수를 출력한다.
# 만약 "t0e0a1c2h0er" 에서 숫자만 출력하면 0,0,1,2,0 이고 이것을 자연수로 만들면 120이다.
# 즉 첫자리 0은 무시한다. 출력을 120을 하고 그 다음줄에는 120의 약수의 갯수를 출력.

# 내 풀이

inputStr = input()

def returnNum(x):
    result = list()
    for i in x:
        if ord(i) <= 65:
            result.append(int(i))
    return result

def sumCount(x):
    count = 1
    sum = 0
    for i in x:
        sum = sum+(count*int(i))
        count = count*10
    return sum

def primeCount(x):
    count = 0
    for i in range(1, x+1):
        if x%i==0:
            count = count+1
    return count

num = returnNum(inputStr)
num = list(reversed(num))
print(sumCount(num))
sum = sumCount(num)
print(primeCount(sum))

# 해설
# isdigit() 는 모든 숫자 2^2등도
# isdecimal 은 0~9까지만
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res*10+int(x)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)

