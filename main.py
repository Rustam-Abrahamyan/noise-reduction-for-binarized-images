import cv2
import glob

extensions = ["images/*.jpeg", "images/*.jpg", "images/*.png"]

for ext in extensions:
    for file in glob.glob(ext):
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        blur = cv2.GaussianBlur(img, (5,5), 0)
        ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        closing_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, closing_kernel)

        cv2.imshow("Original Image", img)
        cv2.imshow("Noise-Reduced Image", closing)

        cv2.waitKey(0)

cv2.destroyAllWindows()

