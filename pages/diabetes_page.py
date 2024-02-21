from h2o_wave import Q, ui, data
from pages.front_page import front_pge,front_cards,back_home

choices_gender = [
    ui.choice('A', 'Male'),
    ui.choice('B', 'Female'),
]

def diabetes_plt(q: Q):
    q.page['diabetes_plot'] = ui.plot_card(
        box='3 2 6 4',
        title='Effect of factors for Diabetes',
        data=data('variable importance',8 , rows = [
            ('Pregnancies', 0.030), 
            ('Glucose', 0.587),
            ('Blood Pressure', 0.009),
            ('Skin Thickness', 0.006),
            ('Insulin', 0.003), 
            ('BMI', 0.161),
            ('Diabetes Pedigree Function', 0.048),
            ('Age', 0.156)
        ]),
        plot=ui.plot([
            ui.mark(
                type='interval', 
                x='=variable',
                y='=importance', y_min=0,
                label='={{intl importance minimum_fraction_digits=2 maximum_fraction_digits=2}}',
                label_offset=0, label_position='middle', label_rotation='-90', label_fill_color='#fff',
                label_font_weight='bold'
            )
        ])
      
    )

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
        q.args.dropdown,  # Store the value of the dropdown directly
        q.args.textbox1 if q.args.textbox1 != '' else 0,    
        q.args.textbox2 if q.args.textbox2 != '' else 85,  
        q.args.textbox3 if q.args.textbox3 != '' else 70,
        q.args.textbox4 if q.args.textbox4 != '' else 20,
        q.args.textbox5 if q.args.textbox5 != '' else 0,
        q.args.textbox6 if q.args.textbox6 != '' else 19,
        q.args.textbox7 if q.args.textbox7 != '' else 0,
        q.args.textbox8 if q.args.textbox8 != '' else 25
    ]

    print(input_values[1:])
    # Get prediction using the predictor object
    prediction = predictor.predict(input_values[1:])
    prediction =prediction[0]
    q.page['example2'] = ui.form_card(box='1 3 2 2', items=[
        ui.text_l(content=f'Prediction: {prediction}')  # Display prediction
    ])

    front_pge(q)
    back_home(q)
    diabtetes_plt(q)
    del q.page['details'] 
    q.page['details_pred'] = ui.form_card(box='1 6 8 2', items=[
        ui.text(content='If prediction is no. You have higher chance of not having Diabetes. Keep up your Good habits'),
        ui.text(content='If prediction is yes. Dont panic. We advice you to  meet the family doctor.'),
        ui.text(content='Look at the plot and identify which area you have to improve for better health. Refer WHO standards'),
        ui.link(
                name="who_btn",
                path="https://www.who.int/",
                label="WHO Standards",
                button=True,
            ),
    ],
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
            ui.textbox(name='textbox1', label='Input Number of times Pregnencies', value=q.args.input1),
            ui.textbox(name='textbox2', label='Input Glocose Level', value=q.args.input2),
            ui.textbox(name='textbox3', label='Input Blood Pressure', value=q.args.input3),
            ui.textbox(name='textbox4', label='Input Skin Thickness', value=q.args.input4),
            ui.textbox(name='textbox5', label='Input Insulin', value=q.args.input5),
            ui.textbox(name='textbox6', label='Input BMI', value=q.args.input6),
            ui.textbox(name='textbox7', label='Input Diabetes Pedigree Function Value', value=q.args.input7),
            ui.textbox(name='textbox8', label='Input Age', value=q.args.input8),
            ui.button(name='show_input_diabetes', label='Submit', primary=True),
        ])
    q.page['details'] = ui.form_card(box='5 3 4 5', items=[
        ui.text_l(content='About the Form'),
        ui.text(content='Please fill the form considering below informations. If any field is unknown please kept blank. We will assume that you are healthy in that unknown factor and values will be assigned automatically according to the world health standards. Try to insert more fields for better prediction'),
        ui.text(content= 'Pregnancies: Number of times pregnant'),
        ui.text(content='BloodPressure: Diastolic blood pressure (mm Hg)'),
        ui.text(content='SkinThickness: Triceps skin fold thickness (mm)'),
        ui.text(content='Insulin: 2-Hour serum insulin (mu U/ml)'),
        ui.text(content='BMI: Body mass index (weight in kg/(height in m)^2)'),
        ui.text(content='DiabetesPedigreeFunction: Diabetes pedigree function'),
        ui.text(content='Age: Age (years)'),
        ui.text(content= 'Technology: We have used H2O AutoML algorithms and predictions are based on best performed one.'),
    ])
    back_home(q)

