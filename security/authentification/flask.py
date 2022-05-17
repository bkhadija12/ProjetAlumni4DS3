from flask_login import LoginManager
from functools import partial
import traceback

from .exceptions import *

class DefaultFlaskAuthenticator(LoginManager):
	"""docstring for DefaultFlaskAuthenticator"""
	def __init__(self, user_class, user_loader=None, anonymous_attributes=None, postload=None, login_view="login", **kwargs):
		super(DefaultFlaskAuthenticator, self).__init__(**kwargs)
		self.user_class = user_class
		self.login_view = login_view
		
		if anonymous_attributes is None:
			self.anonymous_user = self.user_class
		else:
			self.anonymous_user = partial(self.user_class.from_dict,anonymous_attributes,copy=True)

		self.postload = None; self.loading_function = None;
		if user_loader is not None:
			self.setLoader(user_loader)

		if postload is not None:
			self.setPostLoader(postload)

	def setLoader(self,user_loader):
		try:
			assert(hasattr(user_loader,"__call__"))
		except:
			raise MalformedAuthenticatorError("The user loader must be a callable object.")
		self.loading_function = user_loader
		@self.user_loader
		def load_user(userID):
			loaded_user = self.loading_function(userID)
			print(loaded_user)
			if loaded_user is None or self.postload is None:
				return loaded_user
			return self.postload(loaded_user)

	def setPostLoader(self,post_loader):
		try:
			assert(hasattr(post_loader,"__call__"))
		except:
			raise MalformedAuthenticatorError("The user post loader must be a callable object.")
		self.postload = post_loader

		