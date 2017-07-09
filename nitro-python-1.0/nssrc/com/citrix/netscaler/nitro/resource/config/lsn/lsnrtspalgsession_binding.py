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

class lsnrtspalgsession_binding(base_resource):
	""" Binding class showing the resources that can be bound to lsnrtspalgsession_binding. 
	"""
	def __init__(self) :
		self._sessionid = ""
		self.lsnrtspalgsession_datachannel_binding = []

	@property
	def sessionid(self) :
		ur"""Session ID for the RTSP call.
		"""
		try :
			return self._sessionid
		except Exception as e:
			raise e

	@sessionid.setter
	def sessionid(self, sessionid) :
		ur"""Session ID for the RTSP call.
		"""
		try :
			self._sessionid = sessionid
		except Exception as e:
			raise e

	@property
	def lsnrtspalgsession_datachannel_bindings(self) :
		ur"""datachannel that can be bound to lsnrtspalgsession.
		"""
		try :
			return self._lsnrtspalgsession_datachannel_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnrtspalgsession_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnrtspalgsession_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sessionid is not None :
				return str(self.sessionid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, sessionid) :
		ur""" Use this API to fetch lsnrtspalgsession_binding resource.
		"""
		try :
			if type(sessionid) is not list :
				obj = lsnrtspalgsession_binding()
				obj.sessionid = sessionid
				response = obj.get_resource(service)
			else :
				if sessionid and len(sessionid) > 0 :
					obj = [lsnrtspalgsession_binding() for _ in range(len(sessionid))]
					for i in range(len(sessionid)) :
						obj[i].sessionid = sessionid[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class lsnrtspalgsession_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsnrtspalgsession_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnrtspalgsession_binding = [lsnrtspalgsession_binding() for _ in range(length)]

