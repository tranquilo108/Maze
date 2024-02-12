from flask import Flask, render_template, request, redirect, url_for
from wtforms.fields import SelectField
from wtforms import Form

from mansion import Mansion

app = Flask(__name__)
mansion_ = Mansion()


class WayForm(Form):
    way = SelectField(
        'Выберите сторону света, в которую желаете отправиться',
        choices=[
            ('Север'),
            ('Восток'),
            ('Юг'),
            ('Запад')
        ],
        render_kw={
            'class': 'form-control'
        }
    )


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/start_game/')
def start_game():
    mansion_ = Mansion()
    return render_template('start_game.html', mansion_=mansion_)


@app.route('/game/', methods=['GET', 'POST'])
def game():
    form = WayForm(request.form)
    if request.method == 'POST' and form.validate():
        mansion_.move_to(form.way.data)

    return render_template('game.html', mansion_=mansion_, form=form)


if __name__ == '__main__':
    app.run()
