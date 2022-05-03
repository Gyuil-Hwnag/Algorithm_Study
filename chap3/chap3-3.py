# 카드 역배치
# 1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓여있다.
# 각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타난다.
# 1,2,3,4,5,...,18,19,20
# 1,2,3,4,5,6,7,8,9,10,...,20
# 이제 여러분은 다음과 같은 규칙으로 카드의 위치를 바꾼다.
# 구간 [a,b] 가 주어지면 a 부터 b까지의 카드를 현재의 역순으로 놓는다.
# 오름차순으로 한줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면,
# 주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤
# 마지막 카드들의 배치를 구하는 프로그램을 작성
# 총 10번의 바꿈

# 내 풀이

card = list()
for i in range(1,21):
    card.append(i)

def reverCard(a, b):
    global card
    a = int(a)
    b = int(b)
    before = card[a-1:b]
    before.reverse()
    for i in range(a-1,b):
        card[i] = before[i-(a-1)]

for i in range(10):
    a, b = input().split()
    reverCard(a, b)
    print(card)

print(card)

# 해설
