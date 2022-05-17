# ** Section ** Imports
from Temod.core.base.entity import Entity
from Temod.core.base.attribute import *
from copy import deepcopy
# ** EndSection ** Imports

# ** Section ** Entity_User
class User(Entity):
	ENTITY_NAME = "user"
	ATTRIBUTES = {"IdU":{"type":UUID4Attribute,"required":True,"is_id":True,"is_nullable":False,"non_empty":True,"default_value":None},"is_authenticated":{"type":BooleanAttribute,"is_nullable":False,"default_value":False},"is_active":{"type":BooleanAttribute,"is_nullable":False,"default_value":False},"Nom":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Prenom":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Email":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Password":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None},"Birthday":{"type":DateAttribute,"required":True,"is_id":False,"is_nullable":False},"Adresse":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":True,"default_value":"Tunis"},"persontype":{"type":IntegerAttribute,"required":True,"is_id":False,"is_nullable":False,"is_auto":False,"default_value":None}}
	def __init__(self, IdU, Nom, Prenom, Email, Password, Birthday, Adresse, persontype,is_authenticated=False, is_active=False):
		super(User,self).__init__(UUID4Attribute("IdU",value = IdU,is_id = True,is_nullable = False,non_empty = True,default_value = None),StringAttribute("Nom",value = Nom,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Prenom",value = Prenom,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Email",value = Email,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),StringAttribute("Password",value = Password,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None),DateAttribute("Birthday",value = Birthday,is_id = False,is_nullable = False),StringAttribute("Adresse",value = Adresse,is_id = False,non_empty = True,force_lower_case = True,is_nullable = True,default_value = "tunis"),IntegerAttribute("persontype",value = persontype,is_id = False,is_nullable = False,is_auto = False,default_value = None),BooleanAttribute("is_authenticated",value = is_authenticated,is_nullable = False,default_value = False),BooleanAttribute("is_active",value = is_active,is_nullable = False,default_value = False))

	def get_id(self):
		return self.IdU
		
	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return User(dct.pop("IdU"),dct.pop("Nom"),dct.pop("Prenom"),dct.pop("Email"),dct.pop("Password"),dct.pop("Birthday"),dct.pop("Adresse"),dct.pop("persontype"),**dct)


# ** EndSection ** Entity_User

# ** Section ** Entity_Userskills
class Userskills(Entity):
	ENTITY_NAME = "userskills"
	ATTRIBUTES = {"idU":{"type":UUID4Attribute,"required":True,"is_id":False,"is_nullable":False,"non_empty":True,"default_value":None},"idS":{"type":IntegerAttribute,"required":True,"is_id":False,"is_nullable":False,"is_auto":False,"default_value":None}}
	def __init__(self, idU, idS):
		super(Userskills,self).__init__(UUID4Attribute("idU",value = idU,is_id = False,is_nullable = False,non_empty = True,default_value = None),IntegerAttribute("idS",value = idS,is_id = False,is_nullable = False,is_auto = False,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Userskills(dct.pop("idU"),dct.pop("idS"))


# ** EndSection ** Entity_Userskills

# ** Section ** Entity_Userevent
class Userevent(Entity):
	ENTITY_NAME = "userevent"
	ATTRIBUTES = {"idE":{"type":IntegerAttribute,"required":True,"is_id":False,"is_nullable":False,"is_auto":False,"default_value":None},"idU":{"type":UUID4Attribute,"required":True,"is_id":False,"is_nullable":False,"non_empty":True,"default_value":None}}
	def __init__(self, idE, idU):
		super(Userevent,self).__init__(IntegerAttribute("idE",value = idE,is_id = False,is_nullable = False,is_auto = False,default_value = None),UUID4Attribute("idU",value = idU,is_id = False,is_nullable = False,non_empty = True,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Userevent(dct.pop("idE"),dct.pop("idU"))


# ** EndSection ** Entity_Userevent

# ** Section ** Entity_Userjob
class Userjob(Entity):
	ENTITY_NAME = "userjob"
	ATTRIBUTES = {"idJ":{"type":IntegerAttribute,"required":True,"is_id":False,"is_nullable":False,"is_auto":False,"default_value":None},"idU":{"type":UUID4Attribute,"required":True,"is_id":False,"is_nullable":False,"non_empty":True,"default_value":None}}
	def __init__(self, idJ, idU):
		super(Userjob,self).__init__(IntegerAttribute("idJ",value = idJ,is_id = False,is_nullable = False,is_auto = False,default_value = None),UUID4Attribute("idU",value = idU,is_id = False,is_nullable = False,non_empty = True,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Userjob(dct.pop("idJ"),dct.pop("idU"))


# ** EndSection ** Entity_Userjob

