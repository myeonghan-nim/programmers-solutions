# 환자 코드의 마지막 네 글자(code[-4:])를 병과 표에서 찾고, 표에 없으면 "direct recommendation"을 출력한다
departments = {"_eye": "Ophthalmologyc", "head": "Neurosurgery", "infl": "Orthopedics", "skin": "Dermatology"}
print(departments.get(input()[-4:], "direct recommendation"))
