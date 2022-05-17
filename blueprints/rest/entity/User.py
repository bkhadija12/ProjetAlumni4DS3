# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from flask import Blueprint,request,abort,render_template
from flask_login import login_required
from context import DB_EntityLoader_User
from Temod.core.base.attribute import UUID4Attribute
from datetime import datetime
import traceback


# ** EndSection ** Imports

# ** Section ** Blueprint Settings
user_rest = Blueprint('user_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@user_rest.route("/user",methods=["get"])
@login_required
def get_user_User():
	
	return render_template( 
		"user/updateUser.html", 
	  
	 )


@user_rest.route("/user",methods=["post"])
@login_required
def post_user_User():
	form_translator = FormToEntity(User,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = User.from_dict(entity_dct)
	created_id = DB_EntityLoader_User().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@user_rest.route("/user/<string:IdU>",methods=["put"])
@login_required
def put_user_User(IdU):
	entity_dct = dict(request.json)
	print(entity_dct)
	entity_ = DB_EntityLoader_User().get(UUID4Attribute("IdU",value=IdU)).takeSnapshot()
	if entity_ is None:
		return abort(404)
	for key,value in entity_dct.items():
		if key == "Birthday":
			entity_.setAttribute(key,datetime.strptime(value,"%Y-%m-%d"));continue
		entity_.setAttribute(key,value)
	updated_id = DB_EntityLoader_User().updateOnSnapshot(entity_)
	return {"status":"ok"}



@user_rest.route("/user",methods=["delete"])
def delete_user_User():
	entity_ = DB_EntityLoader_User().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints