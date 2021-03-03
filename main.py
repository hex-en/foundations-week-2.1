from flask import Flask, render_template, request
from forms import ContactForm
import pandas as pd

app = Flask(__name__)
app.secret_key = '211569666'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name': name, 'email': email,
                            'subject': subject, 'message': message}, index=[0])
        res.to_csv('./contactusMessage.csv')

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
