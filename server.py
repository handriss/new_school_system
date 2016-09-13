from flask import *
from models import Applicant
from populator import Populator
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask('school_system')

app.config.update(DEBUG=True, SECRET_KEY='secret_xxx')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"

    def __repr__(self):
        return ("{}, {}, {}".format(self.id, self.name, self.password))

users = [User(id) for id in range(1, 21)]


@app.route('/apply')
def apply():
    return render_template('apply.html')


@app.route('/confirm_page', methods=['POST'])
def post():
    new_applicant = {}
    Applicant.get_application_codes()
    code = Applicant.application_code_generator()
    new_applicant['first_name'] = request.form['first_name']
    new_applicant['last_name'] = request.form['last_name']
    new_applicant['email'] = request.form['email']
    new_applicant['city'] = request.form['city']
    new_applicant['application_code'] = code
    Applicant.new_applicant(new_applicant)

    return render_template('confirm_page.html', new_applicant=new_applicant)


@app.route('/list', methods=['GET'])
@app.route('/', methods=['GET'])
# @login_required
def send():
    query_to_print = Applicant.all_applicant()
    print(query_to_print)
    return render_template('list.html', query=query_to_print)


@app.route("/applicant/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        try:
            applicant = Applicant.get(Applicant.email == request.form['email'])
        except:
            return abort(401)

        if applicant.application_code == request.form['application_code']:
            print("minden ok")
            user = User(applicant.id)
            login_user(user)

            new_applicant = {}
            new_applicant['first_name'] = applicant.first_name
            new_applicant['last_name'] = applicant.last_name
            new_applicant['email'] = applicant.email
            new_applicant['city'] = applicant.city
            new_applicant['application_code'] = applicant.application_code

            return render_template('confirm_page.html', new_applicant=new_applicant)
        else:
            return abort(401)
    else:
        return Response(render_template('applicant_login.html'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


@login_manager.user_loader
def load_user(userid):
    return User(userid)


if __name__ == "__main__":
    Populator.establish_connection()
    Populator.populate_tables()
    app.run(port=5001)
