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

class systemkek(base_resource) :
	def __init__(self) :
		self._passphrase = ""
		self._password = ""

	@property
	def passphrase(self) :
		ur"""Passphrase required to generate the key encryption key.<br/>Minimum length =  8<br/>Maximum length =  32.
		"""
		try :
			return self._passphrase
		except Exception as e:
			raise e

	@passphrase.setter
	def passphrase(self, passphrase) :
		ur"""Passphrase required to generate the key encryption key.<br/>Minimum length =  8<br/>Maximum length =  32
		"""
		try :
			self._passphrase = passphrase
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password required to import the key encryption key.<br/>Minimum length =  8<br/>Maximum length =  32.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password required to import the key encryption key.<br/>Minimum length =  8<br/>Maximum length =  32
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemkek_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemkek
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.passphrase is not None :
				return str(self.passphrase)
			return None
		except Exception as e :
			raise e



	@classmethod
	def create(cls, client, resource) :
		ur""" Use this API to create systemkek.
		"""
		try :
			if type(resource) is not list :
				createresource = systemkek()
				createresource.passphrase = resource.passphrase
				return createresource.perform_operation(client,"create")
		except Exception as e :
			raise e

	@classmethod
	def export(cls, client, resource) :
		ur""" Use this API to export systemkek.
		"""
		try :
			if type(resource) is not list :
				exportresource = systemkek()
				exportresource.password = resource.password
				return exportresource.perform_operation(client,"export")
		except Exception as e :
			raise e

	@classmethod
	def Import(cls, client, resource) :
		ur""" Use this API to Import systemkek.
		"""
		try :
			if type(resource) is not list :
				Importresource = systemkek()
				Importresource.password = resource.password
				return Importresource.perform_operation(client,"Import")
		except Exception as e :
			raise e

class systemkek_response(base_response) :
	def __init__(self, length=1) :
		self.systemkek = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemkek = [systemkek() for _ in range(length)]

