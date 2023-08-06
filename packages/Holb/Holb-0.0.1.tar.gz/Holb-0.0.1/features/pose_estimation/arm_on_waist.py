import mediapipe as mp

from features.pose_estimation.estimation import CalculateDistances

MP_POSE = mp.solutions.pose


class ArmDetection():
    def __init__(self):
        self.calcualte_distance = CalculateDistances()

    def detect(self, results):

        try:
            landmarks = results.pose_landmarks.landmark

            right_shoulder = [landmarks[MP_POSE.PoseLandmark.RIGHT_SHOULDER.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_SHOULDER.value].y]

            right_elbow = [landmarks[MP_POSE.PoseLandmark.RIGHT_ELBOW.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_ELBOW.value].y]

            right_wrist = [landmarks[MP_POSE.PoseLandmark.RIGHT_WRIST.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_WRIST.value].y]

            left_shoulds = [landmarks[MP_POSE.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_SHOULDER.value].y]

            left_elbow = [landmarks[MP_POSE.PoseLandmark.LEFT_ELBOW.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_ELBOW.value].y]

            left_wrist = [landmarks[MP_POSE.PoseLandmark.LEFT_WRIST.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_WRIST.value].y]

            right_index = [landmarks[MP_POSE.PoseLandmark.RIGHT_INDEX.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_INDEX.value].y]

            left_index = [landmarks[MP_POSE.PoseLandmark.LEFT_INDEX.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_INDEX.value].y]

            right_hip = [landmarks[MP_POSE.PoseLandmark.RIGHT_HIP.value].x,
                landmarks[MP_POSE.PoseLandmark.RIGHT_HIP.value].y]

            left_hip = [landmarks[MP_POSE.PoseLandmark.LEFT_HIP.value].x,
                landmarks[MP_POSE.PoseLandmark.LEFT_HIP.value].y]

            dist_right = self.calcualte_distance.dist_xy(right_index, right_hip)
            dist_left = self.calcualte_distance.dist_xy(left_index, left_hip)
            
            ang_right = self.calcualte_distance.calculate_angle(right_shoulder, right_elbow, right_wrist)
            ang_left = self.calcualte_distance.calculate_angle(left_shoulds, left_elbow, left_wrist)

            if ((20 < ang_right < 140) and dist_right < 0.2) or ((20 < ang_left < 140) and dist_left < 0.2):
                return "Rests on waist"

            else:
                return "Doesn't rest"
        
        except:
            return "Not recognized"



