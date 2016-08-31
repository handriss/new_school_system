from flask import Flask, render_template
from models import Applicant
from populator import Populator

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/confirm_page')
def confirm():
    Applicant.get_application_codes()
    code = Applicant.application_code_generator()
    return render_template('confirm_page.html', code=code)


if __name__ == "__main__":
    Populator.establish_connection()
    Populator.populate_tables()
    app.run()
