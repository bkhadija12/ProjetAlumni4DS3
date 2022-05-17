# ** Section ** Imports
from Temod.storage.mysql import MysqlEntityStorage
from core.entity.user import *
# ** EndSection ** Imports

# ** Section ** EntityStorage_User
class MysqlUserStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlUserStorage,self).__init__(User,**kwargs)

	def byLogins(self, username, password):
		return self.get(User.ATTRIBUTES['Email']['type']('Email',value=username),User.ATTRIBUTES['Password']['type']('Password',value=password),)

	def setLoggedIn(self, userAccount):
		userAccount.setAttribute("is_active",True)
		userAccount.setAttribute("is_authenticated",True)
		self.update(userAccount,attributes=["is_authenticated","is_active"])
		return userAccount

	def setLoggedOut(self, userAccount):
		userAccount.setAttribute("is_active",False)
		userAccount.setAttribute("is_authenticated",False)
		self.update(userAccount,attributes=["is_authenticated","is_active"])
		return userAccount


# ** EndSection ** EntityStorage_User

# ** Section ** EntityStorage_Userskills
class MysqlUserskillsStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlUserskillsStorage,self).__init__(Userskills,**kwargs)


# ** EndSection ** EntityStorage_Userskills

# ** Section ** EntityStorage_Userevent
class MysqlUsereventStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlUsereventStorage,self).__init__(Userevent,**kwargs)


# ** EndSection ** EntityStorage_Userevent

# ** Section ** EntityStorage_Userjob
class MysqlUserjobStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlUserjobStorage,self).__init__(Userjob,**kwargs)


# ** EndSection ** EntityStorage_Userjob

