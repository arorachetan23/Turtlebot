import cv2
from glob import glob
import os


i=0
my_dirc='final_data/robot1/' 
for filename in os.listdir(my_dirc): 
    dst ="1_" + str(i) + ".png"
    src =my_dirc+ filename 
    dst =my_dirc+ dst 
      
    # rename() function will 
    # rename all the files 
    #print(src)
    os.rename(src, dst) 
    i += 1
print("done")
#for i in glob('fianl_data/robot1/*png'):
#img=cv2.imread('processed_data/test1.png')
#print(img.shape)
# cv2.imshow("ss",img)
# cv2.waitKey(0)