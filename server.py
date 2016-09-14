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
    new_applicant = {}
    # new_applicant.append(request.form['first_name'])
    Applicant.get_application_codes()
    code = Applicant.application_code_generator()
    new_applicant['first_name'] = request.form['first_name']
    new_applicant['last_name'] = request.form['last_name']
    new_applicant['email'] = request.form['email']
    new_applicant['city'] = request.form['city']
    new_applicant['code'] = code
    Applicant.new_applicant(new_applicant)

    return render_template('confirm_page.html', new_applicant=new_applicant)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/list_menu', methods=['GET'])
def send():
    query_to_print = Applicant.all_applicant()
    print (query_to_print)
    return render_template('list_menu.html', query=query_to_print)




@app.route('/filtered_list', methods= ['GET', 'POST'])
def run_query():
    filter_by = request.form['filter_by']
    value = request.form['value']
    query_to_print = Applicant.run_query(filter_by, value)
    return render_template('list_menu.html', query=query_to_print)


if __name__ == "__main__":
    Populator.establish_connection()
    Populator.populate_tables()
    app.run(port=5001)
