from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    # return '<h1>Olá Flask</h1>'   # não é uma boa ideia colocar html explicitamente no código
    return render_template('lista.html')


app.run()
