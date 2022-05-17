# ** Section ** Imports
from Temod.core.base.entity import Entity
from Temod.core.base.attribute import *
from copy import deepcopy
# ** EndSection ** Imports

# ** Section ** Entity_Persontype
class Persontype(Entity):
	ENTITY_NAME = "persontype"
	ATTRIBUTES = {"PersonTypeID":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":False,"is_auto":False,"default_value":None},"PersonType":{"type":StringAttribute,"required":True,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None}}
	def __init__(self, PersonTypeID, PersonType):
		super(Persontype,self).__init__(IntegerAttribute("PersonTypeID",value = PersonTypeID,is_id = True,is_nullable = False,is_auto = False,default_value = None),StringAttribute("PersonType",value = PersonType,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Persontype(dct.pop("PersonTypeID"),dct.pop("PersonType"))


# ** EndSection ** Entity_Persontype

# ** Section ** Entity_Admin
class Admin(Entity):
	ENTITY_NAME = "admin"
	ATTRIBUTES = {"IdU":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":False,"is_auto":False,"default_value":None},"HireDate":{"type":DateTimeAttribute,"required":False,"is_id":False,"is_nullable":True}}
	def __init__(self, IdU,HireDate=None):
		super(Admin,self).__init__(IntegerAttribute("IdU",value = IdU,is_id = True,is_nullable = False,is_auto = False,default_value = None),DateTimeAttribute("HireDate",value = HireDate,is_id = False,is_nullable = True))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Admin(dct.pop("IdU"),**dct)


# ** EndSection ** Entity_Admin

# ** Section ** Entity_Alumni
class Alumni(Entity):
	ENTITY_NAME = "alumni"
	ATTRIBUTES = {"IdU":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":False,"is_auto":False,"default_value":None},"PromotionDate":{"type":DateAttribute,"required":False,"is_id":False,"is_nullable":True}}
	def __init__(self, IdU,PromotionDate=None):
		super(Alumni,self).__init__(IntegerAttribute("IdU",value = IdU,is_id = True,is_nullable = False,is_auto = False,default_value = None),DateAttribute("PromotionDate",value = PromotionDate,is_id = False,is_nullable = True))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Alumni(dct.pop("IdU"),**dct)


# ** EndSection ** Entity_Alumni

# ** Section ** Entity_Student
class Student(Entity):
	ENTITY_NAME = "student"
	ATTRIBUTES = {"IdU":{"type":IntegerAttribute,"required":True,"is_id":True,"is_nullable":False,"is_auto":False,"default_value":None},"HireDate":{"type":DateAttribute,"required":False,"is_id":False,"is_nullable":True},"speciality":{"type":StringAttribute,"required":False,"is_id":False,"non_empty":True,"force_lower_case":True,"is_nullable":False,"default_value":None}}
	def __init__(self, IdU,HireDate=None, speciality=None):
		super(Student,self).__init__(IntegerAttribute("IdU",value = IdU,is_id = True,is_nullable = False,is_auto = False,default_value = None),DateAttribute("HireDate",value = HireDate,is_id = False,is_nullable = True),StringAttribute("speciality",value = speciality,is_id = False,non_empty = True,force_lower_case = True,is_nullable = False,default_value = None))

	def from_dict(dct,copy=False):
		dct = deepcopy(dct) if copy else dct
		return Student(dct.pop("IdU"),**dct)


# ** EndSection ** Entity_Student

