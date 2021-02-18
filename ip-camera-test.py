from urllib.request import urlopen
from cv2 import cv2
import numpy as np

url = "http://admin:Sena14232518@192.168.0.105:80/cgi-bin/snapshot.cgi?"

while True:
    imgResp = urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('Test', img)
    cv2.waitKey(10)
