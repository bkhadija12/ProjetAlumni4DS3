# ** Section ** Imports
from Temod.storage.mysql import MysqlEntityStorage
from core.entity.person import *
# ** EndSection ** Imports

# ** Section ** EntityStorage_Persontype
class MysqlPersontypeStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlPersontypeStorage,self).__init__(Persontype,**kwargs)


# ** EndSection ** EntityStorage_Persontype

# ** Section ** EntityStorage_Admin
class MysqlAdminStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlAdminStorage,self).__init__(Admin,**kwargs)


# ** EndSection ** EntityStorage_Admin

# ** Section ** EntityStorage_Alumni
class MysqlAlumniStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlAlumniStorage,self).__init__(Alumni,**kwargs)


# ** EndSection ** EntityStorage_Alumni

# ** Section ** EntityStorage_Student
class MysqlStudentStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlStudentStorage,self).__init__(Student,**kwargs)


# ** EndSection ** EntityStorage_Student

