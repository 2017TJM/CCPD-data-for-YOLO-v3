import cv2
import os, sys
path =r"D:\baiduyundownloads\CCPD_2019(1)\CCPD2019\ccpd_base"

path_='data/voc/VOCdevkit/VOC2019/JPEGImages'
lable=0
item=0
list_image=[]
for img_name in os.listdir(path):
    print(img_name)
    # 读取图片的完整名字
    # image = cv2.imread(path + "/" + img_name)

    # 以 - 为分隔符，将图片名切分，其中iname[4]为车牌字符，iname[2]为车牌坐标
    iname = img_name.rsplit('/', 1)[-1].rsplit('.', 1)[0].split('-')
    tempName = iname[4].split("_")
    # name = provinces[int(tempName[0])] + alphabets[int(tempName[1])] + ads[int(tempName[2])] \
    #        + ads[int(tempName[3])] + ads[int(tempName[4])] + ads[int(tempName[5])] + ads[int(tempName[6])]

    # crop车牌的左上角和右下角坐标
    item=item+1
    print(item)
    [leftUp, rightDown] = [[int(eel) for eel in el.split('&')] for el in iname[2].split('_')]
    list_image.append(path_ + '/' + img_name + ' ' +str(leftUp[0])+' ' +str(leftUp[1])+' ' +str(rightDown[0])+' ' +str(rightDown[1])+ ' '+str(lable) + '\n')  # 在文件名后加标签



txt = open('val.txt', 'w+')  # 准备写入
txt.writelines(list_image)
txt.close()



