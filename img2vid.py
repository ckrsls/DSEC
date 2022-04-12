import os
import cv2
import numpy as np

#path = '/zrq/train_images/interlaken_00_c/images/left/rectified/'
path1 = '/zrq/train_events/interlaken_00_c/frame/right/'
path2 = '/zrq/train_images/interlaken_00_c/images/right/ev_inf/'

filelist = os.listdir(path1)
filelist.sort()

fps = 20 #视频每秒20帧
size = (640, 480) #需要转为视频的图片的尺寸
#可以使用cv2.resize()进行修改

video = cv2.VideoWriter("/zrq/RGB_EVENT_right.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)
#视频保存在当前目录下

for item in filelist:
#    if item.endswith('.png'): 
#    #找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item1 = path1 + item
        item2 = path2 + item
        img1 = cv2.imread(item1)
        img2 = cv2.imread(item2)
        img3 = cv2.resize(img2,size)

        img = cv2.addWeighted(img1,0.5,img3,0.5,0)
        video.write(img)

video.release()
cv2.destroyAllWindows()