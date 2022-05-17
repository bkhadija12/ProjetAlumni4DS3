# ** Section ** Imports
from storages.entity.recommandation import MysqlRecommandationStorage
from storages.entity.notification import MysqlNotificationStorage
from storages.entity.person import MysqlPersontypeStorage
from storages.entity.user import MysqlUserskillsStorage
from storages.entity.person import MysqlStudentStorage
from storages.entity.user import MysqlUsereventStorage
from storages.entity.person import MysqlAlumniStorage
from storages.entity.skills import MysqlSkillsStorage
from storages.entity.person import MysqlAdminStorage
from storages.entity.user import MysqlUserjobStorage
from storages.entity.event import MysqleventStorage
from storages.entity.user import MysqlUserStorage
from storages.entity.job import MysqlJobStorage
from functools import partial
from flask import g
import configs
# ** EndSection ** Imports

# ** Section ** Predefined
def __DBRegister(dbName, dbObj):
	try:
		g.databases.append(dbName)
	except:
		g.databases = [dbName]
	setattr(g,dbName,dbObj)

def __DBInitializer(dbclass, *dbargs, **dbkwargs):
	if not (dbclass.__name__ in g):
		__DBRegister(dbclass.__name__,dbclass(*dbargs,**dbkwargs))
	return getattr(g,dbclass.__name__)

# ** EndSection ** Predefined

# ** Section ** DBInitializations_entities
DB_EntityLoader_Notification = partial(__DBInitializer,MysqlNotificationStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_event = partial(__DBInitializer,MysqleventStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_Job = partial(__DBInitializer,MysqlJobStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_Admin = partial(__DBInitializer,MysqlAdminStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_Alumni = partial(__DBInitializer,MysqlAlumniStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_Student = partial(__DBInitializer,MysqlStudentStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_Recommandation = partial(__DBInitializer,MysqlRecommandationStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_Skills = partial(__DBInitializer,MysqlSkillsStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_User = partial(__DBInitializer,MysqlUserStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_Userevent = partial(__DBInitializer,MysqlUsereventStorage,**configs.PROJETDS_CREDENTIALS)
DB_EntityLoader_Userjob = partial(__DBInitializer,MysqlUserjobStorage,**configs.PROJETDS_CREDENTIALS)
# ** EndSection ** DBInitializations_entities

