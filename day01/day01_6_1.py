
# split
a = 'a-b-c-d-e-f-g'
print(a.split("-"))             # 리스트로
print(",".join(a.split("-")))   # 리스트 -> 문자열로 합치기
print("".join(a.split("-")))   # 리스트 -> 문자열로 합치기
print(a)