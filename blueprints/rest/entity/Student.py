# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from context import DB_EntityLoader_Student
from flask import Blueprint,request,abort
import traceback

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
student_rest = Blueprint('student_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@student_rest.route("/student",methods=["get"])
def get_person_Student():
	entity_ = DB_EntityLoader_Student().get()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



@student_rest.route("/student",methods=["post"])
def post_person_Student():
	form_translator = FormToEntity(Student,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Student.from_dict(entity_dct)
	created_id = DB_EntityLoader_Student().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@student_rest.route("/student",methods=["put"])
def put_person_Student():
	form_translator = FormToEntity(Student)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Student().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Student().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@student_rest.route("/student",methods=["delete"])
def delete_person_Student():
	entity_ = DB_EntityLoader_Student().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints