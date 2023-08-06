
import mediapipe as mp

from features.pose_estimation.estimation import CalculateDistances


MP_POSE = mp.solutions.pose

class LegDetection():
    def __init__(self):
        self.calcualte_distance = CalculateDistances()

    def detect(self, results):

        try:
            landmarks = results.pose_landmarks.landmark

            right_hip = [landmarks[MP_POSE.PoseLandmark.RIGHT_HIP.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_HIP.value].y]

            right_knee = [landmarks[MP_POSE.PoseLandmark.RIGHT_KNEE.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_KNEE.value].y]

            right_ankle = [landmarks[MP_POSE.PoseLandmark.RIGHT_ANKLE.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_ANKLE.value].y]

            left_hip = [landmarks[MP_POSE.PoseLandmark.LEFT_HIP.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_HIP.value].y]

            left_knee = [landmarks[MP_POSE.PoseLandmark.LEFT_KNEE.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_KNEE.value].y]

            left_ankle = [landmarks[MP_POSE.PoseLandmark.LEFT_ANKLE.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_ANKLE.value].y]

            ang_1 = self.calcualte_distance.calculate_angle(right_hip, right_knee, right_ankle)
            ang_2 = self.calcualte_distance.calculate_angle(left_hip, left_knee, left_ankle)

            if (ang_1 > 160) and (ang_2 > 160):
                return "Straight"

            else:
                return "Not straight"

        except:
            return "Not recognized"
