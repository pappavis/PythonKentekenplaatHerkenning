import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
import os
import socket
import time
from pathlib import PurePath
import traceback

class clsKentekenHerkenning:
  def __init__(self):
      self.__grayImg = None
      self.kentekenText = None
      self.__edged = None
      self.__detected = False
      self.__img = None
      self.scriptFull = PurePath(__file__)
      self.scriptPath = str(PurePath(self.scriptFull.parent))

  def main(self, bronJPG="minicooper1.jpg"):
    cwd = os.getcwd()
    ocv1 = None
    self.__img = None
    logTxt = None

    if(socket.gethostname().startswith("NL00617")):
      ocv1 = "opencv_uitprobeer"

    bronJPG = os.path.join(self.scriptPath, bronJPG)

    print(f'bronbestand={bronJPG}')
    self.__img =cv2.imread(bronJPG,cv2.IMREAD_COLOR)  
    self.__img =cv2.resize(self.__img, (620,480) )

    self.__grayImg = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY) #convert to grey scale
    logTxt = "1. grayscale -- druk een toets"
    print(logTxt)
    try:
      cv2.imshow(logTxt, self.__grayImg)
      cv2.waitKey(3000)        
    except Exception as ex1:
        print(traceback.print_exc())
    finally:
        cv2.destroyAllWindows()

    self.__grayImg = cv2.bilateralFilter(self.__grayImg, 11, 17, 17) #Blur to reduce noise
    logTxt = "2 Blur to reduce noise"
    print(logTxt)
    cv2.imshow(logTxt, self.__grayImg)
    cv2.waitKey(3000)        


    self.__edged = cv2.Canny(self.__grayImg, 30, 200) #Perform Edge detection
    logTxt = f'''3 Perform Edge detection'''
    print(logTxt)
    cv2.imshow(logTxt, self.__edged)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    # find contours in the edged image, keep only the largest
    # ones, and initialize our screen contour
    logTxt = 'findContours'
    print(logTxt)
    cnts = cv2.findContours(self.__edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None
  
  #
    # loop over our contours
    logTxt = f'''loop over our contours'''
    print(logTxt)
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
      cont1 = cv2.drawContours(self.__img, [screenCnt], -1, (0, 255, 0), 3)

      logTxt = f'''drawContours'''
      print(logTxt)
      try:
        cv2.imshow(logTxt, cont1)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
      except Exception as ex1:
          print(traceback.print_exc())
      finally:
          cv2.destroyAllWindows()

    # Masking the part other than the number plate
    mask = np.zeros(self.__grayImg.shape,np.uint8)
    logTxt = f'''mask'''
    print(logTxt)
    try:
      cv2.imshow(logTxt, mask)
      cv2.waitKey(3000)
      cv2.destroyAllWindows()
    except Exception as ex1:
        print(traceback.print_exc())
    finally:
        cv2.destroyAllWindows()

    new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
    new_image = cv2.bitwise_and(self.__img, self.__img, mask=mask)

    logTxt = f'''new_image -- alleen het kenteken'''
    print(logTxt)
    cv2.imshow(logTxt, new_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    # Now crop
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = self.__grayImg[topx:bottomx+1, topy:bottomy+1]
    logTxt = f'''Cropped -- alleen het kenteken'''
    print(logTxt)
    cv2.imshow(logTxt, Cropped)
 
    #Read the number plate
    self.kentekenText = pytesseract.image_to_string(Cropped, config='--psm 11')
    logTxt = f"De herkende kenteken is: {self.kentekenText}"
    print(logTxt)

    logTxt = f'toon image'
    print(logTxt)
    try:        
      cv2.imshow('image',self.__img)
      cv2.waitKey(3000)
    except Exception as ex1:
        print(traceback.print_exc())
    finally:
        cv2.destroyAllWindows()
    logTxt = f'toon cropped'
    print(logTxt)    
    try:
      cv2.imshow(logTxt, Cropped)
      cv2.waitKey(3000)
    except Exception as ex1:
        print(traceback.print_exc())
    finally:
        cv2.destroyAllWindows()

    print("Wachten 5 seconden..")
    time.sleep(5)
    cv2.destroyAllWindows()

  @property
  def edgedImg(self):
    return self.__edged


  def getCroppedImageFromTemplate(self, imgSrc, imgTemplate):
    '''getCroppedImageFromTemplate(imgSrc, imgTemplate) -> retval\n.   @brief zoek de desbetreffend beeld in de opgegeven plaatje.  ideaal voor meterstanden uitlezen. @param imgSrc BronplaatjeJPG   @param imgTemplate hetgeen je zoekt in de plaaatje RETURNS: npArray'''
    npImgSrc1 = cv2.imread(f'''{imgSrc}''', cv2.IMREAD_GRAYSCALE)
    npTemplate1 = cv2.imread(f'''{imgTemplate}''', cv2.IMREAD_GRAYSCALE)

    h, w = npTemplate1.shape   #hoogte is array van element startpunt boven en eindpunt onder, w=start element links, naar rechts.
    #voor shapes, zie turital https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm


    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
                cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    teller0 = 1
    npUitgeknipt = None

    try:
        npImgSrc1copy = npImgSrc1.copy()
        method = cv2.TM_CCOEFF_NORMED

        print(f'''proberen template te matchen met method {method}''')

        matchResult = cv2.matchTemplate(image=npImgSrc1, templ=npTemplate1, method=method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchResult)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        cv2.imshow(f'result method={method}', matchResult)
        cv2.waitKey(2000)

        bottom_right = (location[0] + w, location[1] + h)    
        npUitgeknipt = npImgSrc1copy[location[1]:bottom_right[1], location[0]:bottom_right[0]]            
        cv2.rectangle(npImgSrc1copy, location, bottom_right, 255, thickness=5)

    except Exception as ex1:
        print(traceback.print_exc())
    finally:
        cv2.destroyAllWindows()

    return npUitgeknipt

  
if __name__=='__main__':
  # CREDITS: https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv
  print("App start")
  kenteken1 = clsKentekenHerkenning()
  kenteken1.main(bronJPG="assets/minicooper1.jpg")
  print("App eind")
