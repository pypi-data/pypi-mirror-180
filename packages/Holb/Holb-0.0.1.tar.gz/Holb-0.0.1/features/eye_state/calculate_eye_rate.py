from scipy.spatial import distance as dist
from imutils import face_utils


(LSTART, LEND) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(RSTART, REND) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


class EyeRate():
    def eye_aspect_ratio(self, eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])

        C = dist.euclidean(eye[0], eye[3])
        
        ear = (A + B) / (2.0 * C)
        
        return ear


    def detect(self, shape):

        if len(shape) == 0:
            return "Missing"

        leftEye = shape[LSTART:LEND]
        rightEye = shape[RSTART:REND]

        leftEAR = self.eye_aspect_ratio(leftEye)
        rightEAR = self.eye_aspect_ratio(rightEye)

        ear_coefficient = (leftEAR + rightEAR) / 2.0

        eye_state_pred = "Open" if ear_coefficient > 0.23 else "Closed"

        return eye_state_pred
