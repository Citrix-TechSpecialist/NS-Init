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

class systemsshkey(base_resource) :
	def __init__(self) :
		self._name = ""
		self._sshkeytype = ""
		self._src = ""

	@property
	def name(self) :
		ur"""URL \(protocol, host, path, and file name\) from where the location file will be imported.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""URL \(protocol, host, path, and file name\) from where the location file will be imported.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def sshkeytype(self) :
		ur"""The type of the ssh key whether public or private key.<br/>Possible values = PRIVATE, PUBLIC.
		"""
		try :
			return self._sshkeytype
		except Exception as e:
			raise e

	@sshkeytype.setter
	def sshkeytype(self, sshkeytype) :
		ur"""The type of the ssh key whether public or private key.<br/>Possible values = PRIVATE, PUBLIC
		"""
		try :
			self._sshkeytype = sshkeytype
		except Exception as e:
			raise e

	@property
	def src(self) :
		ur"""URL \(protocol, host, path, and file name\) from where the location file will be imported.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._src
		except Exception as e:
			raise e

	@src.setter
	def src(self, src) :
		ur"""URL \(protocol, host, path, and file name\) from where the location file will be imported.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._src = src
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemsshkey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemsshkey
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
	def delete(cls, client, resource) :
		ur""" Use this API to delete systemsshkey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = systemsshkey()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
					deleteresource.sshkeytype = resource.sshkeytype
				return deleteresource.delete_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def Import(cls, client, resource) :
		ur""" Use this API to Import systemsshkey.
		"""
		try :
			if type(resource) is not list :
				Importresource = systemsshkey()
				Importresource.name = resource.name
				Importresource.src = resource.src
				Importresource.sshkeytype = resource.sshkeytype
				return Importresource.perform_operation(client,"Import")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the systemsshkey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemsshkey()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the systemsshkey resources that are configured on netscaler.
	# This uses systemsshkey_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = systemsshkey()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Sshkeytype:
		PRIVATE = "PRIVATE"
		PUBLIC = "PUBLIC"

class systemsshkey_response(base_response) :
	def __init__(self, length=1) :
		self.systemsshkey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemsshkey = [systemsshkey() for _ in range(length)]

