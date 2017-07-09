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

class lsnclient_binding(base_resource):
	""" Binding class showing the resources that can be bound to lsnclient_binding. 
	"""
	def __init__(self) :
		self._clientname = ""
		self.lsnclient_network6_binding = []
		self.lsnclient_nsacl6_binding = []
		self.lsnclient_network_binding = []
		self.lsnclient_nsacl_binding = []

	@property
	def clientname(self) :
		ur"""Name for the LSN client entity. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN client is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn client1" or 'lsn client1'). .<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._clientname
		except Exception as e:
			raise e

	@clientname.setter
	def clientname(self, clientname) :
		ur"""Name for the LSN client entity. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN client is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn client1" or 'lsn client1'). .<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._clientname = clientname
		except Exception as e:
			raise e

	@property
	def lsnclient_nsacl6_bindings(self) :
		ur"""nsacl6 that can be bound to lsnclient.
		"""
		try :
			return self._lsnclient_nsacl6_binding
		except Exception as e:
			raise e

	@property
	def lsnclient_network_bindings(self) :
		ur"""network that can be bound to lsnclient.
		"""
		try :
			return self._lsnclient_network_binding
		except Exception as e:
			raise e

	@property
	def lsnclient_nsacl_bindings(self) :
		ur"""nsacl that can be bound to lsnclient.
		"""
		try :
			return self._lsnclient_nsacl_binding
		except Exception as e:
			raise e

	@property
	def lsnclient_network6_bindings(self) :
		ur"""network6 that can be bound to lsnclient.
		"""
		try :
			return self._lsnclient_network6_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnclient_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnclient_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.clientname is not None :
				return str(self.clientname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, clientname) :
		ur""" Use this API to fetch lsnclient_binding resource.
		"""
		try :
			if type(clientname) is not list :
				obj = lsnclient_binding()
				obj.clientname = clientname
				response = obj.get_resource(service)
			else :
				if clientname and len(clientname) > 0 :
					obj = [lsnclient_binding() for _ in range(len(clientname))]
					for i in range(len(clientname)) :
						obj[i].clientname = clientname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class lsnclient_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsnclient_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnclient_binding = [lsnclient_binding() for _ in range(length)]

