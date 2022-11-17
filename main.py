import cv2
import pyrealsense2
from realsense_depth import *
from realsense_camera import *
from mask_rcnn import *
import os

depth_camera = DepthCamera()

counter = 0

while(True):
    ret, depth_frame, color_frame = depth_camera.get_frame()

    # cv2.imshow("Depth Frame", depth_frame)
    cv2.imshow("Color frame ", color_frame)

    outpath = str(counter) + ".jpg"

    cv2.imwrite(outpath, color_frame)

    #DETECTING THE CONES

    # for file in os.listdir('C:/Users/user/Desktop/LiveCamera'):
    #     if file.endswith('.jpg'):
    #         os.remove(file)

    key = cv2.waitKey(1)
    if(key == 27):
        break
    counter += 1





# rs = RealsenseCamera()
# mrcnn = MaskRCNN()
#
# while(True):
#     ret, bgr_frame, depth_frame = rs.get_frame_stream()
#
#     boxes, classes, contours, centers = mrcnn.detect_objects_mask(bgr_frame)
#
#     bgr_frame = mrcnn.draw_object_mask(bgr_frame)
#
#
#     cv2.imshow("Depth Frame", depth_frame)
#     cv2.imshow("BGR Frame", bgr_frame)
#
#     key = cv2.waitKey(1)
#     if(key == 27):
#         break