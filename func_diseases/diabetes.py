import h2o

# Initialize h2o
h2o.init()

# Define the Predict_Diabetes class
class Predict_Diabetes:
    def __init__(self):
        """
        Creates an instance for the Diabetes after loading the models.
        """
        # Load the model
        path = r'models\Diabetes.zip'
        self.imported_model = h2o.import_mojo(path)

    def predict(self, input_data):
        column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        
        # Convert input data to H2OFrame
        self.input = h2o.H2OFrame(input_data, column_names=column_names)

        # Make predictions
        predictions = self.imported_model.predict(self.input)

        return predictions


# Create an instance of Predict_Diabetes
predictor_diabetes = Predict_Diabetes()
