import numpy as np
import matplotlib.pyplot as plt
import cv2
from pathlib import PurePath

# 20220602 ref --> https://programmer.ink/think/opencv-python-tutorial-template-matching.html
#                   https://www.youtube.com/results?search_query=opencv+ocr+and+text+recognition+with+tesseract+


if __name__ == "__main__":
    print("App start")
    print("")
    scriptFull = PurePath(__file__)
    scriptPath = str(PurePath(scriptFull.parent))
    plaatjeSrc = f'''{scriptPath}/meterstand_elektra20220429.jpg'''
    templateSrc = f'''{scriptPath}/meterstand_template.jpg'''

    #Read in the image and take the screenshot as the template image
    print('VX official account: Orange code / juzicode.com')
    print('cv2.__version__:',cv2.__version__)
    plt.rc('font',family='Youyuan',size='9')
    plt.rc('axes',unicode_minus='False')
    img_src = cv2.imread(plaatjeSrc) 
    img_templ = cv2.imread(templateSrc) 
    print('img_src.shape:',img_src.shape)
    print('img_templ.shape:',img_templ.shape)

    for method in range(6):
        #template matching
        result = cv2.matchTemplate(img_src, img_templ, method)
        print('result.shape:',result.shape)
        print('result.dtype:',result.dtype)
        #Calculate matching position
        min_max = cv2.minMaxLoc(result)
        if method == 0 or method == 1:   #According to different patterns, the best matching location has different methods
            match_loc = min_max[2]
        else:
            match_loc = min_max[3]      
        #Note that when calculating the coordinates of the lower right corner, the width represented by the template image shape[1] shall be added to the x coordinate and the height shall be added to the y coordinate
        right_bottom = (match_loc[0] + img_templ.shape[1], match_loc[1] + img_templ.shape[0])
        print('result.min_max:',min_max)
        print('match_loc:',match_loc)
        print('right_bottom',right_bottom)
        #marking position 
        img_disp = img_src.copy()
        cv2.rectangle(img_disp, match_loc,right_bottom, (0,255,0), 5, 8, 0 )
        cv2.normalize( result, result, 0, 255, cv2.NORM_MINMAX, -1 )
        cv2.circle(result, match_loc, 10, (255,0,0), 2 )

        cv2.imshow(f'''Resultaat: method {method}''', result)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

        #Display image
        fig,ax = plt.subplots(2,2)
        fig.suptitle('Method=%d'%method)
        ax[0,0].set_title('img_src')
        ax[0,0].imshow(cv2.cvtColor(img_src,cv2.COLOR_BGR2RGB)) 
        ax[0,1].set_title('img_templ')
        ax[0,1].imshow(cv2.cvtColor(img_templ,cv2.COLOR_BGR2RGB)) 
        ax[1,0].set_title('result')
        ax[1,0].imshow(result,'gray') 
        ax[1,1].set_title('img_disp')
        ax[1,1].imshow(cv2.cvtColor(img_disp,cv2.COLOR_BGR2RGB)) 
        #ax[0,0].axis('off');ax[0,1].axis('off');ax[1,0].axis('off');ax[1,1].axis('off')
        plt.show()   

    print("")
    print("App eind")
