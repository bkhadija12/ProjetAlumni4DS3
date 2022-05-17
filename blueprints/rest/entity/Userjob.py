# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from context import DB_EntityLoader_Userjob
from flask import Blueprint,request,abort
import traceback

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
userjob_rest = Blueprint('userjob_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@userjob_rest.route("/userjob",methods=["get"])
def get_user_Userjob():
	entity_ = DB_EntityLoader_Userjob().get()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



@userjob_rest.route("/userjob",methods=["post"])
def post_user_Userjob():
	form_translator = FormToEntity(Userjob,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Userjob.from_dict(entity_dct)
	created_id = DB_EntityLoader_Userjob().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@userjob_rest.route("/userjob",methods=["put"])
def put_user_Userjob():
	form_translator = FormToEntity(Userjob)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Userjob().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Userjob().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@userjob_rest.route("/userjob",methods=["delete"])
def delete_user_Userjob():
	entity_ = DB_EntityLoader_Userjob().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints