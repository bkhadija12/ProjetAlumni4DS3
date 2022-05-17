# ** Section ** Imports
from flask import Flask, g, request, render_template, redirect, url_for
from flask_login import current_user, login_required, LoginManager, login_user, logout_user

from flask_cors import CORS

from Temod.core.base.attribute import UUID4Attribute

from blueprints import *
from context import *
from data import *
from recommandation import similar_jobs

from core.entity.user import User

import mimetypes
import configs
# ** EndSection ** Imports

# ** Section ** MimetypesDefinition
mimetypes.add_type('text/javascript', '.min.js')
mimetypes.add_type('text/javascript', '.js')
mimetypes.add_type('text/css', '.min.css')
mimetypes.add_type('text/css', '.css')
# ** EndSection ** MimetypesDefinition


# ** Section ** AppCreation
app = Flask(__name__,template_folder="front/templates", static_folder="front/static")
app.secret_key = "LogesnrejxEF,qS?"
CORS(app)
# ** EndSection ** AppCreation


# ** Section ** AppContext
@app.context_processor
def inject_gardian():
    return dict(gardian=configs.GARDIAN)

@app.teardown_appcontext
def teardown_db(exception):
	for dbName in g.pop('databases',[]):
		g.pop(dbName).close()

# ** EndSection ** AppContext


# ** Section ** AppSecurity
def get_user_by_id(x):
	
	return DB_EntityLoader_User().get(UUID4Attribute('IdU',value=x,owner_name=User.ENTITY_NAME))
configs.AUTHENTICATOR.setLoader(
	lambda x:get_user_by_id(x)
)
configs.AUTHENTICATOR.init_app(app)

type(configs.GARDIAN).DEFAULT_USER_LOADER = lambda: current_user

@configs.GARDIAN.alarm_response('default')
def on_default_alarm():
	return render_template("errors/page-404.html")
# ** EndSection ** AppSecurity


# ** Section ** BlueprintsRegistration
app.register_blueprint(recommandation_rest)
app.register_blueprint(notification_rest)
app.register_blueprint(userevent_rest)
app.register_blueprint(student_rest)
app.register_blueprint(userjob_rest)
app.register_blueprint(alumni_rest)
app.register_blueprint(skills_rest)
app.register_blueprint(event_rest)
app.register_blueprint(admin_rest)
app.register_blueprint(user_rest)
app.register_blueprint(job_rest)
# ** EndSection ** BlueprintsRegistration

# ** Section ** HomeRegistration
@app.route('/')
@login_required
def home():
	recommandation = similar_jobs('Berlin, Berlin, Allemagne')
	print(recommandation)
	return render_template(

		'acceuil.html',
		recommandation=recommandation
	
		)
# ** Section ** HomeEndpoints

# ** Section ** LoginEndpoints
@app.route('/login',methods=['GET',"POST"])
def login():
	msg = None
	if request.method == "POST":
		user=DB_EntityLoader_User().byLogins(request.form.get("email"),request.form.get("password"))
		if user is not None:
			activeUser = DB_EntityLoader_User().setLoggedIn(user)
			login_user(activeUser)
			return redirect(url_for('home'))
		else:
			msg = "Identifiants Erronés"
	return render_template( 
		"login.html",
		error=msg
	)

@app.route('/logout',methods=['GET',"POST"])
@login_required
def logout():
	DB_EntityLoader_User().setLoggedOut(current_user._get_current_object())
	logout_user()
	return redirect('/login')
# ** EndSection ** LoginEndpoints

@app.route("/dashboard")
@login_required
def get_dashboard():
	Nationalities = df_survey_row['Nationality'].value_counts().to_dict()
	Gender = df_survey_row['Gender'].value_counts().to_dict()
	UserLanguage=df_survey["UserLanguage"].value_counts().to_dict()
	UserLanguage.pop('User Language')
	

	Institution = df_survey_row['Institution Name'].value_counts().to_dict()
	LevelStudy = df_survey_row["Level of Study (Abbreviated)"].value_counts().to_dict()
	
	return render_template( 
		"index.html", 
     	Nationality = Nationalities, 
		Gender=Gender,
		Institution=Institution, 
		Needs = Needs,
		Language = UserLanguage,
		LevelStudy = LevelStudy,
		Status = Current_Student_Status,
		active_sidebar_item="dashboard"
	  
	 )



# ** Section ** ServerLaunch
if __name__ == '__main__':
	app.run(host=configs.HOST,port=configs.PORT,threaded=configs.THREADED,debug=configs.DEBUG)
# ** EndSection ** ServerLaunch

