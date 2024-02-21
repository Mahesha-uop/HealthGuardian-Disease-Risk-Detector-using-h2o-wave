from h2o_wave import Q, ui, data
from pages.front_page import front_pge,front_cards,back_home

choices_gender = [
    ui.choice('1', 'Male'),
    ui.choice('2', 'Female'),
]

choice = [
    ui.choice('0', 'No'),
    ui.choice('1', 'Yes'),
]
choice1 = [
    ui.choice('1', 'Normal'),
    ui.choice('2', 'Above normal'),
    ui.choice('3', 'Well above normal'),
]

def cvd_plt(q: Q):
    q.page['cvd_plot'] = ui.plot_card(
        box='3 2 6 4',
        title='Effect of factors for Cardiovascular Disease',
        data=data('variable importance',11 , rows = [
            ('Age', 0.142), 
            ('Gender', 0.006),
            ('Height', 0.020),
            ('Weight', 0.043),
            ('Systolic blood pressure', 0.530), 
            ('Diastolic blood pressure', 0.154),
            ('Cholesterol', 0.072),
            ('Glucose', 0.010), 
            ('Alcholic', 0.004),
            ('Smoking', 0.006),
            ('Active', 0.010)
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

def cvd_pred(q: Q,predictor):
    del q.page['example']
    del q.page['example1']
    del q.page['example2']
    del q.page['example3']
    del q.page['CVD']
    del q.page['Diabetes']
    del q.page['Lung_Cancer']
    #  Store the values entered in text boxes in a list
    input_values = [
        q.args.textbox1 if q.args.textbox1 != '' else 25,  
        q.args.dropdown,  
        q.args.textbox2 if q.args.textbox2 != '' else 140,  
        q.args.textbox3 if q.args.textbox3 != '' else 70,
        q.args.textbox4 if q.args.textbox4 != '' else 120,
        q.args.textbox5 if q.args.textbox5 != '' else 80,
        q.args.dropdown1,
        q.args.dropdown2,    
        q.args.dropdown3,
        q.args.dropdown4,  
        q.args.dropdown5,
    ]

    print(input_values)
    # Get prediction using the predictor object
    prediction = predictor.predict(input_values)
    prediction =prediction[0]
    q.page['example2'] = ui.form_card(box='1 3 2 2', items=[
        ui.text_l(content=f'Prediction: {prediction}')  # Display prediction
    ])

    front_pge(q)
    back_home(q)
    cvd_plt(q)
    del q.page['details'] 
    q.page['details_pred'] = ui.form_card(box='1 6 8 2', items=[
        ui.text(content='If prediction is no. You have higher chance of not having Cardiovascular Disease. Keep up your Good habits'),
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
    
def cvd_form(q: Q):
    del q.page['Diabetes']
    del q.page['example1']
    del q.page['example2']
    del q.page['example3']
    front_pge(q)
    del q.page['cvd_plot']
    q.page['example'] = ui.form_card(box='1 3 4 7', items=[
        ui.textbox(name='textbox1', label='Input Age', value=q.args.input8),
        ui.dropdown(name='dropdown', label='Choose Gender', value='2', required=True, choices=choices_gender),
        ui.textbox(name='textbox2', label='Input Height', value=q.args.input1),
        ui.textbox(name='textbox3', label='Input Weight', value=q.args.input2),
        ui.textbox(name='textbox4', label='Input Systolic blood pressure', value=q.args.input3),
        ui.textbox(name='textbox5', label='Input Diastolic blood pressure', value=q.args.input4),
        ui.dropdown(name='dropdown1', label='Choose Cholestrol level', value='1', required=True, choices=choice1),
        ui.dropdown(name='dropdown2', label='Choose Glucose level', value='1', required=True, choices=choice1),
        ui.dropdown(name='dropdown3', label='Are you a smoking person', value='0', required=True, choices=choice),
        ui.dropdown(name='dropdown4', label='Are you a Alchoholic person', value='0', required=True, choices=choice),
        ui.dropdown(name='dropdown5', label='Are you a Active person', value='1', required=True, choices=choice),
        ui.button(name='show_input_cvd', label='Submit', primary=True),
        ])
    q.page['details'] = ui.form_card(box='5 3 4 5', items=[
        ui.text_l(content='About the Form'),
        ui.text(content='Please fill the form considering below informations. If any field is unknown please kept default. We will assume that you are healthy in that unknown factor and values will be assigned automatically according to the world health standards. Try to insert more fields for better prediction'),
        ui.text(content= 'Age | Objective Feature | age | int (days)'),
        ui.text(content='Gender | Objective Feature | gender | categorical code |'),
        ui.text(content='Height | Objective Feature | height | int (cm) |'),
        ui.text(content='Weight | Objective Feature | weight | float (kg) |'),
        ui.text(content='Systolic blood pressure | Examination Feature | ap_hi | int |'),
        ui.text(content='Diastolic blood pressure | Examination Feature | ap_lo | int |'),
        ui.text(content='Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal '),
        ui.text(content= 'Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |'),
        ui.text(content='Smoking | Subjective Feature | smoke | binary |'),
        ui.text(content='Alcohol intake | Subjective Feature | alco | binary |'),
        ui.text(content='Physical activity | Subjective Feature | active | binary |'),
        
        ui.text(content= 'Technology: We have used H2O AutoML algorithms and predictions are based on best performed one.'),
    ])
    back_home(q)

