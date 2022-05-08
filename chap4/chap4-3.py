# 뮤직비디오 (결정 알고리즘)
# 지니레코드는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다.
# DVD 에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지되어야 한다.
# 순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다. 즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는
# 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야 한다. 또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
# 지니레코드는 이 DVD가 팔릴 것인지 확신할 수 없기 때문에 이 사업에 낭비되는 DVD를 가급적 줄이려고 한다.
# 고민끝에 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기로 했다.
# 이 때 DVD의 크기를 최소로 하려고 한다. 그리고 M개의 DVD는 모두 같은 크기여야 제조원가가 적게들기 때문에 꼭 같은 그리고 해야 한다.
# 첫 번째 줄부터 DVD의 최소 용량 크기를 출력하라.

# 입력
# N: 곡 수, M: CD갯수, 음원의 시간
# 9 3
# 1 2 3 4 5 6 7 8 9

# 출력
# 17

# 내 풀이
n, m = map(int, input().split())
videoList = list(map(int, input().split()))

left = 1
right = sum(videoList)
res = point = (left+right)//2

while left <= right:
    point = (left+right)//2
    count = 1
    sum = 0

    for i in range(n):
        sum += videoList[i]
        if sum > point:
            count+=1
            sum = videoList[i]
        if i == n-1:
            if sum>point:
                count+=1

    if count <= m:
        right = point-1
        res = point
    else:
        left = point+1
    print("%d %d" %(point, count))

print(res)

# 해설
n, m = map(int, input().split())
Music = list(map(int, input().split()))

def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

lt = 1
rt = sum(Music)
res = 0
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)