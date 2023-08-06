import mediapipe as mp

from features.pose_estimation.estimation import CalculateDistances


MP_POSE = mp.solutions.pose

class PostureDetection():
    def __init__(self):
        self.calcualte_distance = CalculateDistances()


    def detect(self, results):
        try:
            landmarks = results.pose_landmarks.landmark

            right_shoulder = [landmarks[MP_POSE.PoseLandmark.RIGHT_SHOULDER.value].x,
                            landmarks[MP_POSE.PoseLandmark.RIGHT_SHOULDER.value].y]

            right_hip = [landmarks[MP_POSE.PoseLandmark.RIGHT_HIP.value].x,
                        landmarks[MP_POSE.PoseLandmark.RIGHT_HIP.value].y]

            right_knee = [landmarks[MP_POSE.PoseLandmark.RIGHT_KNEE.value].x,
                        landmarks[MP_POSE.PoseLandmark.RIGHT_KNEE.value].y]

            hip_angle = self.calcualte_distance.calculate_angle(right_shoulder, right_hip, right_knee)

            return "Sitting" if (10 < hip_angle < 140) else "Straight"     

        except:

            return "Straight" 

