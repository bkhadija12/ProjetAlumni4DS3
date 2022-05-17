# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from flask import Blueprint,request,abort
from context import DB_EntityLoader_Admin
import traceback

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
admin_rest = Blueprint('admin_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@admin_rest.route("/admin",methods=["get"])
def get_person_Admin():
	entity_ = DB_EntityLoader_Admin().get()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



@admin_rest.route("/admin",methods=["post"])
def post_person_Admin():
	form_translator = FormToEntity(Admin,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Admin.from_dict(entity_dct)
	created_id = DB_EntityLoader_Admin().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@admin_rest.route("/admin",methods=["put"])
def put_person_Admin():
	form_translator = FormToEntity(Admin)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Admin().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Admin().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@admin_rest.route("/admin",methods=["delete"])
def delete_person_Admin():
	entity_ = DB_EntityLoader_Admin().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints