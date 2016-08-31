from flask import *
from models import Applicant
from populator import Populator

app = Flask('school_system')
app.config['DEBUG'] = True


@app.route('/apply')
def apply():
    return render_template('apply.html')


@app.route('/save', methods=['POST'])
def post():
    print('ghjk')
    new_applicant = {}
    # new_applicant.append(request.form['first_name'])
    new_applicant['first_name'] = request.form['first_name']
    new_applicant['last_name'] = request.form['last_name']
    new_applicant['email'] = request.form['email']
    new_applicant['city'] = request.form['city']
    Applicant.new_applicant(new_applicant)
    return redirect('/list')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/confirm_page')
def confirm():
    Applicant.get_application_codes()
    code = Applicant.application_code_generator()
    return render_template('confirm_page.html', code=code)


@app.route('/list', methods=['GET'])
def send():
    query_to_print = Applicant.all_applicant()
    print(query_to_print)
    return render_template('list.html', query=query_to_print)

if __name__ == "__main__":
    Populator.establish_connection()
    Populator.populate_tables()
    app.run()
