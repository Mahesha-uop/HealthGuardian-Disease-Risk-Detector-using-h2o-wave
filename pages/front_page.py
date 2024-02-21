from h2o_wave import Q, ui

def back_home(q: Q):
    ''' Come to front page from anywhere '''
    q.page['Back'] = ui.form_card(box='1 2 2 1', items=[
    ui.button(
        name="back",
        label="Back to Home",
        primary=True,
    ),
    ],
    )
    
def front_pge(q: Q):
    ''' front page header '''
    # Welcome message
    q.page['header'] = ui.header_card(
        box='1 1 10 1',
        title='HealthGuardian: Disease Risk Detector',
        subtitle='Guarding Your Health, Predicting Your Future.',
    )

def front_cards(q: Q):
    ''' front page style '''
    del q.page['diabetes_plot']
    del q.page['Back']
    del q.page['details']
    del q.page['details_pred']
    del q.page['lc_plot'] 
    del q.page['cvd_plot'] 
    # Cards for diseases
    q.page['Lung_Cancer'] = ui.tall_info_card(
        box='1 2 2 5',
        name='Lung_Cancer',
        title='Lung Cancer',
        caption='Lung cancer detection is crucial for early intervention and improved prognosis, leveraging advanced screening techniques and AI-driven analysis to identify subtle signs and symptoms.',
        category='Risk Prediction',
        image = 'https://www.shebaonline.org/wp-content/uploads/2022/05/lung-cancer.jpg',
    
    )
    
    
    q.page['CVD'] = ui.tall_info_card(
        box='3 2 2 5',
        name='CVD',
        title='Cardiovascular Disease',
        caption='Cardiovascular disease (CVD) detection employs innovative diagnostics and risk profiling tools, empowering individuals to adopt preventive measures and lead heart-healthy lifestyles for long-term well-being.',
        category='Risk Prediction',
        image='https://i.ibb.co/370Dnb1/male-student-practicing-medicine.jpg',
    )

    q.page['Diabetes'] = ui.tall_info_card(
        box='5 2 2 5',
        name='Diabetes',
        title='Diabetes',
        caption='With diabetes on the rise globally, accurate risk assessment and proactive management are essential to mitigate complications, emphasizing lifestyle modifications and personalized treatment plans.',
        category='Risk Prediction',
        image='https://i.ibb.co/9ySHn5v/a5qp-qxmg-230817.jpg',
    
    )

    q.page['example'] = ui.form_card(box='7 2 4 1', items=[
        ui.text_l(content='Select a disese type to continue(It is better to have with with your medical reports)'),
        ],
    )
    q.page['example1'] = ui.form_card(box='7 3 2 2', items=[
        ui.text_l(content='Click button to predict Lung Cancer'),
        ui.button(
            name="lung_can",
            label="Lung Cancer",
            primary=False,
        ),
        ],
    )

    q.page['example2'] = ui.form_card(box='9 3 2 2', items=[
        ui.text_l(content='Click button to predict Diabetes'),
        ui.button(
            name="diabetes",
            label="Diabetes",
            primary=True,
        ),
        ],
    )
    q.page['example3'] = ui.form_card(box='8 5 2 2', items=[
        ui.text_l(content='Click button to predict CVD'),
        ui.button(
            name="cvd", 
            label="Cardiovascular Disease", 
            primary=False,
        ),
        ],
        
    )
    footer(q)


def footer(q: Q):
    ''' footer style '''
    caption = """__Made with 💛 by Mahesha Viduranga__ <br /> using __[h2o Wave](https://wave.h2o.ai/docs/getting-started).__"""
    q.page['footer'] = ui.footer_card(
        box="1 8 10 2",
        caption=caption,
        items=[
            ui.inline(
                justify="end",
                items=[
                    ui.links(
                        label="Contact Me",
                        width="200px",
                        items=[
                            ui.link(
                                name="github",
                                label="GitHub",
                                path="https://github.com/Mahesha-uop/HealthGuardian-Disease-Risk-Detector-using-h2o-wave",
                                target="_blank",
                            ),
                            ui.link(
                                name="linkedin",
                                label="LinkedIn",
                                path="https://www.linkedin.com/in/mahesha-viduranga-247b3a204",
                                target="_blank",
                            ),
                            ui.link(
                                name="portfolio",
                                label="Portfolio",
                                path="https://mahesha-uop.github.io/maheshaviduranga.github.io",
                                target="_blank",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )