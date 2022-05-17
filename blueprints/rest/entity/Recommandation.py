# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from context import DB_EntityLoader_Recommandation
from flask import Blueprint,request,abort,render_template
import traceback
from recommandation import similar_jobs,recommendations

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
recommandation_rest = Blueprint('recommandation_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@recommandation_rest.route("/recommandation",methods=["get"])
def get_recommandation_Recommandation():
	jobrecommandation=similar_jobs('France')
	skillrecommandation= recommendations('python html mysql css laravel')
	print(skillrecommandation)
	return render_template( 
		"recommandation/index_recommandation.html", 
		JobRecommandation = jobrecommandation,
		SkillRecommandation = skillrecommandation,
		active_sidebar_item="Recommandation"
	 )



@recommandation_rest.route("/recommandation",methods=["post"])
def post_recommandation_Recommandation():
	form_translator = FormToEntity(Recommandation,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Recommandation.from_dict(entity_dct)
	created_id = DB_EntityLoader_Recommandation().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@recommandation_rest.route("/recommandation",methods=["put"])
def put_recommandation_Recommandation():
	form_translator = FormToEntity(Recommandation)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Recommandation().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Recommandation().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@recommandation_rest.route("/recommandation",methods=["delete"])
def delete_recommandation_Recommandation():
	entity_ = DB_EntityLoader_Recommandation().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}



# ** EndSection ** Endpoints