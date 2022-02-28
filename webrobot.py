from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import sys
sys.path.insert(0, "../")

import aiml
k = aiml.Kernel()
k.learn("cn-startup.xml")
k.respond("load aiml cn")
k.respond("start")
                         
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):                 
    name = StringField('请开始交谈：', validators=[Required()])
    submit = SubmitField('提交')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ''
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=k.respond(name))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8089)
