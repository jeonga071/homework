import turtle

screen = turtle.Screen() #터틀 스크린 생성
screen.setup(1000, 600)
screen.title("BMI 표")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

#시작 지점 및 칸의 넓이 설정
start_x = -400
start_y = 200

cell_w = 140
cell_h = 40

rows = [] #전체 데이터

headers = ["전화번호", "이름", "키(cm)", "몸무게(kg)", "BMI", "소견"]
with open("health.txt", "r", encoding="utf-8") as file: #파일 읽기. 인코딩 필요.
    file.readline() # 헤더 부분만 읽음

    data = []

    for line in file:
        data.append(line.strip().split()) #데이터 원본

def get_bmi(cm: int, kg:int) -> float:
    bmi = kg / (cm/100) ** 2
    return bmi

def bmi_category(bmi: float) -> str:
    if bmi <= 18.5:
        return "저체중"
    elif bmi <= 24.5:
        return "정상"
    elif bmi <= 30:
        return "과체중"
    else:
        return "비만"

def data_to_rows(data):  #rows에 데이터 추가
    for i in data:
        number = i[0]
        name = i[1]
        cm = int(i[2])
        kg = int(i[3])
        bmi = get_bmi(cm, kg)
        category = bmi_category(bmi)
        rows.append([number, name, cm, kg, round(bmi, 1), category])

def draw_cell(x, y, w, h, text): #칸 그리기
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.penup()

    t.goto(x + 10, y + 10)
    t.write(text, font=("Arial", 10, "normal"))

def draw_text(): 
    data_to_rows(data)
    for i, text in enumerate(headers):  # 헤더 생성
        x = start_x + i * cell_w
        draw_cell(x, start_y, cell_w, cell_h, text)


    for r_idx, row in enumerate(rows):
        y = start_y - (r_idx + 1) * cell_h
        for c_idx, text in enumerate(row):
            x = start_x + c_idx * cell_w
            draw_cell(x, y, cell_w, cell_h, text)

if __name__ == "__main__" :
    draw_text()

screen.mainloop()