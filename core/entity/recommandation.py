# ** Section ** Imports
from Temod.core.base.entity import Entity
from Temod.core.base.attribute import *
from copy import deepcopy
# ** EndSection ** Imports

# ** Section ** Entity_Recommandation
class Recommandation(Entity):
	ENTITY_NAME = "recommandation"
	ATTRIBUTES = {"IdR":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":True,"is_auto":True,"default_value":None},"idU":{"type":UUID4Attribute,"required":True,"is_id":False,"is_nullable":False,"non_empty":True,"default_value":None},"Titre":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Description":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None}}
	def __init__(self, IdR, IdU, Titre, Description):
		super(Recommandation,self).__init__(IntegerAttribute("IdR",value = IdR,is_id = True,is_nullable = True,is_auto = True,default_value = None),UUID4Attribute("idU",value = idU,is_id = False,is_nullable = False,non_empty = True,default_value = None),StringAttribute("Titre",value = Titre,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Description",value = Description,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Recommandation(dct.pop("IdR"),dct.pop("IdU"),dct.pop("Titre"),dct.pop("Description"))


# ** EndSection ** Entity_Recommandation

