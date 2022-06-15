# 최대점수 구하기(냅색 알고리즘)

# 이번 정보 올림피아드 대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 풀려고 한다.
# 각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 된다. 제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 한다.
# (해당 문제는 해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있다.)

# 입력설명
# 첫번째 줄에 문제의 개수N(1<=N<=100)과 제한시간 M(10<=M<=1000)이 주어진다.
# 두번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어진다.
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4

# 출력설명
# 첫번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력한다.
# 41

# 내풀이
n, m = map(int, input().split())
dy = [0]*(m+1)

for i in range(n):
    s, t = map(int, input().split())
    for j in range(m, t-1, -1):
        dy[j] = max(dy[j], dy[j-t]+s)
            
print(dy)
print(dy[m])

# 해설
if __name__ == "__main__":
    n, m = map(int, input().split())
    dy=[0]*(m+1)
    for i in range(n):
        ps, pt = map(int, input().split())
        for j in range(m, pt-1, -1):
            dy[j]=max(dy[j], dy[j-pt]+ps)
    print(dy[m])
