import mediapipe as mp
import numpy as np


MP_POSE = mp.solutions.pose


class ShotSizeDetection():

    def detect(self, results, arr):

        top = np.count_nonzero(arr == 1)
        low = np.count_nonzero(arr == 2)
        full = np.count_nonzero(arr == 3)

        try:
            landmarks = results.pose_landmarks.landmark

            head = landmarks[MP_POSE.PoseLandmark.LEFT_EYE_INNER.value].visibility
            left_foot = landmarks[MP_POSE.PoseLandmark.LEFT_FOOT_INDEX.value].visibility
            right_foot = landmarks[MP_POSE.PoseLandmark.RIGHT_FOOT_INDEX.value].visibility

            foot = (left_foot + right_foot) / 2
            if head > 0.9 and foot > 0.9:
                return "Full body"

            elif head > 0.9 and (top > low or full > low):
                return "Top"

            elif foot > 0.4 and (low > 2*top):
                return "Bottom"

            else:
                return "Middle"

        except:
            if (low > 2*top) and (low > 2*full):
                return "Bottom"

            else:
                return "Middle"