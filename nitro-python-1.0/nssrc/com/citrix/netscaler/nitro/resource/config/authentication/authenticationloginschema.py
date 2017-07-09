#
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class authenticationloginschema(base_resource) :
	def __init__(self) :
		self._name = ""
		self._authenticationschema = ""
		self._userexpression = ""
		self._passwdexpression = ""
		self._usercredentialindex = 0
		self._passwordcredentialindex = 0
		self._authenticationstrength = 0
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the new login schema. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the new login schema. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def authenticationschema(self) :
		ur"""Name of the file for reading authentication schema to be sent for Login Page UI. This file should contain xml definition of elements as per Citrix Forms Authentication Protocol to be able to render login form. If administrator does not want to prompt users for additional credentials but continue with previously obtained credentials, then "noschema" can be given as argument. Please note that this applies only to loginSchemas that are used with user-defined factors, and not the vserver factor.<br/>Minimum length =  1.
		"""
		try :
			return self._authenticationschema
		except Exception as e:
			raise e

	@authenticationschema.setter
	def authenticationschema(self, authenticationschema) :
		ur"""Name of the file for reading authentication schema to be sent for Login Page UI. This file should contain xml definition of elements as per Citrix Forms Authentication Protocol to be able to render login form. If administrator does not want to prompt users for additional credentials but continue with previously obtained credentials, then "noschema" can be given as argument. Please note that this applies only to loginSchemas that are used with user-defined factors, and not the vserver factor.<br/>Minimum length =  1
		"""
		try :
			self._authenticationschema = authenticationschema
		except Exception as e:
			raise e

	@property
	def userexpression(self) :
		ur"""Expression for username extraction during login.<br/>Minimum length =  1.
		"""
		try :
			return self._userexpression
		except Exception as e:
			raise e

	@userexpression.setter
	def userexpression(self, userexpression) :
		ur"""Expression for username extraction during login.<br/>Minimum length =  1
		"""
		try :
			self._userexpression = userexpression
		except Exception as e:
			raise e

	@property
	def passwdexpression(self) :
		ur"""Expression for password extraction during login.<br/>Minimum length =  1.
		"""
		try :
			return self._passwdexpression
		except Exception as e:
			raise e

	@passwdexpression.setter
	def passwdexpression(self, passwdexpression) :
		ur"""Expression for password extraction during login.<br/>Minimum length =  1
		"""
		try :
			self._passwdexpression = passwdexpression
		except Exception as e:
			raise e

	@property
	def usercredentialindex(self) :
		ur"""The index at which user entered username should be stored in session.<br/>Minimum length =  1<br/>Maximum length =  16.
		"""
		try :
			return self._usercredentialindex
		except Exception as e:
			raise e

	@usercredentialindex.setter
	def usercredentialindex(self, usercredentialindex) :
		ur"""The index at which user entered username should be stored in session.<br/>Minimum length =  1<br/>Maximum length =  16
		"""
		try :
			self._usercredentialindex = usercredentialindex
		except Exception as e:
			raise e

	@property
	def passwordcredentialindex(self) :
		ur"""The index at which user entered password should be stored in session.<br/>Minimum length =  1<br/>Maximum length =  16.
		"""
		try :
			return self._passwordcredentialindex
		except Exception as e:
			raise e

	@passwordcredentialindex.setter
	def passwordcredentialindex(self, passwordcredentialindex) :
		ur"""The index at which user entered password should be stored in session.<br/>Minimum length =  1<br/>Maximum length =  16
		"""
		try :
			self._passwordcredentialindex = passwordcredentialindex
		except Exception as e:
			raise e

	@property
	def authenticationstrength(self) :
		ur"""Weight of the current authentication.<br/>Maximum length =  65535.
		"""
		try :
			return self._authenticationstrength
		except Exception as e:
			raise e

	@authenticationstrength.setter
	def authenticationstrength(self, authenticationstrength) :
		ur"""Weight of the current authentication.<br/>Maximum length =  65535
		"""
		try :
			self._authenticationstrength = authenticationstrength
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationloginschema_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationloginschema
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add authenticationloginschema.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationloginschema()
				addresource.name = resource.name
				addresource.authenticationschema = resource.authenticationschema
				addresource.userexpression = resource.userexpression
				addresource.passwdexpression = resource.passwdexpression
				addresource.usercredentialindex = resource.usercredentialindex
				addresource.passwordcredentialindex = resource.passwordcredentialindex
				addresource.authenticationstrength = resource.authenticationstrength
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationloginschema() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].authenticationschema = resource[i].authenticationschema
						addresources[i].userexpression = resource[i].userexpression
						addresources[i].passwdexpression = resource[i].passwdexpression
						addresources[i].usercredentialindex = resource[i].usercredentialindex
						addresources[i].passwordcredentialindex = resource[i].passwordcredentialindex
						addresources[i].authenticationstrength = resource[i].authenticationstrength
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete authenticationloginschema.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationloginschema()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationloginschema() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationloginschema() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update authenticationloginschema.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationloginschema()
				updateresource.name = resource.name
				updateresource.authenticationschema = resource.authenticationschema
				updateresource.userexpression = resource.userexpression
				updateresource.passwdexpression = resource.passwdexpression
				updateresource.usercredentialindex = resource.usercredentialindex
				updateresource.passwordcredentialindex = resource.passwordcredentialindex
				updateresource.authenticationstrength = resource.authenticationstrength
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationloginschema() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].authenticationschema = resource[i].authenticationschema
						updateresources[i].userexpression = resource[i].userexpression
						updateresources[i].passwdexpression = resource[i].passwdexpression
						updateresources[i].usercredentialindex = resource[i].usercredentialindex
						updateresources[i].passwordcredentialindex = resource[i].passwordcredentialindex
						updateresources[i].authenticationstrength = resource[i].authenticationstrength
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of authenticationloginschema resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationloginschema()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationloginschema() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationloginschema() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the authenticationloginschema resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationloginschema()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = authenticationloginschema()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [authenticationloginschema() for _ in range(len(name))]
							obj = [authenticationloginschema() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = authenticationloginschema()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of authenticationloginschema resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationloginschema()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the authenticationloginschema resources configured on NetScaler.
		"""
		try :
			obj = authenticationloginschema()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of authenticationloginschema resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationloginschema()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

class authenticationloginschema_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationloginschema = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationloginschema = [authenticationloginschema() for _ in range(length)]

