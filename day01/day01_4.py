s1 = "Hello Python"  # 한번 만들면 변경 불가능
# s1[0] = 'a' # 변경 불가능 : 에러발생
print(s1[0])
print(s1[1])
print(s1[2])

# slice (커서기준)
print(s1[0:5])      # 0~4까지 문자열 출력 (시작:끝-1)
print(s1[6:12])     # 6~11까지 문자열 출력
print(s1[:])        # 전체 문자열 출력


# 한개씩 건너띄워서 가져오기
print(s1[0:5:2])    # 1개씩 건너띄기
print(s1[6:12:3])   # 2개씩 건너띄기


# 뒤에서 꺼내올때 -기호 활용
print(s1[-1])
print(s1[-4:-1])    # 작은값이 먼저 와야함
print(s1[:5])       # 0은 기본값이므로 생략이 가능함  [0:5]와 동일
print(s1[6:])       # 마지막 값은 정해져 있으므로 생략이 가능함  [6:문자열길이]와 동일
print(s1[:])        # 0과 마지막 생략시 -> 전체문자열 들고옴