# 동적계획법이란? 네트워크 선 자르기(Bottom-Up)

# 현수는 네트워크선을 1m, 2m의 길이를 갖는 선으로 자르려고 한다.
# 예를 들어 4m의 네트워크선이 주어진다면
# 1) 1m+1m+1m+1m
# 2) 2m+1m+1m
# 3) 1m+2m+1m
# 4) 1m+1m+2m
# 5) 2m+2m
# 등의 5가지 방법을 생각할 수 있다. 2 와 3 과 4의 경우 
# 왼쪽을 기준으로 자르는 위치가 다르면 다른 경우로 생각한다.
# 그렇다면, 네트워크 선의 길이가 Nm 이라면 몇 가지의 자르는 방법을 생각할 수 있는지

# 입력설명
# 첫째줄에 네트워크선의 총 길이인 자연수 N이 주어진다.
# 21

# 출력설명
# 첫번째 줄에 부분증가수열의 최대길이를 출력한다.
# 7
