import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
import os
import socket
import time

class clsKentekenHerkenning:
  def __init__(self):
      self.__img = None
      self.__grayImg = None
      self.kentekenText = None
      self.__edged = None
      self.__detected = False

  def main(self, bronJPG1=None):
    cwd = os.getcwd()
    ocv1 = None

    if(socket.gethostname().startswith("NL00617")):
      ocv1 = "opencv_uitprobeer"

    if(bronJPG1 is None):
      bronJPG1 = os.path.join(cwd, ocv1, "PythonKentekenplaatHerkenning", "kenteken_borent.jpg")

    print(f'bronbestand={bronJPG1}')
    self.__img =cv2.imread(bronJPG1,cv2.IMREAD_COLOR)  
    self.__img =cv2.resize(self.__img, (620,480) )

    self.__grayImg = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY) #convert to grey scale
    self.__grayImg = cv2.bilateralFilter(self.__grayImg, 11, 17, 17) #Blur to reduce noise
    self.__edged = cv2.Canny(self.__grayImg, 30, 200) #Perform Edge detection

    # find contours in the edged image, keep only the largest
    # ones, and initialize our screen contour
    cnts = cv2.findContours(self.__edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None
  #
    # loop over our contours
  # loop over our contours
    for c in cnts:
      # approximate the contour
      peri = cv2.arcLength(c, True)
      approx = cv2.approxPolyDP(c, 0.018 * peri, True)
      # if our approximated contour has four points, then
      # we can assume that we have found our screen
      if len(approx) == 4:
        screenCnt = approx
        break

    if(screenCnt is None):
      print("No contour detected")
    else:
      self.__detected = True

    if(self.__detected):
      cv2.drawContours(self.__img, [screenCnt], -1, (0, 255, 0), 3)

    # Masking the part other than the number plate
    mask = np.zeros(self.__grayImg.shape,np.uint8)
    new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
    new_image = cv2.bitwise_and(self.__img, self.__img, mask=mask)

    # Now crop
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = self.__grayImg[topx:bottomx+1, topy:bottomy+1]

    #Read the number plate
    self.kentekenText = pytesseract.image_to_string(Cropped, config='--psm 11')
    print("De herkende kenteken is: ", self.kentekenText)

    cv2.imshow('image',self.__img)
    cv2.imshow('Cropped', Cropped)

    print("Wachten 5 seconden..")
    time.sleep(5)
    cv2.destroyAllWindows()

  @property
  def edgedImg(self):
    return self.__edged

if __name__=='__main__':
  # CREDITS: https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv
  print("App start")
  kenteken1 = clsKentekenHerkenning()
  kenteken1.main()
  print("App eind")
