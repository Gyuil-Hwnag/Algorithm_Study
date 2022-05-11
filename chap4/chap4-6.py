# 씨름 선수(그리디)
# 현수는 씨름 감독이다. 현수는 씨름 선수 선발 공고를 냈고, N 명의 지원자가 지원을 했다.
# 현수는 각 지원자의 키와 몸무게 정보를 알고 있다. 현수는 씨름 선수 선발 원칙을 다음과 같이 정했다.
# 다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자만 뽑기로 했다.
# 만약 A 라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A 지원자는 탈락이다.
# 첫째 줄에 씨름 선수로 뽑히는 최대 인원을 출력하라.

# 입력 예제
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60

# 출력 예제
# 3

# 내 풀이
n = int(input())
people = list()
for i in range(n):
    weight, height = map(int, input().split())
    people.append([weight, height])
people.sort(key= lambda x: (x[0], x[1]))
# print(people)

cnt = 0
for x in range(n):
    for y in range(x, n):
        if people[x][0] < people[y][0] and people[x][1] < people[y][1]:
            # print("%d %d : %d %d" %(people[x][0], people[x][1], people[x+1][0], people[x+1][1]))
            break
    else:
        cnt+=1
print(cnt)

# 해설
n = int(input())
body=[]
for i in range(n):
    a, b = map(int, input().split())
    body.append((a,b))
body.sort(reverse=True)
largest = 0
cnt = 0
for x,y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)