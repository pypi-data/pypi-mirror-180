import cv2
import numpy as np


class GazeDetection():

    def get_gaze_ratio(self, eye_points, landmarks, frame, gray):

        eye_region = landmarks[eye_points]
            
        height, width, _ = frame.shape
        mask = np.zeros((height, width), np.uint8)
        cv2.polylines(mask, [eye_region], True, 255, 2)
        cv2.fillPoly(mask, [eye_region], 255)
        eye = cv2.bitwise_and(gray, gray, mask=mask)

        min_x = np.min(eye_region[:, 0])
        max_x = np.max(eye_region[:, 0])
        min_y = np.min(eye_region[:, 1])
        max_y = np.max(eye_region[:, 1])
        gray_eye = eye[min_y: max_y, min_x: max_x]
        _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)

        height, width = threshold_eye.shape
        left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
        left_side_white = cv2.countNonZero(left_side_threshold)

        right_side_threshold = threshold_eye[0: height, int(width / 2): width]
        right_side_white = cv2.countNonZero(right_side_threshold)

        gaze_ratio = left_side_white / right_side_white
        return gaze_ratio


    def detect(self, image, landmarks):
        
        frame = cv2.imread(image)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        try:
            
            gaze_ratio_left_eye = self.get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks, frame, gray)
            gaze_ratio_right_eye = self.get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks, frame, gray)
            
            gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2
        
            if 0.8 < gaze_ratio < 1.7:
                return "Camera"
            else:
                return "Sideways"

        except:
            return "Not recognized"