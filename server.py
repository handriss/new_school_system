from flask import *
from models import Applicant, Mentor
from populator import Populator
from models.basemodel import *
from peewee import *
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask('school_system')
app.config['DEBUG'] = True

app.config.update(DEBUG=True, SECRET_KEY='secret_xxx')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return ("Applicant id: {}".format(self.id))




@app.route('/apply', methods=['GET'])
def apply():
    return render_template('apply.html')


@app.route('/confirm_page', methods=['POST'])
def post():
    try:
        with db.transaction():

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

    except IntegrityError:
        email_in_use = True
        return render_template('apply.html', email_in_use=email_in_use)

    #return render_template('confirm_page.html', new_applicant=new_applicant)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/list_menu', methods=['GET'])
@login_required
def send():
    query_to_print = Applicant.all_applicant()
    return render_template('list_menu.html', query=query_to_print)


@app.route('/filtered_list', methods=['GET', 'POST'])
@login_required
def run_query():
    filter_by = request.form['filter_by']
    value = request.form['value']
    query_to_print = Applicant.run_query(filter_by, value)
    return render_template('list_menu.html', query=query_to_print)


@app.route('/list', methods=['GET'])
@app.route('/', methods=['GET'])
@login_required
def view_list():
    query_to_print = Applicant.all_applicant()
    return render_template('list.html', query=query_to_print)


@app.route("/applicant/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        try:
            if request.form['user'] == 'applicant':
                applicant = Applicant.get(Applicant.email == request.form['email'])
                if applicant.application_code == request.form['application_code']:

                    user = User("applicant")
                    print  (user)
                    login_user(user)

                    new_applicant = {}
                    new_applicant['first_name'] = applicant.first_name
                    new_applicant['last_name'] = applicant.last_name
                    new_applicant['email'] = applicant.email
                    new_applicant['city'] = applicant.city
                    new_applicant['application_code'] = applicant.application_code
                    print (new_applicant)

                    return render_template('confirm_page.html', new_applicant=new_applicant)
            elif request.form['user'] == 'mentor':
                mentor = Mentor.get(Mentor.email == request.form['email'])

                if mentor.password == request.form['application_code']:
                    user = User("mentor")
                    print(user)
                    login_user(user)

                    query = Applicant.all_applicant()
                    return render_template('list_menu.html', query=query)
        except:
            return abort(401)
    else:
        return Response(render_template('login.html'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response(render_template('logout.html'))


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p> <a href="/applicant/login">back</a>')


@login_manager.user_loader
def load_user(userid):
    return User(userid)


if __name__ == "__main__":
    Populator.establish_connection()
    Populator.populate_tables()
    app.run(port=5001)
