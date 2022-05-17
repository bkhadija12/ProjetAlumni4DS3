# ** Section ** Imports
from Temod.storage.mysql import MysqlEntityStorage
from core.entity.notification import *
# ** EndSection ** Imports

# ** Section ** EntityStorage_Notification
class MysqlNotificationStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlNotificationStorage,self).__init__(Notification,**kwargs)


# ** EndSection ** EntityStorage_Notification

