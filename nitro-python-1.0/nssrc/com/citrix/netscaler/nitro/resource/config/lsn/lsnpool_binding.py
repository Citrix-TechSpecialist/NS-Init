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

class lsnpool_binding(base_resource):
	""" Binding class showing the resources that can be bound to lsnpool_binding. 
	"""
	def __init__(self) :
		self._poolname = ""
		self.lsnpool_lsnip_binding = []

	@property
	def poolname(self) :
		ur"""Name for the LSN pool. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN pool is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn pool1" or 'lsn pool1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._poolname
		except Exception as e:
			raise e

	@poolname.setter
	def poolname(self, poolname) :
		ur"""Name for the LSN pool. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN pool is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn pool1" or 'lsn pool1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._poolname = poolname
		except Exception as e:
			raise e

	@property
	def lsnpool_lsnip_bindings(self) :
		ur"""lsnip that can be bound to lsnpool.
		"""
		try :
			return self._lsnpool_lsnip_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnpool_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnpool_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.poolname is not None :
				return str(self.poolname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, poolname) :
		ur""" Use this API to fetch lsnpool_binding resource.
		"""
		try :
			if type(poolname) is not list :
				obj = lsnpool_binding()
				obj.poolname = poolname
				response = obj.get_resource(service)
			else :
				if poolname and len(poolname) > 0 :
					obj = [lsnpool_binding() for _ in range(len(poolname))]
					for i in range(len(poolname)) :
						obj[i].poolname = poolname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class lsnpool_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsnpool_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnpool_binding = [lsnpool_binding() for _ in range(length)]

