import h2o

# Initialize h2o
h2o.init()

# Define the Predict_Lung_Cancer class
class Predict_Lung_Cancer:
    
    def __init__(self):
        """
        Creates an instance for the Lung Cancer Prediction after loading the models.
        """
        # Load the model
        path = r'models\Lung_cancer.zip'
        self.imported_model = h2o.import_mojo(path)

    def predict(self, input_data):
        column_names = ['Age','Gender','Air Pollution','Alcohol use','Dust Allergy','OccuPational Hazards','Genetic Risk','chronic Lung Disease','Balanced Diet','Obesity','Smoking','Passive Smoker','Chest Pain','Coughing of Blood','Fatigue','Weight Loss','Shortness of Breath','Wheezing','Swallowing Difficulty','Clubbing of Finger Nails','Frequent Cold','Dry Cough','Snoring']
        input_data = [input_data]
        # Convert input data to H2OFrame
        self.input = h2o.H2OFrame(input_data, column_names=column_names)

        # Make predictions
        predictions = self.imported_model.predict(self.input)

        return predictions


# Create an instance of Predict_Lung Cancer
predictor_lung_cancer = Predict_Lung_Cancer()
