from h2o_wave import Q, ui

def front_pge(q: Q):
    # Welcome message
    q.page['header'] = ui.header_card(
        box='1 1 8 1',
        title='HealthGuardian: Disease Risk Detector',
        subtitle='Precaution before Destrotion',
    )

def front_cards(q: Q):
    # Cards for diseases
    path = 'F:\Learn_python\Test_Interview\H2o_app\HealthGuardian-Disease-Risk-Detector-using-h2o-wave\plots\diabetes_variable_importance.png'
    q.page['example'] = ui.form_card(box='1 2 2 4', items=[
    ui.image(title='Image title', path=path),
    ])
    q.page['Lung_Cancer'] = ui.tall_info_card(
        box='1 5 2 4',
        name='Lung_Cancer',
        title='Lung Cancer',
        caption='You can assess your risks from your medical records and habits.',
        category='Risk Prediction',
    
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

def back_home(q: Q):
    q.page['Back'] = ui.form_card(box='1 2 2 1', items=[
    ui.button(
        name="back",
        label="Back to Home",
        primary=True,
    ),
    ],
)