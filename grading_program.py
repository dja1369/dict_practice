#사전형을 공부하기 위한 코드
student_scores = {
    "재석": 81,
    "명수": 78,
    "세호": 99,
    "하하": 74,
    "준하": 62,
}
#빈사전형 생성하기
student_grades = {}
#반복문을 이용하여 입력받기, values 그 자체는 키값만을 가져오기에 사전형 student_scores 에 키값으로 반복문 변수 [values]를 넣어줌
#이를 빈사전형[반복변수] = 새데이터 형식으로 선언하면 키: 밸류 구조로 되어있는 사전형의 값을 바꿀수 있음
for values in student_scores:
    score = student_scores[values]
    if score > 90:
        student_grades[score] = "A"
    elif score > 80:
        student_grades[score] = "B"
    elif score > 70:
        student_grades[score] = "C"
    else:
        student_grades[score] = "F"


print(student_scores)





