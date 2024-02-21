from h2o_wave import Q, app, ui, main
from func_diseases.diabetes import predictor_diabetes
# from func_diseases.cvd import predictor_cvd
# from func_diseases.lung_cancer import predictor_lung_cancer
from pages.diabetes_page import diabetes_pred,diabetes_form
from pages.front_page import front_pge,front_cards

choices_pick = [
    ui.choice('A', 'Lung Cancer'),
    ui.choice('B', 'Cardiovascular Disease'),
    ui.choice('C', 'Diabetes'),
]


# Main page
@app('/health_guardian')
async def serve(q: Q):

    if q.args.show_input_diabetes:
        diabetes_pred(q,predictor_diabetes)
        if q.args.back:
            front_pge
            front_cards



            
    else:
        if q.args.diabetes:
            diabetes_form(q)
            if q.args.back:
                front_pge
                front_cards


        else: 
            front_pge(q)
            front_cards(q)



    await q.page.save()


if __name__ == '__main__':
    main('/health_guardian', host='127.0.0.1', port=10101)

