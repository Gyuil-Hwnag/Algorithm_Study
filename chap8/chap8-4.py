# 도전과제 : 돌다리 건너기(Bottom-Up)

# 철수는 학교에 가는데 개울을 만났다. 개울은 N개의 돌로 다리를 만들어 놓았다.
# 철수는 돌다리를 건널 때 한번에 한칸 또는 두칸씩 건너뛰면서 돌다리를 건널 수 있다.
# 철수가 개울을 건너는 방법은 몇가지 인지?

# 입력설명
# 첫째줄에 계단의 개수 N이 주어진다.
# 7

# 출력설며
# 첫번째 줄에 올라가는 방법의 수를 출력한다.
# 21

# 내풀이
n = int(input())
dy = [0]*(n+1)
dy[1]=1
dy[2]=2

def DFS(L):
    if L > n:
        return 0
    elif L==n:
        return dy[L]
    else:
        if dy[L]>0:
            return dy[L]
        else:
            dy[L] = dy[L-1]+dy[L-2]
            return DFS(L+1)+DFS(L+2)

print(DFS(3))
print(dy)