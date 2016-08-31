from flask import *
from models import Applicant

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


@app.route('/list', methods=['GET'])
def send():
    query_to_print = Applicant.all_applicant()
    print (query_to_print)
    return render_template('list.html', query=query_to_print)


app.run()