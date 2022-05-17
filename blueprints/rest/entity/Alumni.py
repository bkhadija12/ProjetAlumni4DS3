# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from context import DB_EntityLoader_Alumni
from flask import Blueprint,request,abort,render_template

from data import *

import traceback
import requests
import configs
import yaml
# ** EndSection ** Imports

# ** Section ** Functions
def get_from_position_stack(location):
	try:
		req = requests.get(
			f'http://api.positionstack.com/v1/forward?access_key={configs.POSITIONSTACK_API_KEY}&query={location}&output=json&limit=1'
		)
		js = req.json()['data'][0]
		coordinates = (js['latitude'],js['longitude'])
		print(f"{location}: {coordinates}")
		return coordinates
	except IndexError:
		return []
	except:
		traceback.print_exc()
# ** EndSection ** Functions

# ** Section ** Blueprint Settings
alumni_rest = Blueprint('alumni_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@alumni_rest.route("/alumni",methods=["get"])
def get_person_Alumni():
	entity_ = DB_EntityLoader_Alumni().get()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



@alumni_rest.route("/alumni",methods=["post"])
def post_person_Alumni():
	form_translator = FormToEntity(Alumni,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Alumni.from_dict(entity_dct)
	created_id = DB_EntityLoader_Alumni().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@alumni_rest.route("/alumni",methods=["put"])
def put_person_Alumni():
	form_translator = FormToEntity(Alumni)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Alumni().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Alumni().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@alumni_rest.route("/alumni",methods=["delete"])
def delete_person_Alumni():
	entity_ = DB_EntityLoader_Alumni().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}


@alumni_rest.route('/maps')
def maps():
	locations = set(df['location'].to_dict().values())
	markers = []; update = False
	with open("coordinates.yml",encoding="utf-8") as file:
		coordinates = yaml.safe_load(file.read())
		for location in locations:
			try:
				if len(coordinates[location]) > 0:
					markers.append(tuple(coordinates[location]))
			except KeyError:
				new_coordinates = get_from_position_stack(location)
				if new_coordinates is not None:
					coordinates[location] = list(new_coordinates); update = True
					markers.append(tuple(coordinates[location]))
	if update:
		with open("coordinates.yml",'w',encoding="utf-8") as file:
			file.write(yaml.dump(coordinates))
	return render_template( 
		"map.html",
		Locations = markers,
	  active_sidebar_item="maps"
	 )
# ** EndSection ** Endpoints