from flask import *
from models import Applicant
from populator import Populator

app = Flask('school_system')
app.config['DEBUG'] = True


@app.route('/apply')
def apply():
    return render_template('apply.html')


@app.route('/confirm_page', methods=['POST'])
def post():

    Applicant.get_application_codes()
    code = Applicant.application_code_generator()
    Applicant.create(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        email=request.form['email'],
        city=request.form['city'],
        application_code=code
    )
    new_applicant = Applicant.get(application_code=code)
    return render_template('confirm_page.html', new_applicant=new_applicant)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list_menu', methods=['GET'])
def send():
    return render_template('list_menu.html', query=Applicant.select())


@app.route('/filtered_list', methods=['GET', 'POST'])
def run_query():
    filter_by = request.form['filter_by']
    value = request.form['value']
    query_to_print = Applicant.run_query(filter_by, value)
    return render_template('list_menu.html', query=query_to_print)


if __name__ == "__main__":
    Populator.establish_connection()
    Populator.populate_tables()
    app.run(port=5001)
