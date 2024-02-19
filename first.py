from h2o_wave import main, app, Q, ui


@app('/myfirst')
async def serve(q: Q):
    q.page['card1'] = ui.form_card(box='1 1 2 2', items=[
            ui.text(content='Helo world'),	
    ])
    await q.page.save()
