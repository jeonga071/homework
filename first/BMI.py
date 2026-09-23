with open("health.txt", "r", encoding="utf-8") as file: #파일 읽기. 인코딩 필요.
    file.readline() # 헤더 부분만 읽음

    data = []

    for line in file:
        data.append(line.strip().split())

print(data)