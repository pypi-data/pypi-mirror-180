import cv2 as cv
import numpy as np
import pickle


class CalculateHistogram():
    def __init__(self):
        file_light = "features/models/fixed_knn_for_lightning_expanded_ranges.sav"
        self.model_light = pickle.load(open(file_light, 'rb'))

    def detect(self, photo):
        max_blue = 0
        max_red = 0
        max_green = 0

        src = cv.imread(photo)

        bgr_planes = cv.split(src)
        histSize = 256

        histRange = (0, 256)
        accumulate = False

        b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
        g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
        r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)

        hist_w = 512
        hist_h = 400
        bin_w = int(round( hist_w/histSize ))

        cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
        cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
        cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

        for i in range(1, histSize):
            if int(b_hist[i]) >= max_blue:
                max_blue = b_hist[i]
                bin_blue = bin_w*(i)

            if int(r_hist[i]) >= max_red:
                max_red = r_hist[i]
                bin_red = bin_w*(i)

            if int(g_hist[i]) >= max_green:
                max_green = g_hist[i]
                bin_green = bin_w*(i)

        map_light = {0 : "Fine", 1 : "Overexposed", 2 : "Underexposed"}

        bin_blue, bin_red, bin_green = bin_blue / 510, bin_red / 510, bin_green / 510

        arr = np.array([[bin_blue, bin_red, bin_green]])

        light_predict = self.model_light.predict(arr)

        return map_light[light_predict[0]]

