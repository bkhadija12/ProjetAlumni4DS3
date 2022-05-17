# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from context import DB_EntityLoader_Userevent
from flask import Blueprint,request,abort
import traceback

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
userevent_rest = Blueprint('userevent_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@userevent_rest.route("/userevent",methods=["get"])
def get_user_Userevent():
	entity_ = DB_EntityLoader_Userevent().get()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



@userevent_rest.route("/userevent",methods=["post"])
def post_user_Userevent():
	form_translator = FormToEntity(Userevent,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Userevent.from_dict(entity_dct)
	created_id = DB_EntityLoader_Userevent().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@userevent_rest.route("/userevent",methods=["put"])
def put_user_Userevent():
	form_translator = FormToEntity(Userevent)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Userevent().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Userevent().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@userevent_rest.route("/userevent",methods=["delete"])
def delete_user_Userevent():
	entity_ = DB_EntityLoader_Userevent().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints