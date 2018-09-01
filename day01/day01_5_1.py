# 원문자열은 수정되지 않음!
a = "hello python."


# capitalize
print(a.capitalize())   # 첫문자만 대문자로
print(a)


#                   Python 중앙처리
print(a.center(60))         # 중앙정렬 처리
print(a.center(60, "*"))    # 앞뒤로 문자열 붙이기


# count : 문자열안에 있는 문자의 갯수 출력
print(a.count("p"))


# startswith : 첫문자의 시작단어 확인
print(a.startswith(""))
print(a.startswith("he"))

# endswith : 맨단어의 확인
print(a.endswith('python.'))


# upper 대문자
print(a.upper())
print(a.upper().isupper())
print(a.isupper())


# lower 소문자
print(a.lower())
print(a.lower().islower())
print(a.islower())

# strip 앞뒤 공백 제거
a = "         ㅁㅇㅁㄴㅇㅁㄴ     "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = "         ㅁㅇㅁㄴ    ㅇㅁㄴ     "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = "********^^^**ㅁㅇㅁㄴ***&&*****"
print(a.strip("*"))
print(a.lstrip("*"))
print(a.rstrip("*"))

print(a.strip("*^&"))
print(a.lstrip("*^"))
print(a.rstrip("*^"))

print(a.strip(".*[*|^|&]"))
print(a.lstrip(".*[*|^]"))
print(a.rstrip(".*[*|^]"))

# 채우기
a = "1"
print(a.zfill(10))  # 나머지를 0으로 채워줌

a = "11051"
print(a.zfill(10))  # 나머지를 0으로 채워줌

# 포매팅을 활용하여 채우기
a = "11051"
print("{:*>10}".format(a))  # lpad
print("{:&>10}".format(a))  # lpad
print("{:*<10}".format(a))  # rpad
print("{: <10}".format(a))  # rpad


# replace (대체될 문자열, 대체할문자열)
a = "Hello <Origin>, <Destination>"
print(a.replace('<Origin>', '소명섭'))

a = "Hello <Origin> <Origin>, <Destination>"
print(a.replace('<Origin>', '소명섭'))
print(a.replace('<Origin>', '소명섭', 1))  # 바꿀횟수 지정
print(a.replace('<Origin>', '소명섭', 2))  # 바꿀횟수 지정
print(a.replace('<Origin>', '소명섭', 3))  # 바꿀횟수 지정
print(a.replace('<Origin>', '소명섭', 0))  # 바꿀횟수 지정 (안바뀜)


# find  문자가 몇번째에서 시작하는지
a = "Hello Python"
print(a.find("Python"))      # 왼쪽에서 찾기
print(a.rfind("Python"))     # 오른쪽에서 찾기
print(a.rfind("python"))     # 못찾을 경우 -1 리턴

print(a.index("Python"))      #
# print(a.rindex("python"))     # 예외발생



# is메서드들 중
a = "1"
print(a.isdecimal())    # 10진수인지 판단 (아라비아 숫자기반)
print(a.isdigit())      # 숫자인지 판단   (유니코드기반으로 숫자판별)

a = "\N{KHAROSHTHI DIGIT ONE}"
print(a)
print("\N{KHAROSHTHI DIGIT TWO}")
print("\N{KHAROSHTHI DIGIT THREE}".isdigit())       # True
print("\N{KHAROSHTHI DIGIT THREE}".isdecimal())     # False


# 키보드상 입력하기 힘든 문자 -> 유니코드로
print("\N{WON SIGN}")
print("\N{DOLLAR SIGN}")
print("\N{EURO SIGN}")

print("\uAC00")
print("\uAC01")
print("\uAC02")


# 인코딩  나라별 다름 (한국 : ksc5601, iso-2022-kr, cp949(ms), euc-kr, utf-8
# utf-8 / utf-16le
# 기본적으로 파이썬은 유니코드로 저장됨

a = "한글"
print(a.encode('utf-8'))   # 인코딩 : 바이트문자열로 반환됨
print(a.encode('utf-8').decode('utf-8'))   # 디코딩


# 바이트문자열  저장 및 데이터를 송신할 때
a = a.encode('utf-8')
print(type(a))
b = b'aaaadgggasdadas'
c = bytes()
print(b.find(b"g"))
print(c)


