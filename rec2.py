import cv2
import pytesseract
import numpy as np

def detect_number_plate(image, vehicle_box):
    number_plate_region = image[vehicle_box[1]:vehicle_box[3], vehicle_box[0]:vehicle_box[2]]
    return number_plate_region

def detect_color(image):
    yellow = np.array([20, 100, 100])
    blue = np.array([130, 255, 255])
    mask_yellow = cv2.inRange(image, yellow, yellow)
    mask_blue = cv2.inRange(image, blue, blue)
    
    if np.sum(mask_yellow) > np.sum(mask_blue):
        return 'yellow'
    else:
        return 'blue'

elec_image = cv2.imread('EV.jpg')
cm_image = cv2.imread('CM.jpg')

# Resize elec_image to match the size of cm_image
elec_image = cv2.resize(elec_image, (cm_image.shape[1], cm_image.shape[0]))

combined_image = cv2.hconcat([elec_image, cm_image])
cv2.imshow('Combined Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(combined_image, cv2.COLOR_BGR2GRAY)

elec_range = cv2.inRange(combined_image, (50, 10, 170), (200, 230, 255))
cv2.imshow('electronic_license_plate', elec_range)
cv2.waitKey(0)
cv2.destroyAllWindows()

commercial_range = cv2.inRange(combined_image, (20, 100, 100), (30, 255, 255))
cv2.imshow('commercial_vehicle', commercial_range)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)

height, width = elec_range.shape[:2]

Electric = 0
notElectric = 0
Commercial = 0

for y in range(height):
    for x in range(width):
        if elec_range[y, x] >= 1:
            Electric += 1
        else:
            notElectric += 1

for y in range(height):
    for x in range(width):
        if commercial_range[y, x] >= 1:
            Commercial += 1
            
print("Electric", Electric)
print("notElectric", notElectric)
print("Commercial", Commercial)

if 10 * Electric >= notElectric:
    print("전기 자동차입니다.")
else:
    print("전기 자동차가 아닙니다.")

if Commercial >= 1000:
    print("영업용 자동차입니다.")
else:
    print("영업용 자동차가 아닙니다.")

# Define the coordinates for the vehicle box in the combined image
# Adjust these values based on the specific location of the vehicle in the combined image
x_min = int(width * 0.2)  # Starting x-coordinate of the region of interest
y_min = int(height * 0.4)  # Starting y-coordinate of the region of interest
x_max = int(width * 0.8)  # Ending x-coordinate of the region of interest
y_max = int(height * 0.8)  # Ending y-coordinate of the region of interest

image_path = 'https://github.com/Trippyle/OSS_TermProject/assets/143789666/9f416508-43d6-4a60-a624-588dc4602b1c.jpg'
image = cv2.imread(image_path)

number_plate_region = detect_number_plate(combined_image, vehicle_box=(x_min, y_min, x_max, y_max))

number_plate_text = pytesseract.image_to_string(number_plate_region)

hsv_plate = cv2.cvtColor(number_plate_region, cv2.COLOR_BGR2HSV)
color_detected = detect_color(hsv_plate)

if color_detected == 'yellow':
    vehicle_type = 'bus or taxi'
elif color_detected == 'blue':
    vehicle_type = 'electric cars'
else:
    vehicle_type = 'normal cars'

print("번호판:", number_plate_text)
print("차량 유형:", vehicle_type)

cv2.imshow('번호판', number_plate_region)
cv2.waitKey(0)
cv2.destroyAllWindows()

