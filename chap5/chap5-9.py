# Anagram(아나그램 : 구글 인터뷰 문제, 딕셔너리 해시)
# Anagram이란 두 문자열이 알바펫의 나열 순서는 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 한다.
# 예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열한 순서는 다르지만 그 구성을 살펴보면 A(2), a(1), C(1), e(2)로
# 알파벳과 그 개수가 모두 일치한다. 즉 어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 한다.
# 길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램. 아나그램 판별시 대소문자가 구분된다.

# 입력설명
# 첫줄에 첫번째 단어가 입력되고, 두번째 줄에 두번째 단어가 입력된다. 단어의 길이는 100을 넘지 않는다.
# AbaAeCe
# baeeACA

# 출력설명
# 두 단어가 아나그램이면 "YES"를 출력하고, 아니면 "NO"를 출력한다.

# 내 풀이
a=input()
b=input()
str=dict()
for x in a:
    str[x]=str.get(x,0)+1
for x in b:
    str[x]=str.get(x)-1
for i in str.values():
    if i != 0:
        print("NO")
        break
else:
    print("YES")

# 해설 방법1
a=input()
b=input()
str1=dict()
str2=dict()
for x in a:
    str1[x] = str1.get(x, 0)+1
for x in b:
    str2[x] = str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys:
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

# 해설 방법2
a=input()
b=input()
str1=[0]*52
str2=[0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1
for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")