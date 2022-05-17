# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from flask import Blueprint,request,abort,render_template
from context import DB_EntityLoader_event
import traceback

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
event_rest = Blueprint('event_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@event_rest.route("/events",methods=["get"])
def get_event_event():
	return render_template( 
		"events/index_events.html", 
	   active_sidebar_item="events"
	 )
@event_rest.route("/event")
def get_add_event():
	return render_template( 
		"events/addEvents.html", 
	   active_sidebar_item="events"
	 )

@event_rest.route("/event",methods=["post"])
def post_event_event():
	form_translator = FormToEntity(event,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = event.from_dict(entity_dct)
	created_id = DB_EntityLoader_event().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@event_rest.route("/event",methods=["put"])
def put_event_event():
	form_translator = FormToEntity(event)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_event().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_event().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@event_rest.route("/event",methods=["delete"])
def delete_event_event():
	entity_ = DB_EntityLoader_event().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints