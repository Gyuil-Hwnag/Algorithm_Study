# 전역변수와 지역(local)변수
# 지역변수 우선 -> 그다음 전역변수

def DFS1():
    cnt=3
    print(cnt)

def DFS2():
    global cnt  # 전역변수를 할당
    if cnt==5:   # 지역변수로 할당시 값을 할당 안하면 에러 발생
        cnt=cnt+1
        print(cnt)

def DFS():
    a[0]=7  # 새로운 리스트 생성이 아닌 a의 리스트의 0 인덱스를 참조
    # a=[7,0] # 이 경우에는 새로운 a라는 지역 리스트가 생성
    # global a  # 밑에 부분에 에러 안발생하게 하려면 선언
    # a = a+[4]   # a = 이므로 a라는 로컬리스트 생성
    print(a)

if __name__ == "__main__":
    cnt=5
    a=[1,2,3]
    print(a)
    DFS1()
    DFS2()
    print(cnt)