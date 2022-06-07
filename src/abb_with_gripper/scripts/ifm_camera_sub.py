#!/usr/bin/env python3
# coding: utf-8

import rospy
from sensor_msgs.msg import Image as msg_Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import cv2
import math
import sys
import os

class ImageListener:
    def __init__(self):
        self.bridge = CvBridge()
        

    def cm2pix(self, dist, real_length, image_width, cam_fov):
        dist = dist / 10
        return real_length / (2 * math.tan(cam_fov / 2 * math.pi / 180) * dist / image_width)

    def pix2cm(self, dist, pix_length, imgwidth, cam_fov=40):
        dist = dist / 10
        return (2 * math.tan(cam_fov / 2 * math.pi / 180) * dist / imgwidth) * pix_length

    def draw_rect(self, img, centre, a, w, l):
        img_box = img.copy()
        a = np.radians(a)
        c, s = np.cos(a), np.sin(a)
        R = np.matrix('{} {}; {} {}'.format(c, s, -s, c))
        print("R matrix: ", R)

        p1 = [+ w / 2, + l / 2]
        p2 = [- w / 2, + l / 2]
        p3 = [- w / 2, - l / 2]
        p4 = [+ w / 2, - l / 2]
        #print(w,l)
        p1_new = np.dot(p1, R) + centre
        p2_new = np.dot(p2, R) + centre
        p3_new = np.dot(p3, R) + centre
        p4_new = np.dot(p4, R) + centre

        img1 = cv2.line(img, (int(p1_new[0, 0]), int(p1_new[0, 1])), (int(p2_new[0, 0]), int(p2_new[0, 1])),
                        (255, 0, 0),
                        1)
        img1 = cv2.line(img1, (int(p2_new[0, 0]), int(p2_new[0, 1])), (int(p3_new[0, 0]), int(p3_new[0, 1])),
                        (255, 0, 0), 1)
        img1 = cv2.line(img1, (int(p3_new[0, 0]), int(p3_new[0, 1])), (int(p4_new[0, 0]), int(p4_new[0, 1])),
                        (255, 0, 0), 1)
        img1 = cv2.line(img1, (int(p4_new[0, 0]), int(p4_new[0, 1])), (int(p1_new[0, 0]), int(p1_new[0, 1])),
                        (255, 0, 0), 1)
        img1 = cv2.line(img1, (int(p2_new[0, 0]), int(p2_new[0, 1])), (int(p4_new[0, 0]), int(p4_new[0, 1])),
                        (255, 0, 0), 1)
        img1 = cv2.line(img1, (int(p1_new[0, 0]), int(p1_new[0, 1])), (int(p3_new[0, 0]), int(p3_new[0, 1])),
                        (255, 0, 0), 1)

        return img1

    def get_world_cor(self, ix, iy, cent, distance):
        ix = ix / 2
        iy = iy / 2
        box1_x, box1_y = 0, 0
        box2_x, box2_y = 0, 0
        box3_x, box3_y = 0, 0

        no_of_cent = len(cent)
        print(no_of_cent)
        if no_of_cent == 1:
            cent1 = cent[0]
            box1 = ix - cent1[0], iy - cent1[1]
            box1_x = self.pix2cm(distance[0], box1[0], ix)
            box1_y = self.pix2cm(distance[0], box1[1], ix)

            return box1_x, box1_y

        elif no_of_cent == 2:
            cent1 = cent[0]
            box1 = ix - cent1[0], iy - cent1[1]
            box1_x = self.pix2cm(distance[0], box1[0], ix)
            box1_y = self.pix2cm(distance[0], box1[1], ix)

            cent2 = cent[1]
            box2 = ix - cent2[0], iy - cent2[1]
            box2_x = self.pix2cm(distance[1], box2[0], ix)
            box2_y = self.pix2cm(distance[1], box2[1], ix)

            return box1_x, box1_y, box2_x, box2_y

        elif no_of_cent == 3:
            cent1 = cent[0]
            box1 = ix - cent1[0], iy - cent1[1]
            box1_x = self.pix2cm(distance[0], box1[0], ix)
            box1_y = self.pix2cm(distance[0], box1[1], ix)

            cent2 = cent[1]
            box2 = ix - cent2[0], iy - cent2[1]
            box2_x = self.pix2cm(distance[1], box2[0], ix)
            box2_y = self.pix2cm(distance[1], box2[1], ix)

            cent3 = cent[2]
            box3 = ix - cent3[0], iy - cent3[1]
            box3_x = self.pix2cm(distance[2], box3[0], ix)
            box3_y = self.pix2cm(distance[2], box3[1], ix)

            return box1_x, box1_y, box2_x, box2_y, box3_x, box3_y

    def imageDepthCallback(self):
        try:

            image = cv2.imread("/home/dhara/arm_ws/src/abb_with_gripper/scripts/amplitude.png")
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image_blur = cv2.GaussianBlur(image_gray, (5, 5), 1)

            im_dis = np.random.randn(*image.shape)

            image_edge = cv2.Canny(image_blur, 40, 140)

            temp = np.zeros(image.shape, dtype='uint8')
            cont, hier = cv2.findContours(image_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for c in cont:
                m = cv2.moments(c)
                area = float(m['m00'])
                # print(area)
                if area > 1000:
                    # print(area)
                    cv2.drawContours(temp, [c], 0, (255, 255, 255), cv2.FILLED)

            temp = cv2.erode(temp, (5, 5), 300)

            temp1 = np.zeros(temp.shape, dtype='uint8')
            image_dep = cv2.imread("/home/dhara/arm_ws/src/abb_with_gripper/scripts/depth.png")
            length = 39.3
            width = 19.3
            image_width = image.shape[1]
            image_height = image.shape[0]
            # print(image_width)
            temp_gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
            cont1, hier = cv2.findContours(temp_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            center_point = []
            distances = []
            for c1 in cont1:
                m = cv2.moments(c1)
                area = float(m['m00'])
                # print(area)
                if area > 1000:
                    # print(area)
                    cv2.drawContours(temp1, [c1], -1, (255, 255, 255), 1)

                    m = cv2.moments(c1)
                    cx = int(m['m10'] / m['m00'])
                    cy = int(m['m01'] / m['m00'])
                    cv2.circle(temp1, (cx, cy), 5, (0, 0, 255), -1)

                    e = cv2.fitEllipse(c1)
                    (x, y), (MA, ma), angle = cv2.fitEllipse(c1)
                    # print(angle)
                    cv2.ellipse(temp1, e, (0, 255, 0), 2)

                    x1 = int(np.round(cx + e[1][1] / 2 * np.cos((e[2] + 90) * np.pi / 180.0)))
                    y1 = int(np.round(cy + e[1][1] / 2 * np.sin((e[2] + 90) * np.pi / 180.0)))
                    x2 = int(np.round(cx + e[1][1] / 2 * np.cos((e[2] - 90) * np.pi / 180.0)))
                    y2 = int(np.round(cy + e[1][1] / 2 * np.sin((e[2] - 90) * np.pi / 180.0)))
                    cv2.line(temp1, (x1, y1), (x2, y2), (255, 255, 0), 2)

                    cv2.imshow("princi axis", temp1)
                    cv2.waitKey(0)

                    depth_data = im_dis[cx, cy]
                    distances.append(depth_data)
                    # print(depth_data)
                    depth_data = 40

                    pix_l = self.cm2pix(depth_data, length, image_width, 40)
                    pix_w = self.cm2pix(depth_data, width, image_width, 40)
                    print("length: ", pix_l, "width: ", pix_w)

                    final = self.draw_rect(temp1, (cx, cy), angle, pix_w, pix_l)
                    center_point.append((cx, cy))

                    cv2.imshow("princi axis", temp1)
                    cv2.waitKey(0)

                    # print(distances, center_point)
                    coordinates = self.get_world_cor(image_width, image_height, center_point, distances)
                    no_of_boxes = len(center_point)
                    
                    if no_of_boxes == 1:
                        box1_coor = [coordinates[0], coordinates[1], distances[0] / 10]

                        print('Detected 1 box')
                        print("box coordinates", box1_coor)

                    elif no_of_boxes == 2:
                        box1_coor = [coordinates[0], coordinates[1], distances[0] / 10]
                        box2_coor = [coordinates[2], coordinates[3], distances[1] / 10]
                        print('Detected 2 boxes')
                        print("box1 coordinates", box1_coor)
                        print("box2 coordinates",box2_coor)

                    elif no_of_boxes == 3:
                        box1_coor = [coordinates[0], coordinates[1], distances[0] / 10]
                        box2_coor = [coordinates[2], coordinates[3], distances[1] / 10]
                        box3_coor = [coordinates[4], coordinates[5], distances[2] / 10]

                        print('Detected 3 boxes')
                        print("Vertical box coordinates", box1_coor)
                        print("Horizontal UP box coordinates", box2_coor)
                        print("Horizontal Down box coordinates", box3_coor)

        except CvBridgeError as e:
            print(e)
            return


if __name__ == '__main__':
    rospy.init_node("depth_image_processor")
    #topic = '/camera/depth/image_raw'  # check the depth image topic in your Gazebo environmemt and replace this with your
    listener = ImageListener()
    listener.imageDepthCallback()
    #rospy.spin()