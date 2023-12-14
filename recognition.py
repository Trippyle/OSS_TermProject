import cv2
import pytesseract
import numpy

def detect_number_plate(image, vehicle_box):
    
def detect_color(image):
    

image_path = 'https://github.com/Trippyle/OSS_TermProject/assets/143789666/9f416508-43d6-4a60-a624-588dc4602b1c.jpg'
image = cv2.imread(image_path)

#번호판 찾기
number_plate_region = detect_number_plate(image)

#번호판 인식
number_plate_text = pytesseract.image_to_string(number_plate_region)

# 색상 감지
hsv_plate = cv2.cvtColor(number_plate_region, cv2.COLOR_BGR2HSV)
yellow = numpy.array([20, 100, 100])
blue = numpy.array([130, 255, 255])
mask = cv2.inRange(hsv_plate, yellow, blue)

# 차량 분류
if 'yellow' in detect_color(mask):
    vehicle_type = 'bus or taxi'
elif 'blue' in detect_color(mask):
    vehicle_type = 'electric cars'
else:
    vehicle_type = 'normal cars'

print("번호판:", number_plate_text)
print("차량 유형:", vehicle_type)

# 걸과 출력
cv2.imshow('번호판', number_plate_region)
cv2.imshow('색상 마스크', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
