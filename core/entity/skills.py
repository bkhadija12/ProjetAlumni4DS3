# ** Section ** Imports
from Temod.core.base.entity import Entity
from Temod.core.base.attribute import *
from copy import deepcopy
# ** EndSection ** Imports

# ** Section ** Entity_Skills
class Skills(Entity):
	ENTITY_NAME = "skills"
	ATTRIBUTES = {"id":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":False,"is_auto":True,"default_value":None},"skill":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None}}
	def __init__(self, id, skill):
		super(Skills,self).__init__(IntegerAttribute("id",value = id,is_id = True,is_nullable = False,is_auto = True,default_value = None),StringAttribute("skill",value = skill,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Skills(dct.pop("id"),dct.pop("skill"))


# ** EndSection ** Entity_Skills

