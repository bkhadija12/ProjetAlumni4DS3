# ** Section ** Imports
from flask import render_template

from security.authority import Gardian, LawBookGardian, YamlLawBookKeeper, TimedRotatingJsonFileAlarm
from security.authentification.flask import DefaultFlaskAuthenticator

from core.entity.user import *
from datetime import date

import os
# ** EndSection ** Imports

# ** Section ** AppSetups
HOST = '127.0.0.1'
PORT = 4542
THREADED = True
DEBUG = True
POSITIONSTACK_API_KEY = "406171c4a0979b2c63120809321346bb"
# ** EndSection ** AppSetups

# ** Section ** Authentification
AUTHENTICATOR = DefaultFlaskAuthenticator(
	User,
	anonymous_attributes={
		"IdU":"00000000-0000-0000-0000-000000000000", 
		"Nom":"a",
		"Prenom":"a",
		"Email":"a",
		"Password":"a",
		"Birthday":date.today(),
		"Adresse":"a",
		"persontype":-1
	}
)
# ** EndSection ** Authentification



# ** Section ** AccessRightsManagement
GARDIAN_LOGGING_FILE = os.path.join('logs','security','grd')
GARDIAN = LawBookGardian(
	YamlLawBookKeeper('access.yml','.').load(),
	lambda user:user.persontype,
	index=lambda right: right.symbol,
	alarm=TimedRotatingJsonFileAlarm(
		GARDIAN_LOGGING_FILE,
		logger_name='gardian',
		default_state="warning"
	),
	strict=True
)

FRONT_DESK_LOGGING_FILE = os.path.join('logs','security','grd')
FRONT_DESK = Gardian(
	alarm=TimedRotatingJsonFileAlarm(
		FRONT_DESK_LOGGING_FILE,
		logger_name='front_desk',
		default_state="warning"
	),
	strict=True
)
# ** EndSection ** AccessRightsManagement

# ** Section ** MysqlDatabases
PROJETDS_CREDENTIALS = {'host': '127.0.0.1', 'port': '3306', 'user': 'root', 'password': '3Ounder3O$', 'database': 'projetds'}
# ** EndSection ** MysqlDatabases

