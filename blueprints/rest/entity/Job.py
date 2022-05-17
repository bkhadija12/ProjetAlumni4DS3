# ** Section ** Imports
from Temod.core.forms.formToEntity import FormToEntity
from flask import Blueprint,request,abort,render_template
from context import DB_EntityLoader_Job
import traceback

# ** EndSection ** Imports

# ** Section ** Blueprint Settings
job_rest = Blueprint('job_rest', __name__)
# ** EndSection ** Blueprint Settings

# ** Section ** Endpoints
@job_rest.route("/jobs",methods=["get"])
def get_job_Job():
		return render_template( 
		"jobs/index_job.html", 
	   active_sidebar_item="jobs"
	 )
@job_rest.route("/job")
def get_add_Job():
		return render_template( 
		"jobs/addJob.html",  
	   active_sidebar_item="jobs"
	 )


@job_rest.route("/job",methods=["post"])
def post_job_Job():
	form_translator = FormToEntity(Job,if_incomplete = "raise")
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = Job.from_dict(entity_dct)
	created_id = DB_EntityLoader_Job().create(entity_)
	if created_id is None:
		return {"status":"error","data":None}
	return {"status":"ok","data":created_id}



@job_rest.route("/job",methods=["put"])
def put_job_Job():
	form_translator = FormToEntity(Job)
	entity_dct = form_translator.to_dict({} if request.form is None else dict(request.form))
	entity_ = DB_EntityLoader_Job().get().takeSnapshot()
	if entity_ is None:
		return abort(404)
	for (key,value) in entity_dct.items():
		DB_EntityLoader_Job().setAttribute(key,value)
	updated_id = entity_.updateOnSnapshot(entity_)
	return {"status":"ok","data":updated_id}



@job_rest.route("/job",methods=["delete"])
def delete_job_Job():
	entity_ = DB_EntityLoader_Job().delete()
	if entity_ is None:
		return abort(404)
	return {"status":"ok","data":entity_.to_dict()}

@job_rest.route("/market")
def market_job_Job():
	return render_template( 
		"jobs/jobmarket.html", 
		active_sidebar_item="jobmarket"
	 
	 )

# ** EndSection ** Endpoints