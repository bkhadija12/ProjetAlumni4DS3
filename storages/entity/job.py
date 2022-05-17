# ** Section ** Imports
from Temod.storage.mysql import MysqlEntityStorage
from core.entity.job import *
# ** EndSection ** Imports

# ** Section ** EntityStorage_Job
class MysqlJobStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlJobStorage,self).__init__(Job,**kwargs)


# ** EndSection ** EntityStorage_Job

