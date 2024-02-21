from h2o_wave import Q, ui, data
from pages.front_page import front_pge,front_cards,back_home,footer

choices_gender = [
    ui.choice('1', 'Male'),
    ui.choice('2', 'Female'),
]

choice_level = [
    ui.choice('1', '1'),
    ui.choice('2', '2'),
    ui.choice('3', '3'),
    ui.choice('4', '4'),
    ui.choice('5', '5'),
    ui.choice('6', '6'),
    ui.choice('7', '7'),
    ui.choice('8', '8'),
    ui.choice('9', '9'),
    
]

def lc_plt(q: Q):
    ''' Plot Effecting factors for Lung Cancer'''
    q.page['lc_plot'] = ui.plot_card(
        box='3 2 6 4',
        title='Effect of factors for Lung Cancer - Top 10', 
        data=data('variable importance',10 , rows = [
            ('Passive Smoker' ,0.155), 
            ('Wheezing',0.135),
            ('Alcohol use',0.093),
            ('Dust Allergy',0.072),
            ('Fatigue',0.071), 
            ('Snoring',0.067),
            ('Obesity',0.066),
            ('Smoking',0.045),
            ('Chest Pain',0.040),
            ('Frequent Cold',0.037)
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

def lc_pred(q: Q,predictor):
    ''' Prediction page for Lung Cancer'''
    del q.page['example']
    del q.page['example1']
    del q.page['example2']
    del q.page['example3']
    del q.page['CVD']

    #  Store the values entered in text boxes in a list
    input_values = [
        q.args.textbox if q.args.textbox != '' else 25,  # Store the value of the dropdown directly
        q.args.dropdown2,
        q.args.dropdown3,
        q.args.dropdown4,
        q.args.dropdown5,
        q.args.dropdown6,
        q.args.dropdown7,
        q.args.dropdown8,
        q.args.dropdown9,
        q.args.dropdown10,
        q.args.dropdown11,  
        q.args.dropdown12,
        q.args.dropdown13,
        q.args.dropdown14,
        q.args.dropdown15,
        q.args.dropdown16,
        q.args.dropdown17,
        q.args.dropdown18,
        q.args.dropdown19,
        q.args.dropdown20,
        q.args.dropdown21,
        q.args.dropdown22,
        q.args.dropdown23,
    ]

    print(input_values)
    # Get prediction using the predictor object
    prediction = predictor.predict(input_values)
    q.page['example2'] = ui.form_card(box='1 3 2 2', items=[
        ui.text_l(content=f'Prediction: {prediction[1]}'),  # Display prediction
        ui.text_l(content=f'Prediction: {prediction[2]}'), 
        ui.text_l(content=f'Prediction: {prediction[3]}') 
    ])
    footer(q)
    front_pge(q)
    back_home(q)
    lc_plt(q)
    del q.page['details'] 
    q.page['details_pred'] = ui.form_card(box='1 6 8 2', items=[
        ui.text(content='If higher probability in prediction is Low. You have higher chance of not having Lung Cancer. Keep up your Good habits'),
        ui.text(content='If higher probability in prediction is Medium. Control your day-today habits'),
        ui.text(content='If higher probability in prediction is High. Dont panic. We advice you to  meet the family doctor.'),
        ui.text(content='Look at the plot and identify which area you have to improve for better health. Refer WHO standards'),
        ui.link(
                name="who_btn",
                path="https://www.who.int/",
                label="WHO Standards",
                button=True,
            ),
    ],
    )
def lc_form(q: Q):
    ''' Form page to grt input for Lung cancer'''
    del q.page['Diabetes']
    del q.page['CVD']
    del q.page['Lung_Cancer']
    del q.page['example1']
    del q.page['example2']
    del q.page['example3']
    front_pge(q)
    del q.page['lc_plot']
    del q.page['footer']
    
    q.page['example'] = ui.form_card(box='1 3 4 7', items=[
        ui.textbox(name='textbox', label='Input Age', value=q.args.input8),
        ui.dropdown(name='dropdown2', label='Choose Gender', value='2', required=True, choices=choices_gender),
        ui.dropdown(name='dropdown3', label='Air Pollution', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown4', label='Alcohol use', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown5', label='Dust Allergy', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown6', label='OccuPational Hazards', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown7', label='Genetic Risk', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown8', label='chronic Lung Disease', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown9', label='Balanced Diet', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown10', label='Obesity', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown11', label='Smoking', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown12', label='Passive Smoker', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown13', label='Chest Pain', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown14', label='Coughing of Blood', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown15', label='Fatigue', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown16', label='Weight Loss', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown17', label='Shortness of Breath', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown18', label='Wheezing', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown19', label='Swallowing Difficulty', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown20', label='Clubbing of Finger Nails', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown21', label='Frequently Cold', value='1', required=True, choices=choice_level),
        ui.dropdown(name='dropdown22', label='Dry Cough', value='2', required=True, choices=choice_level),
        ui.dropdown(name='dropdown23', label='Snoring', value='1', required=True, choices=choice_level),
        ui.button(name='show_input_lc', label='Submit', primary=True),
    ])
    q.page['details'] = ui.form_card(box='5 3 4 5', items=[
        ui.text_l(content='About the Form'),
        ui.text(content='Please fill the form considering below informations. If any field is unknown default value is level 2. We will assume that you are healthy in that unknown factors. Try to insert more fields for better prediction'),
        ui.text(content= 'Age: The age of the patient. (Numeric)'),
        ui.text(content='Gender: The gender of the patient. (Categorical)'),
        ui.text(content='Air Pollution: The level of air pollution exposure of the patient.(Categorical)'),
        ui.text(content='Alcohol use: The level of alcohol use of the patient. (Categorical)'),
        ui.text(content='Dust Allergy: The level of dust allergy of the patient. (Categorical)'),
        ui.text(content='OccuPational Hazards: The level of occupational hazards of the patient. (Categorical)'),
        ui.text(content='Genetic Risk: The level of genetic risk of the patient. (Categorical)'),
        ui.text(content='chronic Lung Disease: The level of chronic lung disease of the patient. (Categorical)'),
        ui.text(content='Balanced Diet: The level of balanced diet of the patient. (Categorical)'),
        ui.text(content='Obesity: The level of obesity of the patient. (Categorical)'),
        ui.text(content='Smoking: The level of smoking of the patient. (Categorical)'),
        ui.text(content='Passive Smoker: The level of passive smoker of the patient. (Categorical)'),
        ui.text(content='Chest Pain: The level of chest pain of the patient. (Categorical)'),
        ui.text(content='Coughing of Blood: The level of coughing of blood of the patient. (Categorical)'),
        ui.text(content='Fatigue: The level of fatigue of the patient. (Categorical)'),
        ui.text(content='Weight Loss: The level of weight loss of the patient. (Categorical)'),
        ui.text(content= 'Shortness of Breath: The level of shortness of breath of the patient. (Categorical)'),
        ui.text(content='Wheezing: The level of wheezing of the patient. (Categorical)'),
        ui.text(content='Swallowing Difficulty: The level of swallowing difficulty of the patient. (Categorical)'),
        ui.text(content='Clubbing of Finger Nails: The level of clubbing of finger nails of the patient. (Categorical)'),
        ui.text(content='Frequently Cold. (Categorical)'),
        ui.text(content='Dry Cough. (Categorical)'),
        ui.text(content='Snooring. (Categorical)'),
        ui.text(content= 'Technology: We have used H2O AutoML algorithms and predictions are based on best performed one.'),

    ])
    back_home(q)

















