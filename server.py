from flask import *
from models import Applicant

app = Flask('school_system')
app.config['DEBUG'] = True

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/save', methods=['POST'])
def post():
    new_applicant = {}
    new_applicant['first_name'] = request.form['first_name']
    new_applicant['last_name'] = request.form['last_name']
    new_applicant['email'] = request.form['email']
    new_applicant['city'] = request.form['city']
    Applicant.new_applicant(new_applicant)
    return redirect('/list_menu')

@app.route('/')
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



app.run()