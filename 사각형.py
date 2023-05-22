width = 1
height = 1
min_area = 1
max_area = 1
area = 1

area = width * height

while area < 150:

    area = (width*2)*(height*3)
    width +=1
    height+=1

    if min_area > area:
        min_area = area
    elif max_area < area:
        max_area = area
    print("사각형의 넓이",area)

print("작은 사각형넓이",min_area)
print("큰 사각형 넓이",max_area)
