# 랜선 자르기 (결정 알고리즘)
# 엘리트 학원은 자체적으로 K 개의 랜선을 가지고 있다. 그러나 K 개의 랜선은 길이가 제각각이다.
# 선생님은 랜선을 모두 N 개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K 개의 랜선을 잘라서 만들어야 한다.
# 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두개 잘라내면 20cm 는 버려야 한다. (이미 자른 랜선은 붙힐 수 없다.)
# 편의를 위해 랜선을 자를 때 손실되는 길이는 없다고 가정하며, 기존의 K 개의 랜선으로 N 개의 랜선을 만들 수 없는 경우는 없다고 가정.
# 그리고 자를 때는 항상 cm 단위로 정수길이만큼 자른다고 가정. N 개보다 많이 만드는 것도 N 개를 만드는 것에 포함된다.
# 이 때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램

# 첫째줄에 이미 가진 랜선의 개수 K, 필요한 랜선 개수 N
# 입력 예제
# 첫째줄에 N 개를 만들 수 있는 랜선의 최대 길이를 cm 단위의 정수로 출력
# 4 11
# 802
# 743
# 457
# 539

# 출력 예제
# 200

# 내 풀이
k, n = map(int, input().split())
lan = list()
for i in range(k):
    lan.append(int(input()))
lan.sort()

left = 1
right = lan[k-1]
point = (left+right)//2

while left<=right:
    count = 0
    point = (left+right)//2
    for i in lan:
        count += i//point
    if count >= n:
        left = point+1
    else:
        right = point-1

print(point-1)

# 해설
k,n=map(int, input().split())
Line=[]

def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

res=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
