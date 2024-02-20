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

    q.page['example'] = ui.form_card(box='7 3 2 4', items=[
            ui.text_l(content='Risk Assesment Form'),
            ui.choice_group(name='choice_group', label='Pick the disease for risk assesment', value='B', required=True, choices=choices_pick),
            # ui.button(name='show_inputs', label='Submit', primary=True),
        ])

    # if q.args.show_inputs:
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
    
    if q.args.show_input:
        del q.page['example']
        del q.page['header']
        del q.page['CVD']
        del q.page['Diabetes']
        del q.page['Lung_Cancer']
        #  Store the values entered in text boxes in a list
        input_values = [
            q.args.textbox1,
            q.args.textbox2,
            q.args.textbox3,
            q.args.textbox4,
            q.args.textbox5,
            q.args.textbox6,
            q.args.textbox7,
            q.args.textbox8,
        ]

        # Get prediction using the predictor object
        prediction = predictor.predict(input_values)#  Store the values entered in text boxes in a list
        q.page['example2'] = ui.form_card(box='1 3 4 7', items=[
            ui.text(f'textbox1={q.args.textbox}'),
            ui.text_l(content=f'Prediction: {prediction}')  # Display prediction
        ])
        
            
    # else:
    #     q.page['example'] = ui.form_card(box='7 3 2 4', items=[
    #         ui.text_l(content='Risk Assesment Form'),
    #         ui.choice_group(name='choice_group', label='Pick the disease for risk assesment', value='B', required=True, choices=choices_pick),
    #         ui.button(name='show_inputs', label='Submit', primary=True),
    #     ])
    await q.page.save()

# # Lung cancer page
# @app('/lung_cancer')
# async def lung_cancer_page(q: Q):
#     # Define the layout for lung cancer page
#     q.page['header'] = ui.header_card(
#         title='Lung Cancer Risk Prediction',
#         subtitle='Please provide the following information to evaluate your risk.'
#     )

#     # Your form components for lung cancer page goes here...

#     await q.page.save()

# # CVD page
# @app('/cvd')
# async def cvd_page(q: Q):
#     # Define the layout for CVD page
#     q.page['header'] = ui.header_card(
#         title='CVD Risk Prediction',
#         subtitle='Please provide the following information to evaluate your risk.'
#     )

#     # Your form components for CVD page goes here...

#     await q.page.save()

# # Diabetes page
# @app('/diabetes')
# async def diabetes_page(q: Q):
#     # Define the layout for diabetes page
#     q.page['header'] = ui.header_card(
#         title='Diabetes Risk Prediction',
#         subtitle='Please provide the following information to evaluate your risk.'
#     )

#     # Your form components for diabetes page goes here...

#     await q.page.save()





if __name__ == '__main__':
    main('/health_guardian', host='127.0.0.1', port=10101)

# from h2o_wave import main, app, Q, ui

# @app('/health_guardian')
# async def serve(q: Q):

#     # Welcome message
#     q.page['header'] = ui.header_card(
#         box='1 1 8 1',
#         title='HealthGuardian: Disease Risk Detector',
#         subtitle='Welcome!',
#     )

#     q.page['Lung_Cancer'] = ui.tall_info_card(
#             box='1 2 2 4',
#             name='Lung Cancer',
#             title='Lung Cancer',
#             caption='You can asses your risks from your medical records and habits.',
#             category='Risk Prediction',
#             label='Click',
#             image='https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
#         )

#     q.page['CVD'] = ui.tall_info_card(
#                 box='3 2 2 4',
#                 name='CVD',
#                 title='Cardiovascular Disease',
#                 caption='You can asses your risks from your medical records and habits.',
#                 category='Risk Prediction',
#                 label='Click',
#                 image='https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
#             )
    
#     q.page['Diabetes'] = ui.tall_info_card(
#                 box='5 2 2 4',
#                 name='Diabetes',
#                 title='Diabetes',
#                 caption='You can asses your risks from your medical records and habits.',
#                 category='Risk Prediction',
#                 label='Click',
#                 image='https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
#             )
    

        

#     await q.page.save()

# if __name__ == '__main__':
#     main('/health_guardian', host='127.0.0.1', port=10101)

    # caption = '''
    # ![theme-generator](https://wave.h2o.ai/img/logo.svg)

    # Made with 💛 by H2O Wave Team.'''
    # q.page['footer1'] = ui.footer_card(box='1 7 -1 1', caption='Made with 💛 by H2O Wave Team.')
    # # q.page['footer2'] = ui.footer_card(box='1 7 -1 3', caption=caption)
    # q.page['footer3'] = ui.footer_card(
    #     box='1 7 -1 3',
    #     caption=caption,
    #     items=[
    #         ui.inline(justify='end', items=[
    #             ui.links(label='First Column', width='200px', items=[
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #             ]),
    #             ui.links(label='Second Column', width='200px', items=[
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #             ]),
    #             ui.links(label='Third Column', width='200px', items=[
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #                 ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
    #             ]),
    #         ]),
    #     ]
    # )

# def lung_cancer(q: Q, msg):
#     q.page["search_box"] = ui.form_card(
#         box= '1 2 2 4',
#         items=[
#             ui.text_m(content='Lung Cancer'),
#             ui.text(content='You can asses your risks from your medical records and habits.'),
#             ui.buttons(
#                 items=[
#                     ui.button(
#                         name="search",
#                         label="Search",
#                         primary=True,
#                         icon="BookAnswers",
#                     ),
#                     ui.button(name="find_books", label="Find Book", primary=False),
#                 ]
#             ),
#             ui.text(msg, size="m", name="msg_text"),
#         ],
#     )

# from h2o_wave import main, app, Q, ui



# @app('/health_guardian')
# async def serve(q: Q):
#     if q.args.show_inputs:
#         q.page['example'].items = [
#             ui.text(f'selected={q.args.choice_group}'),
#             ui.button(name='show_form', label='Back', primary=True),
#         ]
#     else:
#         q.page['example'] = ui.form_card(box='1 1 4 7', items=[
#             ui.choice_group(name='choice_group', label='Pick one', value='B', required=True, choices=choices),
#             ui.button(name='show_inputs', label='Submit', primary=True),
#         ])
#     await q.page.save()