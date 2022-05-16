# 최대힙
# 최대힙은 완전 이진트리로 구현된 자료구조이다. 그 구성은 부모 노드값이 왼쪽 자식과 오른쪽 자식노드의 값보다 크게 트리를 구성하는 것.
# 그렇게 하면 트리의 루트노드는 입력된 값들 중 큰 값이 저장되어 진다. 예를 들어 5 3 2 1 4 6 7순으로 입력되면 
# 최대힙 트리는 아래와 같이 구성된다.
#         7
#     4       6
# 1      3 2      5
# 최대힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램
# 1. 자연수가 입력되면 최대힙에 입력한다.
# 2. 숫자 0이 입력되면 최대힙에서 최댓값을 꺼내어 출력한다. (출력할 자료가 없으면 -1을 출력한다.)
# -1 이 입력되면 프로그램을 종료한다.

# 해설
import heapq as hq
a=[]
while True:
    n=int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)