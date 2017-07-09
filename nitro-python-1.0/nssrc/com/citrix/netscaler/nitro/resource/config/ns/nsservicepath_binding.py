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

class nsservicepath_binding(base_resource):
	""" Binding class showing the resources that can be bound to nsservicepath_binding. 
	"""
	def __init__(self) :
		self._servicepathname = ""
		self.nsservicepath_nsservicefunction_binding = []

	@property
	def servicepathname(self) :
		ur"""Name for the Service path. Must begin with an ASCII alphanumeric or underscore (_) character, and must 
		contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
		characters.<br/>Minimum length =  1.
		"""
		try :
			return self._servicepathname
		except Exception as e:
			raise e

	@servicepathname.setter
	def servicepathname(self, servicepathname) :
		ur"""Name for the Service path. Must begin with an ASCII alphanumeric or underscore (_) character, and must 
		contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
		characters.<br/>Minimum length =  1
		"""
		try :
			self._servicepathname = servicepathname
		except Exception as e:
			raise e

	@property
	def nsservicepath_nsservicefunction_bindings(self) :
		ur"""nsservicefunction that can be bound to nsservicepath.
		"""
		try :
			return self._nsservicepath_nsservicefunction_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsservicepath_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsservicepath_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicepathname is not None :
				return str(self.servicepathname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, servicepathname) :
		ur""" Use this API to fetch nsservicepath_binding resource.
		"""
		try :
			if type(servicepathname) is not list :
				obj = nsservicepath_binding()
				obj.servicepathname = servicepathname
				response = obj.get_resource(service)
			else :
				if servicepathname and len(servicepathname) > 0 :
					obj = [nsservicepath_binding() for _ in range(len(servicepathname))]
					for i in range(len(servicepathname)) :
						obj[i].servicepathname = servicepathname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class nsservicepath_binding_response(base_response) :
	def __init__(self, length=1) :
		self.nsservicepath_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsservicepath_binding = [nsservicepath_binding() for _ in range(length)]

