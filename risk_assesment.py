from h2o_wave import Q, app, ui, main
from func_diseases.diabetes import predictor_diabetes
# from func_diseases.cvd import predictor_cvd
# from func_diseases.lung_cancer import predictor_lung_cancer
from pages.diabetes_page import diabetes_pred,diabetes_form

choices_pick = [
    ui.choice('A', 'Lung Cancer'),
    ui.choice('B', 'Cardiovascular Disease'),
    ui.choice('C', 'Diabetes'),
]


# Main page
@app('/health_guardian')
async def serve(q: Q):
    if q.args.show_input:
            diabetes_pred(q,predictor_diabetes)
            
    else:
        if q.args.diabetes:
            diabetes_form(q)

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
                
            )

    await q.page.save()


if __name__ == '__main__':
    main('/health_guardian', host='127.0.0.1', port=10101)

