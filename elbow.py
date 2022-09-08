import cv2
import time
import numpy as np
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)
pTime = 0
count = 0
dir = 0


mpDraw = mp.solutions.drawing_utils
mPose = mp.solutions.pose
pose = mPose.Pose()

def findAngle(img, p1, p2, p3, draw=True):
    x1, y1 = lmList[p1][1:]
    x2, y2 = lmList[p2][1:]
    x3, y3 = lmList[p3][1:]

    angle = math.degrees(math.atan2(y3-y1,x3-x2)-
                         math.atan2(y1-y2,x1-x2))
    if angle <0:
        angle +=360

    print(angle)

    if draw:
        cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)
        cv2.line(img,(x2,y2),(x3,y3),(255,255,255),3)
        cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x1, y1), 10, (255, 0, 0), 2)
        cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), 2)
        cv2.circle(img, (x3, y3), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x3, y3), 10, (255, 0, 0), 2)
        cv2.putText(img,str(int(angle)),(x2-20,y2+50),cv2.FONT_ITALIC,1,(255,68,35),3)
    return angle


angle_1=angle_2=angle_3 =0
angle_list = {}
angle_list["l_elbow"] = [11,13,15]
angle_list["r_elbow"] = [12,14,16]
angle_list["ls_angle"] = [13,11,23]
angle_list["rs_angle"] = [14,12,24]
angle_list["rh_angle"] = [12,24,26]
angle_list["lh_angle"] = [11,23,25]
angle_list["rk_angle"] = [24,26,28]
angle_list["lk_angle"] = [23,25,27]

prim_list = [angle_list["l_elbow"],angle_list["r_elbow"],angle_list["ls_angle"],angle_list["rs_angle"],angle_list["rh_angle"],angle_list["lh_angle"] ,angle_list["rk_angle"],angle_list["lk_angle"]]

print(prim_list)
print("Select an angle to capture")
print("1.Left Elbow Angle\n2.Right Elbow Angle\n3.Left Shoulder Angle\n4.Right Shoulder Angle\n5.Right Hip Angle\n6.Left Hip Angle\n7.Right Knee Angle\n8.Left Knee Angle")

choice = int(input("\nEnter a choice"))

angle_1 = prim_list[choice-1][0]
angle_2 = prim_list[choice-1][1]
angle_3 = prim_list[choice-1][2]

print(angle_1,angle_2,angle_3)




while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    lmList = []
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            # print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            lmList.append([id, cx, cy])
            # print(lmList)
        if len(lmList) !=0:
            angle = findAngle(img,angle_1,angle_2,angle_3,draw=True) #FOR LEFT HAND
            per = np.interp(angle,(20,160),(0,100)) #MAXIMUM AND MINIMUM
            print(str(int(angle)),per)

            if per == 100:
                if dir ==0:
                    count +=0.5
                    dir = 1
            if per == 0:
                if dir ==1:
                    count +=0.5
                    dir = 0

            print(count)
            cv2.putText(img,f'n:{str(count)}',(450,50),cv2.FONT_ITALIC,2,(34,45,34),5)

            # x1, y1 = lmList[12][1:]
            # print(x1,y1)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,40),cv2.FONT_ITALIC,2,(255,0,0),2)



    cv2.imshow('video',img)
    cv2.waitKey(1)
