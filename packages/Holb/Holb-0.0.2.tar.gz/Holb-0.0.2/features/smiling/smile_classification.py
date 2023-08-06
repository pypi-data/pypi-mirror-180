import pickle


class SmileCLassification():
    def __init__(self):
        file_smile = "features/models/svm_for_smile.sav"
        self.model_smile = pickle.load(open(file_smile, 'rb'))


    def detect(self, shape):

        if len(shape) == 0:
            return  "Not recognized"

        min_x = shape.min(axis=0)[0]
        max_x = shape.max(axis=0)[0]
        max_y = shape.max(axis=0)[1]
        min_y = shape.min(axis=0)[1]
        
        x = []
        y = []

        for i, (a, b) in enumerate(shape):
            if i in range(48,68):
                x_i = abs(min_x- a) / abs(max_x - min_x)
                y_i = abs(min_y- b) / abs(max_y - min_y)
                x.append(x_i)
                y.append(y_i)

        X_test = x + y
        y_pred = self.model_smile.predict_proba([X_test])
        y = y_pred[:,1]
        smile_pred = y >= 0.5
        smile_pred = "Smile" if int(smile_pred) == 1 else "No smile"

        return smile_pred