import cv2
import dlib
import numpy as np
from imutils import face_utils

from features.face_direction.utils import REPROJECTSRC, OBJECT_PTS, CAM_MATRIX, DIST_COEFFS



class CalcualteDirection():

    def get_head_pose(self, shape):
        image_pts = np.float32([shape[17], shape[21], shape[22], shape[26], shape[36],
                                shape[39], shape[42], shape[45], shape[31], shape[35],
                                shape[48], shape[54], shape[57], shape[8]])

        _, rotation_vec, translation_vec = cv2.solvePnP(OBJECT_PTS, image_pts, CAM_MATRIX, DIST_COEFFS)

        reprojectdst, _ = cv2.projectPoints(REPROJECTSRC, rotation_vec, translation_vec, CAM_MATRIX,
                                            DIST_COEFFS)

        reprojectdst = tuple(map(tuple, reprojectdst.reshape(8, 2)))

        # calc euler angle
        rotation_mat, _ = cv2.Rodrigues(rotation_vec)
        pose_mat = cv2.hconcat((rotation_mat, translation_vec))
        _, _, _, _, _, _, euler_angle = cv2.decomposeProjectionMatrix(pose_mat)

        return reprojectdst, euler_angle

    def check_angles(self, x,z):
        if (-30 < x < 30) and (-30 < z < 30):
            return "Camera"

        else:
            return "Sideways"


    def detect(self, shape):

        if len(shape) == 0:
            return "Missing"

        reprojectdst, euler_angle = self.get_head_pose(shape)
        prediction = self.check_angles(euler_angle[0, 0], euler_angle[2, 0])

        return prediction

