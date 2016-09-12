from flask import *
from models import Applicant
from populator import Populator
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask('school_system')

# config
app.config.update(DEBUG=True, SECRET_KEY='secret_xxx')

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


# create some users with ids 1 to 20
users = [User(id) for id in range(1, 21)]


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
    new_applicant['application_code'] = code
    Applicant.new_applicant(new_applicant)

    return render_template('confirm_page.html', new_applicant=new_applicant)


@app.route('/list', methods=['GET'])
def send():
    query_to_print = Applicant.all_applicant()
    print(query_to_print)
    return render_template('list.html', query=query_to_print)


@app.route('/')
@login_required
def home():
    return Response(render_template('list.html'))


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "_secret":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response(render_template('index.html'))


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
