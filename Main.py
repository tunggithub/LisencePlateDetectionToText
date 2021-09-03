import TextRecognize
import YOLOv4_detect
import cv2
import re
import os

imgPath="test1.jpg"
YOLOv4_detect.getLisencePlate(imgPath)

if os.path.exists("predict.txt"):

    with open("predict.txt", 'r') as f:  #
        result=""
        img = cv2.imread(imgPath)
        for line in f.readlines():
            string_list =line.split()
            integer_map = map(int, string_list )
            integer_list = list(integer_map)

            crop_img = img[integer_list[1]:integer_list[3], integer_list[0]:integer_list[2]]

            s=TextRecognize.getLisencePlateText(crop_img)
            result+= re.sub('[^\w\-]', '', s)+"\n"
        with open("out.txt", 'w') as f1:  #
            f1.write(result)