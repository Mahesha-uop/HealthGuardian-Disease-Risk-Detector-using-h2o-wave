import h2o

# Initialize h2o
h2o.init()

# Define the Predict_CVD class
class Predict_CVD:
    def __init__(self):
        """
        Creates an instance for the CVD Prediction after loading the models.
        """
        # Load the model
        path = r'models\CVD.zip'
        self.imported_model = h2o.import_mojo(path)

    def predict(self, input_data):
        column_names = ['age','gender','height','weight','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active']
        input_data = [input_data]
        # Convert input data to H2OFrame
        self.input = h2o.H2OFrame(input_data, column_names=column_names)

        # Make predictions
        predictions = self.imported_model.predict(self.input)

        return predictions


# Create an instance of Predict_CVD
predictor_cvd = Predict_CVD()
