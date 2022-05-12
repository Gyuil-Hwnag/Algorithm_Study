# 회의실 배정(그리디 <- 대부분 정렬로 하기)
# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들려고 한다. 
# 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라.
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

# 입력 설명
# 첫째 줄에 회의의 수 n 이 주어진다. 둘째 줄부터 n+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# 최대 사용할 수 있는 회의 수를 출력
# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7

# 출력
# 3

# 내 풀이
n = int(input())
meeting = list()
for i in range(n):
    start, end = map(int, input().split())
    meeting.append([start, end])
meeting.sort(key= lambda x: (x[1], x[0]))
endTime = 0
res = 0
for s, e in meeting:
    if s>=endTime:
        endTime = e
        res += 1
print(res)


# 해설
n=int(input())
meeting = []
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x: (x[1], x[0]))
et=0
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)