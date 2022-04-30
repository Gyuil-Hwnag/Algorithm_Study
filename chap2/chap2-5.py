# 대표값
# N명의 학생의 수학점수가 주어진다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
# N명의 학생 중 평균에 가장 가까운 학생은 몇번째 학생인지 출력하는 프로그램
# 평균과 가장 가까운 점수가 여러개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
# 높은 점수를 가진 학생이 여러명일 경우 그 중 학생번호가 빠른 학생의 번호를 답

# 나의 풀이

a = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
# average = round(sum(a)/len(a)) # round 5이상에서 올려주는게 아니므로 다른거 써야함
average = round(sum(a)/len(a)+0.5)

res = 0
min = max(a) - average
score = 0

for i in range(0, len(a)):
    if abs(a[i] - average) <= min:
        min = abs(a[i] - average)
        if score < a[i]:
            score = a[i]
            res = i

print("%d %d" %(average, res+1))

# 해설
a = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
# ave = round(sum(a)/len(a))
ave = round(sum(a)/len(a)+0.5)

min = max(a)

for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print("%d %d" %(ave, res))