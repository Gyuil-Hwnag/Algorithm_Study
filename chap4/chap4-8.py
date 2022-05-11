# 침몰하는 타이타닉(그리디)
# 유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있다. 유람선에는 N명의 승객이 타고 있다.
# 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있으며, 
# 보트 한개에 탈 수 있는 총 무게도 M Kg 이하로 제한되어 있다.
# N 명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하라.

# 입력설명
# 첫째 줄에 자연수 N, M 이 주어진다.
# 두번째 줄에 N 개로 구성된 몸무게 수열이 주어진다. 몸무게는 50 이상 150 이하.
# 각 승객의 몸무게는 M 을 넘지 않는다. 즉 탈출을 못하는 경우는 X
# 5 140
# 90 50 70 100 60

# 출력
# 구명보트의 최소갯수
# 3

# 내 풀이
n, m = map(int, input().split())
people = list(map(int, input().split()))

cnt = 0
numCount = 0
while numCount < n:
    people.sort(reverse=True)
    print(people)
    cnt+=1
    numCount+=1
    sum = people[0]
    people[0] = 0
    for i in range(0, n):
        if people[i] != 0:
            if sum + people[i] <= m:
                sum += people[i]
                people[i] = 0
                numCount += 1
print(cnt)

# 해설
from collections import deque
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)
cnt=0
while p:
    if len(p) == 1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        # p.pop(0)
        p.popleft()
        p.pop()
        cnt+=1

print(cnt)