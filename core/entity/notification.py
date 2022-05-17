# ** Section ** Imports
from Temod.core.base.entity import Entity
from Temod.core.base.attribute import *
from copy import deepcopy
# ** EndSection ** Imports

# ** Section ** Entity_Notification
class Notification(Entity):
	ENTITY_NAME = "notification"
	ATTRIBUTES = {"IdN":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":False,"is_auto":True,"default_value":None},"Type":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Description":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None}}
	def __init__(self, IdN, Type, Description):
		super(Notification,self).__init__(IntegerAttribute("IdN",value = IdN,is_id = True,is_nullable = False,is_auto = True,default_value = None),StringAttribute("Type",value = Type,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Description",value = Description,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Notification(dct.pop("IdN"),dct.pop("Type"),dct.pop("Description"))


# ** EndSection ** Entity_Notification

