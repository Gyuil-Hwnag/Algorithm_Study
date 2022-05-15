# 응급실
# 메디컬 병원 응급실에는 의사가 한명 밖에 없다. 응급실은 환자가 도착한 순서대로 진료를 한다.
# 하지만 위험도가 높은 환자는 빨리 응급조치를 의사가 해야한다. 이런 문제를 보완하기 위해 응급실은 다음과 같은 방법으로 환자의 진료순서를 정한다.
# 1. 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자 목록을 꺼낸다.
# 2. 나머지 대기 목록에서 꺼낸 환자보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 다시 넣는다. 그렇지 않으면 진료를 받는다.
# 즉 대기목록에 자기보다 위험도가 높은 환자가 없을 때 자신이 진료를 받는 구조
# 현재 N 명의 환자가 대기목록에 있다.
# N 명의 대기목록 순서의 환자 위험도가 주어지면, 대기목록상의 M 번째 환자는 몇 번째로 진료를 받는지 출력
# 대기목록상 M 번쨰는 대기목록의 제일 처음 환자를 0번째로 간주

# 입력설명
# 첫 줄에 자연수 N, M 이 주어진다.
# 두 번째 줄에 접수한 순서대로 환자의 위험도가 주어진다.
# 위험도는 값이 높을수록 더 위험하고 같은값이 존재 가능
# 5 2
# 60 50 70 80 90

# 출력설명
# M 번째 환자의 몇번쨰로 진료받는지를 출력
# 3

# 내 풀이
n, m = map(int, input().split())
paList = list(map(int, input().split()))
for i in range(len(paList)):
    paList[i] = [i, paList[i]]

res = 0
while True:
    max = paList.pop()
    for i in range(1, len(paList)):
        if paList[i][1] > max[1]:
            paList.append(max)
            break
    else:
        res+=1
        if max[0] == m:
            print(res)
            break

# 해설
from collections import deque
n, m = map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break
print(cnt)