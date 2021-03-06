import imghdr
from re import template
from tempfile import tempdir
from traceback import print_tb
import traceback
from unittest import result
import cv2
import os
from pathlib import PurePath
import random
import numpy as np
import time
from pip import main
import pytesseract
#OpenCV Python zoek overeenstemmend in een opgegevn plaatje.
#ref --> https://youtu.be/T-0lZWYWE9Y?list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn
#20220630

class clsMain:
    def __init__(self) -> None:
        self.img = None
        self.cap = None
        self.scriptFull = PurePath(__file__)
        self.scriptPath = str(PurePath(self.scriptFull.parent))        

    def getOCRedFromImage(self, imgSrc=None, imgTemplateSr=None):
        '''Main routine'''
        intTeller = 0
        print(f'''{intTeller} Probeer demo: {imgSrc}''')

        npUitgeknipt, rect1 = self.getCroppedImageFromTemplate(imgSrc=imgSrc, imgTemplate=imgTemplateSr)

        cv2.imwrite(f'''{self.scriptPath}/out/resultaat_meterTemplateMatch01_rect1.jpg''', rect1)
        try:
            cv2.imshow(f'{intTeller} rect1', rect1)
            cv2.waitKey(2000)
        except Exception as ex1:
            print(traceback.print_exc())

        resultImg = f'''{self.scriptPath}/out/resultaat_meterTemplateMatch01_npUitgeknipt.jpg'''
        cv2.imwrite(f'''{resultImg}''', npUitgeknipt)

        try:
            cv2.imshow(f'{intTeller} npUitgeknipt=versie', npUitgeknipt)
            cv2.waitKey(2000)                
        except Exception as ex1:
            print(traceback.print_exc())

        # ref --> https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/
        resultOCR = pytesseract.image_to_string(image=resultImg, config="--psm 6")

        #ocrStr = pytesseract.image_to_string(resultImg)
        #print(f'''OCRed={ocrStr}''')
        #print("")
        intTeller += 1
        return resultOCR


    def getCroppedImageFromTemplate(self, imgSrc, imgTemplate, debug=False):
        '''getCroppedImageFromTemplate(imgSrc, imgTemplate) -> retval\n.   @brief zoek de desbetreffend beeld in de opgegeven plaatje.  ideaal voor meterstanden uitlezen. @param imgSrc BronplaatjeJPG   @param imgTemplate hetgeen je zoekt in de plaaatje RETURNS: npArray'''
        npimgSrc = cv2.imread(f'''{imgSrc}''', cv2.IMREAD_GRAYSCALE)
        npTemplate1 = cv2.imread(f'''{imgTemplate}''', cv2.IMREAD_GRAYSCALE)

        h, w = npTemplate1.shape   #hoogte is array van element startpunt boven en eindpunt onder, w=start element links, naar rechts.
        #voor shapes, zie turital https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm


        methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
                    cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

        teller0 = 1
        npUitgeknipt = None
        rect1 = None

        try:
            print(f'''Maak een copy van {imgSrc}''')
            npimgSrccopy = npimgSrc.copy()
            method = cv2.TM_CCOEFF_NORMED

            print(f'''Zoek de overeenkomst {imgTemplate} in bron={imgSrc}''')

            matchResult = cv2.matchTemplate(image=npimgSrc, templ=npTemplate1, method=method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchResult)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                location = min_loc
            else:
                location = max_loc

            if(debug):
                print(f'''Overeenstemmend beeld wordt getoond''')
                cv2.imshow(f'matchResult getoond', matchResult)
                cv2.waitKey(2000)

            bottom_right = (location[0] + w, location[1] + h)    
            npUitgeknipt = npimgSrccopy[location[1]:bottom_right[1], location[0]:bottom_right[0]]        
            rect1 = cv2.rectangle(npimgSrccopy, location, bottom_right, 255, thickness=5)
            
        except Exception as ex1:
            print(traceback.print_exc())
        finally:
            cv2.destroyAllWindows()

        return npUitgeknipt, rect1


if __name__ == "__main__":
    print("App start")
    print(f"")
    print(f"SYNOPIS:")
    print(f"Deze code loopt door een dir en probeert meterlezingen/kentekens te detecteren  op basis van een gegeven template en daarin de kentekentekst proberen bepalen.")
    print(f"")

    main1 = clsMain()
    templateMeterstand = f'''{main1.scriptPath}/assets/meterstand_template_leeg.jpg'''
    templateKentekenNLToUse = f'''{main1.scriptPath}/assets/template_kentekenNL01.jpg'''
    templateKentekenNLToUse02 = f'''{main1.scriptPath}/assets/template_kentekenNL02.jpg'''

    try:
        plaatjesArr = [{"imgSrc" : f'''{main1.scriptPath}/assets/meterstand_elektra20220630_test1.jpg''',
                            "imgTemplateSr" : templateMeterstand},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/meterstand_elektra202200704.jpg''',
                            "imgTemplateSr" : templateMeterstand},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/meterstand_elektra20220630_test2.jpg''',
                            "imgTemplateSr" : templateMeterstand},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/meterstand_elektra20220630_test3.jpg''',
                            "imgTemplateSr" : templateMeterstand},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/meterstand_elektra20220630_test3_geenMeting.jpg''',
                            "imgTemplateSr" : templateMeterstand},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/meterstand_elektra20220630_test3_meting_rarePositie.jpg''',
                            "imgTemplateSr" : templateMeterstand},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/meterstand_elektra20220630_test1.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/minicooper1.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/kenteken_borent.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/NL_auto_vooraanzicht03_aygo.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/NL_auto_vooraanzicht03_aygo.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse02},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/kenteken_KL55R2473.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/NL_auto_lancia01.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/NL_auto_lancia01.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse02},

                            {"imgSrc" : f'''{main1.scriptPath}/assets/NL_auto_vooraanzicht03_aygo.jpg''',
                            "imgTemplateSr" : templateKentekenNLToUse02}
                        ]

        ocredKentekens = []

        for item1 in plaatjesArr:
            ocrTxt = main1.getOCRedFromImage(imgSrc=item1["imgSrc"], imgTemplateSr=item1["imgTemplateSr"])
            print("")
            print("")
            ocredKentekens.append(ocrTxt)
            print(f'''ocrTxt={ocrTxt}''')
            print("")
            print("")
        
        print(f"ocredKentekens:\n{ocredKentekens}")

    except Exception as ex1:
        print(traceback.print_exc())
    finally:
        cv2.destroyAllWindows()

    print("App eind")
