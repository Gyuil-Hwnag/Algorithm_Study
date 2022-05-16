# 단어 찾기(해쉬)
# 현수는 영어로 시를 쓰는 것을 좋아한다. 현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둔다.
# 이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 한다. 그것을 찾아라

# 입력설명
# 첫줄에는 N이 주어지고, 두번째에는 미리 적어놓은 N개의 단어가 주어지고, 이에 바로 다음줄부터 시에 쓰인 N-1개의 단어가 주어진다.
# 5
# big
# good
# sky
# blue
# mouse
# sky
# hood
# mouse
# big

# 출력설명
# 첫번째 줄에 시에 쓰지 않은 한개의 단어를 출력한다.
# blue

# 내 풀이
n = int(input())
wordList = list()
for i in range(n):
    wordList.append(input())

for j in range(n-1):
    res = input()
    for x in range(len(wordList)):
        if res == wordList[x]:
            wordList.pop(x)
            break
print(wordList[0])

# 해설
n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word] = 1
for i in range(n-1):
    word=input()
    p[word]=0
for key, val in p.items:
    if val == 1:
        print(key)
        break