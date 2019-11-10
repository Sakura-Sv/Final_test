from flask import Flask,url_for,render_template,flash,redirect
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign In')


def request_data():
    requests.post('https://os.ncuos.com/api/user/token',header="")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {},remember_me={}'.format(
            form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template(url_for('login'),form=form)



if __name__ == '__main__':
    app.run()
