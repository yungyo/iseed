age = int(input("나이를 입력하세요 : "))
result = ''

if age < 20 :
    result = '청소년 할인'
elif age >= 60 :
    result = '경로 우대'
else :
    result = '무혜택'
