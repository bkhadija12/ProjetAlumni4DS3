# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from context import DB_EntityLoader_Skills
from flask import Blueprint,request,abort
import traceback

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
skills_rest = Blueprint('skills_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@skills_rest.route("/skills",methods=["get"])
def get_skills_Skills():
	entity_ = DB_EntityLoader_Skills().get()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



@skills_rest.route("/skills",methods=["post"])
def post_skills_Skills():
	form_translator = FormToEntity(Skills,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Skills.from_dict(entity_dct)
	created_id = DB_EntityLoader_Skills().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@skills_rest.route("/skills",methods=["put"])
def put_skills_Skills():
	form_translator = FormToEntity(Skills)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Skills().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Skills().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@skills_rest.route("/skills",methods=["delete"])
def delete_skills_Skills():
	entity_ = DB_EntityLoader_Skills().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints