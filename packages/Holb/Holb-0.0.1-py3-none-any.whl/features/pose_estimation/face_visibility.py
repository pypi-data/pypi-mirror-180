import mediapipe as mp

MP_POSE = mp.solutions.pose

class FaceVisibility(): 

    def detect(self, results, smile):
            if smile != "Not recognized":
                return "Visible"

            try:
                landmarks = results.pose_landmarks.landmark

                left_eye_inner = [landmarks[MP_POSE.PoseLandmark.LEFT_EYE_INNER.value].x,
                    landmarks[MP_POSE.PoseLandmark.LEFT_EYE_INNER.value].y]

                right_eye_inner = [landmarks[MP_POSE.PoseLandmark.RIGHT_EYE_INNER.value].x,
                    landmarks[MP_POSE.PoseLandmark.RIGHT_EYE_INNER.value].y]

                left_wrist = [landmarks[MP_POSE.PoseLandmark.LEFT_WRIST.value].x,
                    landmarks[MP_POSE.PoseLandmark.LEFT_WRIST.value].y]

                right_wrist = [landmarks[MP_POSE.PoseLandmark.RIGHT_WRIST.value].x,
                    landmarks[MP_POSE.PoseLandmark.RIGHT_WRIST.value].y]

                dist_leye_lwrist = self.dist_xy(left_eye_inner, left_wrist)

                dist_leye_rwrist = self.dist_xy(left_eye_inner, right_wrist)

                dist_reye_lwrist = self.dist_xy(right_eye_inner, left_wrist)

                dist_reye_rwrist = self.dist_xy(right_eye_inner, right_wrist)

                if min(dist_leye_lwrist, dist_leye_rwrist, dist_reye_lwrist, dist_reye_rwrist) < 0.2:
                    return "Hidden"

                else:
                    return "Not recognized"

            except:
                return "Not recognized"
