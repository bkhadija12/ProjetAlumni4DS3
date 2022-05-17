# ** Section ** Imports
from Temod.core.base.entity import Entity
from Temod.core.base.attribute import *
from copy import deepcopy
# ** EndSection ** Imports

# ** Section ** Entity_Job
class Job(Entity):
	ENTITY_NAME = "job"
	ATTRIBUTES = {"IDJob":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":False,"is_auto":True,"default_value":None},"Job_funtion":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Description":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Country_of_work":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Salary":{"type":RealAttribute,"required":False,"is_id":False,"is_nullable":True,"default_value":None},"Seniority_level":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Company_name":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None}}
	def __init__(self, IDJob, Job_funtion, Description, Country_of_work, Seniority_level, Company_name,Salary=None):
		super(Job,self).__init__(IntegerAttribute("IDJob",value = IDJob,is_id = True,is_nullable = False,is_auto = True,default_value = None),StringAttribute("Job_funtion",value = Job_funtion,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Description",value = Description,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Country_of_work",value = Country_of_work,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),RealAttribute("Salary",value = Salary,is_id = False,is_nullable = True,default_value = None),StringAttribute("Seniority_level",value = Seniority_level,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Company_name",value = Company_name,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Job(dct.pop("IDJob"),dct.pop("Job_funtion"),dct.pop("Description"),dct.pop("Country_of_work"),dct.pop("Seniority_level"),dct.pop("Company_name"),**dct)


# ** EndSection ** Entity_Job

