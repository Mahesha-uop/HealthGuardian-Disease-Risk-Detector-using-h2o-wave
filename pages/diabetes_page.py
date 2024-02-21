from h2o_wave import Q, ui
from pages.front_page import front_pge,front_cards,back_home

choices_gender = [
    ui.choice('A', 'Male'),
    ui.choice('B', 'Female'),
]

def diabetes_pred(q: Q,predictor):
    del q.page['example']
    del q.page['example1']
    del q.page['example2']
    del q.page['example3']
    del q.page['CVD']
    del q.page['Diabetes']
    del q.page['Lung_Cancer']
    #  Store the values entered in text boxes in a list
    input_values = [
        q.args.dropdown,
        50 if q.args.textbox1 != '' and q.args.dropdown == 'Male' else 100,
        50 if q.args.textbox2 != '' and q.args.dropdown == 'Male' else 100,
        50 if q.args.textbox3 != '' and q.args.dropdown == 'Male' else 110,
        50 if q.args.textbox4 != '' and q.args.dropdown == 'Male' else 120,
        50 if q.args.textbox5 != '' and q.args.dropdown == 'Male' else 100,
        50 if q.args.textbox6 != '' and q.args.dropdown == 'Male' else 100,
        50 if q.args.textbox7 != '' and q.args.dropdown == 'Male' else 100,
        50 if q.args.textbox8 != '' and q.args.dropdown == 'Male' else 100
    ]
    print(input_values[1:])
    # Get prediction using the predictor object
    prediction = predictor.predict(input_values[1:])#  Store the values entered in text boxes in a list
    q.page['example2'] = ui.form_card(box='1 3 4 2', items=[
        ui.text_l(content=f'Prediction: {prediction[0]}')  # Display prediction
    ])
    front_pge(q)
    back_home(q)
    q.page['diabetes_plot'] = ui.tall_info_card(
        box='5 3 2 4',
        name='Lung_Cancer',
        title='Lung Cancer',
        caption='You can assess your risks from your medical records and habits.',
        category='Risk Prediction',
        image='https://drive.google.com/file/d/1cDFPmcmX7MQywQks3IxLMsQmT_AvIWLu/view?usp=sharing',
    )

    
def diabetes_form(q: Q):
    del q.page['Diabetes']
    del q.page['example1']
    del q.page['example2']
    del q.page['example3']
    front_pge(q)
    del q.page['diabetes_plot']
    q.page['example'] = ui.form_card(box='1 3 4 7', items=[
            ui.dropdown(name='dropdown', label='Choose Gender', value='B', required=True, choices=choices_gender),
            ui.textbox(name='textbox1', label='Input Number of times Pregnencies (if a male put zero)', value=q.args.input1),
            ui.textbox(name='textbox2', label='Input Glocose Level', value=q.args.input2),
            ui.textbox(name='textbox3', label='Input Blood Pressure', value=q.args.input3),
            ui.textbox(name='textbox4', label='Input Skin Thickness', value=q.args.input4),
            ui.textbox(name='textbox5', label='Input Insulin', value=q.args.input5),
            ui.textbox(name='textbox6', label='Input BMI', value=q.args.input6),
            ui.textbox(name='textbox7', label='Input Diabetes Pedigree Function Value', value=q.args.input7),
            ui.textbox(name='textbox8', label='Input Age', value=q.args.input8),
            ui.button(name='show_input_diabetes', label='Submit', primary=True),
        ])
    q.page['details'] = ui.form_card(box='5 3 4 7', items=[
            ui.text(content='This is not.....'),
    ])
    back_home(q)