# 이분검색
# 임의의 N 개의 숫자가 입력으로 주어진다. N 개의 수를 오름차순으로 정렬한 다음 N 개의 수중 한 개의 수인 M 이 주어지면 
# 이분검색으로 M 이 정렬된 상태에서 몇 번쨰에 있는지 구하는 프로그램

# 입력 예제
# 8 32
# 23 87 65 12 57 32 99 81

# 출력 예제
# 3

# 내 풀이
n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()

count = 0
for i in numList:
    count+=1
    if m == i:
        print(count)
        break
# 이분검색으로 바꾸기
left = 0
right = n-1
while left<=right:
    point = (left+right)//2
    if numList[point] == m:
        print(point+1)
    elif numList[point]>m:
        right = point-1
    else:
        left = point+1


# 해설
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1

