# 공주 구하기 (큐 자료구조로 해결)
# 정보 왕국의 이웃나라 외동딸 공주가 숲속의 괴물에게 잡혀갔다. 정보 왕국에는 왕자가 N명이 있는데 서로 공주를 구하러 가겠다고 한다. 
# 정보 왕국의 왕은 다음과 같은 방법으로 공주를 구하러 갈 왕자를 결정하기로 했다.
# 왕은 왕자들을 나이순으로 1 ~ N 까지 차례로 번호를 매긴다. 그리고 1번부터 N번 왕자까지 순서대로 시계 방향으로 돌아가며 동그랗게 앉게 한다.
# 그리고 1번 왕자부터 시계 방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다.
# 한 왕자가 K 를 외치면 그 왕자는 공주를 구하러 가는데서 제외되고 원밖으로 나오게 된다. 그리고 다음왕자부터 다시 1부터 시작하여 번호를 외친다.
# 이렇게 해서 마지막 남은 왕자가 공주를 구하러 갈 수 있다.

# 예를 들어 8명의 왕자가 있고, 3을 외친 왕자가 제외된다고 하자. 
# 처음에는 3번 왕자가 3을 외쳐 제외된다. 이어 6, 1, 5, 2, 8, 4번 왕자가 차례대로 제외되고 
# 마지막까지 남게 된 7번 왕자에게 공주를 구하러 간다.
# N 과 K 가 주어질 때 공주를 구하러 갈 왕자의 번호를 출력하는 프로그램

# 입력설명
# 첫 줄에 자연수 N(5 ~ 1,000), K(2 ~ 9) 가 주어진다.
# 8 3

# 출력설명
# 첫 줄에 마지막 남은 왕자의 번호를 출력한다.
# 7 

# 내 풀이
n, k = map(int, input().split())
prince = list()
for i in range(n):
    prince.append(i+1)

count = 0
while len(prince) > 1:
    prince.append(prince.pop(0))
    count+=1
    if count == k:
        prince.pop()
        count=0
print(prince[0])

# 해설
from collections import deque
n, k=map(int, input().split())
dq=list(range(1,n+1))
dq=deque(dq)
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()
