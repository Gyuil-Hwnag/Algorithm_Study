# 송아지 찾기(BFS : 상태트리검색)

# 현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 현수의 위치와 송아지의 위치가 직선상의 좌표점으로 주어지면
# 현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.
# 현수는 스카이 콩콩을 타고 가는데 한번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다.
# 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램

# 입력설명
# 첫번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표점은 1부터 10,000 까지이다.
# 5 14

# 출력설명
# 점프의 최소횟수를 구한다.
# 3

# 해설
from collections import deque
MAX = 10000
ch = [0]*(MAX+1)
dis = [0]*(MAX+1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if next == m:
        break
    for next in (now-1, now+1, now+5):
        if 0<next<=MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1

print(dis[m])
