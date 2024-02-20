from h2o_wave import Q, app, ui

@app('/risk-assesment')
async def serve(q: Q):
    # Define the main page layout
    q.page = ui.page(
        path='/', 
        title='HealthGuardian: Disease Risk Detector',
        )

    # Welcome message
    q.page['header'] = ui.header_card(
        box='1 1 6 1',
        title='Welcome to HealthGuardian: Disease Risk Detector',
    )

    # Message to select disease
    q.page['select_message'] = ui.message_bar(
        box='1 2 6 1',
        text='Please select your disease to evaluate risk',
    )

    # Cards for diseases
    q.page['disease_cards'] = ui.cards(
        box='1 3 2 1',
        items=[
            ui.card(
                title='Lung Cancer',
                caption='Click to continue to Lung Cancer evaluation',
                on_click=q.page('/lung_cancer'),
            ),
            ui.card(
                title='CVD',
                caption='Click to continue to CVD evaluation',
                on_click=q.page('/cvd'),
            ),
            ui.card(
                title='Diabetes',
                caption='Click to continue to Diabetes evaluation',
                on_click=q.page('/diabetes'),
            ),
        ]
    )

    await q.page.save()
