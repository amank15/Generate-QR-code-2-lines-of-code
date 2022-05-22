


import qrcode

img=qrcode.make('https://www.linkedin.com/in/amank15/')
img.save('Linkedin_qr.jpg')

import cv2
detect = cv2.QRCodeDetector()
val,point, straight_qrcode = detect.detectAndDecode(cv2.imread("Linkedin_qr.jpg"))
print(val)