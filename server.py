from flask import *
from models import Applicant

app = Flask('school_system')


@app.route('/save', methods=['POST'])
def post():
    data = request.form
    Applicant.new_applicant(data)

@app.route('/list', methods=['GET'])
def send():
    query_to_print = Applicant.all_applicant(Applicant)
    print (query_to_print)
    return render_template('list.html', query=query_to_print)


app.run()