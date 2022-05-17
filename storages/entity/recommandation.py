# ** Section ** Imports
from Temod.storage.mysql import MysqlEntityStorage
from core.entity.recommandation import *
# ** EndSection ** Imports

# ** Section ** EntityStorage_Recommandation
class MysqlRecommandationStorage(MysqlEntityStorage):
	def __init__(self, **kwargs):
		super(MysqlRecommandationStorage,self).__init__(Recommandation,**kwargs)


# ** EndSection ** EntityStorage_Recommandation

