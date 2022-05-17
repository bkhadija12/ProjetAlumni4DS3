# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from context import DB_EntityLoader_Notification
from flask import Blueprint,request,abort
import traceback

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
notification_rest = Blueprint('notification_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@notification_rest.route("/notification",methods=["get"])
def get_notification_Notification():
	entity_ = DB_EntityLoader_Notification().get()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



@notification_rest.route("/notification",methods=["post"])
def post_notification_Notification():
	form_translator = FormToEntity(Notification,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Notification.from_dict(entity_dct)
	created_id = DB_EntityLoader_Notification().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@notification_rest.route("/notification",methods=["put"])
def put_notification_Notification():
	form_translator = FormToEntity(Notification)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Notification().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Notification().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@notification_rest.route("/notification",methods=["delete"])
def delete_notification_Notification():
	entity_ = DB_EntityLoader_Notification().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints