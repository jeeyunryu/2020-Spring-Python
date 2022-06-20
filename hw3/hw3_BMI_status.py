cm_height = float(input("키 입력: "))
weight = float(input("몸무게 입력: "))

m_height = cm_height * 1/100

bmi = int(10 *  (weight /  m_height**2))/10


if bmi < 18.5:
    status = "저체중"
elif bmi < 25.0:
    status = "정상"
elif bmi < 30.0:
    status = "과체중"
else:
    status = "비만"
print("BMI수치는 {:.1f} 이며, {:s} 입니다." .format(bmi, status))

