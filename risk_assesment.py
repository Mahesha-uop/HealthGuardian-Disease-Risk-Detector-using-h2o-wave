from h2o_wave import Q, app, ui, main
import h2o

choices_pick = [
    ui.choice('A', 'Lung Cancer'),
    ui.choice('B', 'Cardiovascular Disease'),
    ui.choice('C', 'Diabetes'),
]

# Initialize h2o
h2o.init()

# Define the Predict_Diabetes class
class Predict_Diabetes:
    def __init__(self):
        """
        Creates an instance of the recommender system after loading the data.
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
predictor = Predict_Diabetes()


# Main page
@app('/health_guardian')
async def serve(q: Q):
    if q.args.show_input:
            del q.page['example']
            del q.page['example1']
            del q.page['example2']
            del q.page['example3']
            del q.page['header']
            del q.page['CVD']
            del q.page['Diabetes']
            del q.page['Lung_Cancer']
            #  Store the values entered in text boxes in a list
            input_values = [
                q.args.textbox1 if q.args.textbox1 != '' else 0,
                q.args.textbox2 if q.args.textbox2 != '' else 0,
                q.args.textbox3 if q.args.textbox3 != '' else 0,
                q.args.textbox4 if q.args.textbox4 != '' else 0,
                q.args.textbox5 if q.args.textbox5 != '' else 0,
                q.args.textbox6 if q.args.textbox6 != '' else 0,
                q.args.textbox7 if q.args.textbox7 != '' else 0,
                q.args.textbox8 if q.args.textbox8 != '' else 0
            ]
            print(input_values)
            # Get prediction using the predictor object
            prediction = predictor.predict(input_values)#  Store the values entered in text boxes in a list
            q.page['example2'] = ui.form_card(box='1 3 4 7', items=[
                ui.text(f'textbox1={q.args.textbox}'),
                ui.text_l(content=f'Prediction: {prediction}')  # Display prediction
            ])
            
            
    else:
        if q.args.diabetes:

                    del q.page['Diabetes']
                    q.page['example'] = ui.form_card(box='1 3 4 7', items=[
                            # ui.dropdown(name='dropdown', label='Pick one', value='B', required=True, choices=choices),
                            ui.textbox(name='textbox1', label='Input Number of times Pregnencies (if a male put zero)', value=q.args.input1),
                            ui.textbox(name='textbox2', label='Input Glocose Level', value=q.args.input2),
                            ui.textbox(name='textbox3', label='Input Blood Pressure', value=q.args.input3),
                            ui.textbox(name='textbox4', label='Input Skin Thickness', value=q.args.input4),
                            ui.textbox(name='textbox5', label='Input Insulin', value=q.args.input5),
                            ui.textbox(name='textbox6', label='Input BMI', value=q.args.input6),
                            ui.textbox(name='textbox7', label='Input Diabetes Pedigree Function Value', value=q.args.input7),
                            ui.textbox(name='textbox8', label='Input Age', value=q.args.input8),
                            ui.button(name='show_input', label='Submit', primary=True),
                        ])
        else: 
            # Welcome message
            q.page['header'] = ui.header_card(
                box='1 1 8 1',
                title='HealthGuardian: Disease Risk Detector',
                subtitle='Welcome!',
            )

            # Cards for diseases
            q.page['Lung_Cancer'] = ui.tall_info_card(
                box='1 3 2 4',
                name='Lung_Cancer',
                title='Lung Cancer',
                caption='You can assess your risks from your medical records and habits.',
                category='Risk Prediction',
                image='https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
            )

            q.page['CVD'] = ui.tall_info_card(
                box='3 3 2 4',
                name='CVD',
                title='Cardiovascular Disease',
                caption='You can assess your risks from your medical records and habits.',
                category='Risk Prediction',
                image='https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
            )

            q.page['Diabetes'] = ui.tall_info_card(
                box='5 3 2 4',
                name='Diabetes',
                title='Diabetes',
                caption='You can assess your risks from your medical records and habits.',
                category='Risk Prediction',
                image='https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
            
            )
            q.page['example'] = ui.form_card(box='7 3 2 1', items=[
                ui.text_l(content='Risk Assesment Form'),
                ui.text(content='Click the disease type'),
                ],
            )
            q.page['example1'] = ui.form_card(box='7 4 2 1', items=[
                ui.button(
                    name="lung_can",
                    label="Lung Cancer",
                    primary=False,
                ),
                ],
            )

            q.page['example2'] = ui.form_card(box='7 5 2 1', items=[
                ui.button(
                    name="diabetes",
                    label="Diabetes",
                    primary=True,
                ),
                ],
            )
            q.page['example3'] = ui.form_card(box='7 6 2 1', items=[
                ui.button(
                    name="CVD", 
                    label="Cardiovascular Disease", 
                    primary=False,
                ),
            
                ],
            )

    await q.page.save()


if __name__ == '__main__':
    main('/health_guardian', host='127.0.0.1', port=10101)

