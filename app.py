from flask import Flask, render_template, session, redirect, url_for
from model import Formulario, procuraAgenciasBB

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='JAJAJKKKAHERJJCCAASS')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Formulario()
    if form.validate_on_submit():
        session['agencia'] = form.agencia.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, agencia=procuraAgenciasBB(session.get('agencia')))

if __name__ == '__main__':
    app.run(debug=True)
