

class MoveDetection():

    def detect(self, hands_pred, legs_pred):
        if hands_pred == "Up" or legs_pred == "Not straight":
            model_state = "Moving"

        elif hands_pred == "Down" and legs_pred == "Straight":
            model_state = "Still"

        else:
            model_state = "Not recognized"

        return model_state