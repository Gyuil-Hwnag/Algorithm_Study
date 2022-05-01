# 자릿수의 합
# N 개의 자연수가 입력되면 각 자릿수의 합을 구하고, 합이 최대인 자연수를 풀력하는 프로그램

# 내 풀이
# a = (125, 15232, 98, 97)
a = list(map(int, input().split()))

max = 0
result = a[0]
def digit_sum(x):
    global max, result
    init = x
    sum = 0
    while x > 0:
        sum += x%10
        x = x/10
    if sum > max:
        result = init
        max = sum

for i in range(0, len(a)):
    digit_sum(a[i])

print(result)

# 해설
a = list(map(int, input().split()))

# def digit_sum(x):
#     sum = 0
#     while x>0:
#         sum+=x%10
#         x = x//10
#     return sum

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2417000
for x in a:
    tot = digit_sum(x)
    if tot>max:
        max = tot
        res = x

print(res)