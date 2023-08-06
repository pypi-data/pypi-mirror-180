import cv2
import dlib
import pandas as pd

from imutils import face_utils


class LandmarkDetection():
    def __init__(self, detector = None, predictor = None):
        self._detector = dlib.get_frontal_face_detector() if detector==None else detector
        self._predictor = dlib.shape_predictor('features/models/shape_predictor_68_face_landmarks.dat') if predictor==None else predictor


    def shape(self, image):
        shape = []
        
        image = cv2.imread(image)

        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        rects = self._detector(img, 1)

        for rect in rects:
            shape = self._predictor(img, rect)
            shape = face_utils.shape_to_np(shape)

        return shape
