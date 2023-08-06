import cv2
import numpy as np

import mediapipe as mp

MP_POSE = mp.solutions.pose


class CalculateDistances():

    def dist_xy(self, point1, point2):
        """ Euclidean distance between two points point1, point2 """
        diff_point1 = (point1[0] - point2[0]) ** 2
        diff_point2 = (point1[1] - point2[1]) ** 2
        return (diff_point1 + diff_point2) ** 0.5

    def calculate_angle(self, a, b, c):
        '''Calculate an angle beetween two vectors
        Params:
            a (list) - coordinates x, y
            b (list) - coordinates x, y
            c (list) - coordinates x, y
        Returns:
            Calculated angle
        '''
        a = np.array(a) 
        b = np.array(b) 
        c = np.array(c) 
        
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
        
        if angle >180.0:
            angle = 360-angle
            
        return angle


class CalculatePoseLandmarks():
    def pose_landmarks(self, frame):
            with MP_POSE.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                image = cv2.imread(frame)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                results = pose.process(image)

                image.flags.writeable = True

                return results
