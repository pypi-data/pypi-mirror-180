import mediapipe as mp

from features.pose_estimation.estimation import CalculateDistances

MP_POSE = mp.solutions.pose

class HandDetection():
    def __init__(self):
        self.calcualte_distance = CalculateDistances()

    def detect(self, results):

        try:
            landmarks = results.pose_landmarks.landmark

            right_hip = [landmarks[MP_POSE.PoseLandmark.RIGHT_HIP.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_HIP.value].y]

            right_shoulder = [landmarks[MP_POSE.PoseLandmark.RIGHT_SHOULDER.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_SHOULDER.value].y]

            right_elbow = [landmarks[MP_POSE.PoseLandmark.RIGHT_ELBOW.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_ELBOW.value].y]

            left_hip = [landmarks[MP_POSE.PoseLandmark.LEFT_HIP.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_HIP.value].y]

            left_shoulder = [landmarks[MP_POSE.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_SHOULDER.value].y]

            left_elbow = [landmarks[MP_POSE.PoseLandmark.LEFT_ELBOW.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_ELBOW.value].y]

            ang_right = self.calcualte_distance.calculate_angle(right_hip, right_shoulder, right_elbow)
            ang_left = self.calcualte_distance.calculate_angle(left_hip, left_shoulder, left_elbow)

            if (ang_left < 75) and (ang_right < 75):
                return "Down"

            else:
                return "Up"

        except:
            return "Not recognized"

