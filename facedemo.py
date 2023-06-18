import cv2


img = cv2.imread('images.jpeg')

# img = cv2.resize(img, (600,600))
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face = cascade.detectMultiScale(img, 1.1, 4)
print(face)
for x,y,w,h in face:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 2)

cv2.imshow('My Image', img)

cv2.waitKey(0)