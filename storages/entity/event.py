# ** Section ** Imports
from Temod.storage.mysql import MysqlEntityStorage
from core.entity.event import *
# ** EndSection ** Imports

# ** Section ** EntityStorage_event
class MysqleventStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqleventStorage,self).__init__(event,**kwargs)


# ** EndSection ** EntityStorage_event

