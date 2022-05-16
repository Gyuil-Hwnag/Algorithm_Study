# 교육과정 설계
# 현수는 1년 과정의 수업계획을 짜야 합니다. 수업중에는 필수과목이 있습니다. 이 필수과목은 반드시 이수해야 하며, 그 순서도 정해져 있다.
# 만약 총 과목이 A, B, C, D, E, F, G 가 있고, 여기서 필수과목이 CBA로 주어지면 필수과목은 C, B, A 과목이며
# 이 순서대로 꼭 수업계획을 짜야 합니다. 여기서 순서란 B 과목은 C 과목을 이수한 후에 들어야 하고, 
# A 과목은 C와 B를 이수한 후에 들어야 한다.
# 현수가 C, B, D, A, G, E 로 수업계획을 짜면 제대로 된 설계지만 C, G, E, A, D, B 순서로 짰다면 잘 못 설계된 수업계획이 된다.
# 수업 계획은 그 순서대로 앞에 수업이 이수되면 다음 수업을 시작한다는 것으로 해석된다.
# 수업계획서상의 각 과목은 무조건 이수된다고 가정한다. 필수과목순서가 주어지면 현수가 짠 N 개의 수업설계가 잘된 것이면 "YES",
# 잘못된 것이면 "NO" 를 출력하는 프로그램

# 입력설명
# 첫줄에 한줄에 필수과목의 순서가 주어진다. 모든 과목은 영어 대문자
# 두번째 줄에는 N, 세번째 줄부터 현수가짠 N 개의 수업설계가 주어진다.
# 수업설계는 같은 과목을 여러번 이수하도록 설계해도 된다.
# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA

# 출력설명
# 수업설계가 잘된 것이면 "YES", 잘못된 것이면 "NO"를 출력
# YES
# NO
# YES

# 내 풀이
from collections import deque
cur = input()
n = int(input())
curList = list()
for i in range(n):
    people = input()
    queue = deque(cur)
    for x in people:
        if x == queue[0]:
            queue.popleft()
            if len(queue) == 0:
                break
    if len(queue) == 0:
        print("%d YES" %(i+1))
    else:
        print("%d NO" %(i+1))


# 해설
from collections import deque
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
             print("#%d NO" %(i+1))