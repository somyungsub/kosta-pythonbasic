# 문자열
s = "Hello Python"      # 방식 1  더블쿼테이션
s1 = 'Hello Python'     # 방식 2  싱글쿼테이션

# 방식이 2가지 인 이유 는 문자열 안에 " 내용이 들어갈 경우를 대비 or ' 내용이 들어갈 경우 -> 이스케이프 문자처리의 편리성을 제공
s2 = 'Hello\' Python'   # 문자열 '를 이스케이프 처리
s3 = 'Hello\" Python'   # 문자열 "를 이스케이프 처리

s5 = str()  # 빈문자열로 초기화
print(s5)

s6 = "jfijaijiajdiajdilll!!!!" \
     "adjajdkasasdj" \
     "adadasdas" \
     "adasdasdasdad" \
     "adasdasdada" \
     "adasdasdasdas" \
     "adad" \
     "adasdas" \
     "adasda" \
     "!!!!------------=========="
print(s6)


s7 = "aadadasdadjiajiadsda" \
     "adadasdas" \
     "dadadasd" \
     "adadadas" \
     "dadasda" \
     "ddddd"
print(s7)

# 보기 좋은 방식
s8 = ("ahduahdajasddjadada"
      "adadadasdasda"
      "asdasdasas"
      "dasdasda"
      "asddadada"
      "ddddddd"
      "dddd")
print(s8)

# 여러줄 입력 -> 여러줄 출력 (문자 그대로로 인식함) -> ''' 3개입력
s9 = '''aadsadasdasdasdasdasda     ㅁ엄ㄴ엄ㄴ어    ㅁ언머인마ㅓㅇ미


adaasdasdasdasdasdas
dadasdasdasdasd
dadasdasdsadadas
dadasdasdasdasdasdasda
'''
print(s9)

# 문서화 문자열 (변수에 입력안되는 경우) 주석으로도 활용됨
'''
     여러줄 주석으로 활용 할 수 있음
     여러줄 주석으로 활용 할 수 있음
     여러줄 주석으로 활용 할 수 있음
'''