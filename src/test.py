
import cv2

im = cv2.imread('..\\assets\\processed_image_steps\\1_processed_img_format.tiff')

th, im_th = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

th, im_th_tz = cv2.threshold(im, 128, 255, cv2.THRESH_TOZERO)


im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

cv2.imwrite('..\\assets\\processed_image_steps\\3-processed_img_binar.tiff', im_gray_th_otsu)
