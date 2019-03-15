
import numpy as np
import cv2


def edgedetect(channel):
  # sobelX = cv2.Sobel(channel, cv2.CV_16S, 1, 0, ksize=1)
  # sobelY = cv2.Sobel(channel, cv2.CV_16S, 0, 1, ksize=1)
  # sobel = np.hypot(sobelX, sobelY)
  sobel = channel
  # Some values seem to go above 255. However RGB channels has to be within 0-255
  sobel[sobel > 255] = 255
  sobel[sobel < 25] = 0
  return sobel


img = cv2.imread('sample.jpg')
blurred = cv2.GaussianBlur(img, (25, 25), 0)  # Remove noise
kernel = np.ones((4, 4), np.uint8)
blurred = cv2.erode(blurred, kernel, iterations=2)
blurred = cv2.bilateralFilter(blurred,9,75,75)
opening = cv2.morphologyEx(blurred, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,20)))
blurred = opening
blurred = cv2.medianBlur(img,25)


edgeImg = np.max(np.array([edgedetect(blurred[:, :, 0]), edgedetect(blurred[:, :, 1]), edgedetect(blurred[:, :, 2])]), axis=0)
# Open and close the image
edgeImg = cv2.erode(edgeImg, kernel*2, iterations=1)
edgeImg = cv2.morphologyEx(edgeImg, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2)))
edgeImg[edgeImg>0]=255

_, thresh = cv2.threshold(edgeImg, 100, 255, cv2.THRESH_BINARY) # Optimize this
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

try: hierarchy = hierarchy[0]
except: hierarchy = []

height, width, _ = img.shape
min_x, min_y = width, height
max_x = max_y = 0
particles = []

# computes the bounding box for the contour, and draws it on the frame,
for contour, hier in zip(contours, hierarchy):
    (x,y,w,h) = cv2.boundingRect(contour)
    min_x, max_x = min(x, min_x), max(x+w, max_x)
    min_y, max_y = min(y, min_y), max(y+h, max_y)
    # if w > 80 and h > 80:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0, 0, 255), 2)
    particles.append((w, h))

for i in sorted(particles):
  print(i)

cv2.imshow('orig', img)
# cv2.imshow('blurred', blurred)
cv2.imshow('image', thresh)
if cv2.waitKey(0) & 0xFF:
  cv2.destroyAllWindows()
