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

class lsnsipalgcall_binding(base_resource):
	""" Binding class showing the resources that can be bound to lsnsipalgcall_binding. 
	"""
	def __init__(self) :
		self._callid = ""
		self.lsnsipalgcall_datachannel_binding = []
		self.lsnsipalgcall_controlchannel_binding = []

	@property
	def callid(self) :
		ur"""Call ID for the SIP call.
		"""
		try :
			return self._callid
		except Exception as e:
			raise e

	@callid.setter
	def callid(self, callid) :
		ur"""Call ID for the SIP call.
		"""
		try :
			self._callid = callid
		except Exception as e:
			raise e

	@property
	def lsnsipalgcall_controlchannel_bindings(self) :
		ur"""controlchannel that can be bound to lsnsipalgcall.
		"""
		try :
			return self._lsnsipalgcall_controlchannel_binding
		except Exception as e:
			raise e

	@property
	def lsnsipalgcall_datachannel_bindings(self) :
		ur"""datachannel that can be bound to lsnsipalgcall.
		"""
		try :
			return self._lsnsipalgcall_datachannel_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnsipalgcall_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnsipalgcall_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.callid is not None :
				return str(self.callid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, callid) :
		ur""" Use this API to fetch lsnsipalgcall_binding resource.
		"""
		try :
			if type(callid) is not list :
				obj = lsnsipalgcall_binding()
				obj.callid = callid
				response = obj.get_resource(service)
			else :
				if callid and len(callid) > 0 :
					obj = [lsnsipalgcall_binding() for _ in range(len(callid))]
					for i in range(len(callid)) :
						obj[i].callid = callid[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class lsnsipalgcall_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsnsipalgcall_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnsipalgcall_binding = [lsnsipalgcall_binding() for _ in range(length)]

