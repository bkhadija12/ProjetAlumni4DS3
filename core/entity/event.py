# ** Section ** Imports
from Temod.core.base.entity import Entity
from Temod.core.base.attribute import *
from copy import deepcopy
# ** EndSection ** Imports

# ** Section ** Entity_event
class event(Entity):
	ENTITY_NAME = "event"
	ATTRIBUTES = {"IdE":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":False,"is_auto":True,"default_value":None},"titre":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"EventDate":{"type":DateAttribute,"required":True,"is_id":False,"is_nullable":False},"Description":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"NbrAttending":{"type":IntegerAttribute,"required":True,"is_id":False,"is_nullable":False,"is_auto":False,"default_value":None},"Organizers":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Adresse":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None}}
	def __init__(self, IdE, titre, EventDate, Description, NbrAttending, Organizers, Adresse):
		super(event,self).__init__(IntegerAttribute("IdE",value = IdE,is_id = True,is_nullable = False,is_auto = True,default_value = None),StringAttribute("titre",value = titre,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),DateAttribute("EventDate",value = EventDate,is_id = False,is_nullable = False),StringAttribute("Description",value = Description,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),IntegerAttribute("NbrAttending",value = NbrAttending,is_id = False,is_nullable = False,is_auto = False,default_value = None),StringAttribute("Organizers",value = Organizers,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Adresse",value = Adresse,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return event(dct.pop("IdE"),dct.pop("titre"),dct.pop("EventDate"),dct.pop("Description"),dct.pop("NbrAttending"),dct.pop("Organizers"),dct.pop("Adresse"))


# ** EndSection ** Entity_event

