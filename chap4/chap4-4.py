# 마구간 정하기 (결정 알고리즘)
# N 개의 마구간이 수직선상에 있다. 각 마구간은 x1, x2, x3, ... , xN 의 좌표를 가지며, 마구간간에 좌표가 중복되는 일은 없다.
# 현수는 C 마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않는다.
# 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶다.
# C 마리의 말을 N 개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대값을 출력하라.

# 입력 설명
# 첫줄에 N, C
# 둘째줄 부터 N 개의 마구간 좌표가 한줄씩
# 5 3
# 1
# 2
# 6
# 4
# 9

# 출력 예제
# 3

# 내 풀이
from operator import le


n, c = map(int, input().split())
house = list()
for i in range(n):
    house.append(int(input()))

house.sort()

left = 0
right = len(house)-1
max = 0
while left <= right:
    point = (left+right)//2
    cnt=1
    last = house[0]
    for i in range(1, n):
        if house[i]-last >= point:
            cnt+=1
            last = house[i]
    if cnt >= c:
        max = point
        left = point+1
    else:
        right = point-1

print(max)

# 해설
def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)