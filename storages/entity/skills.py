# ** Section ** Imports
from Temod.storage.mysql import MysqlEntityStorage
from core.entity.skills import *
# ** EndSection ** Imports

# ** Section ** EntityStorage_Skills
class MysqlSkillsStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlSkillsStorage,self).__init__(Skills,**kwargs)


# ** EndSection ** EntityStorage_Skills

