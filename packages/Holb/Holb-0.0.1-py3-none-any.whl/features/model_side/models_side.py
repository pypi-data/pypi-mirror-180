import mediapipe as mp


MP_POSE = mp.solutions.pose


class ModelSideDetection():

    def detect(self, results, head_visibility):

        try:
            landmarks = results.pose_landmarks.landmark

            
            left_foot = landmarks[MP_POSE.PoseLandmark.LEFT_FOOT_INDEX.value].z
            right_foot = landmarks[MP_POSE.PoseLandmark.RIGHT_FOOT_INDEX.value].z

            depth = abs(left_foot - right_foot)

            if depth < 0.35 and head_visibility != "Not recognized":
                return "Front"
            
            elif depth > 0.35 and left_foot > right_foot:
                return "Right"

            elif depth > 0.35 and left_foot < right_foot:
                return "Left"

            else:
                return "Back"
        except:
            if head_visibility == "Not recognized":
                return "Back"

            else:
                return "Front"



                
