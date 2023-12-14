import cv2

elec_image = cv2.imread('EV.jpg')
cm_image = cv2.imread('CM.jpg')

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
            Electric +=1
        else:
            notElectric += 1

for y in range(height):
    for x in range(width):
        if commercial_range[y, x] >= 1:
            Commercial +=1
            
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

