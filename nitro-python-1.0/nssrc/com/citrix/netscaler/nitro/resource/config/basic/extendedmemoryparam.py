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

class extendedmemoryparam(base_resource) :
	""" Configuration for Parameter for extended memory used by LSN and Subscriber Store resource. """
	def __init__(self) :
		self._memlimit = 0
		self._memlimitactive = 0
		self._maxmemlimit = 0
		self._minrequiredmemory = 0

	@property
	def memlimit(self) :
		ur"""Amount of NetScaler memory to reserve for the memory used by LSN and Subscriber Session Store feature, in multiples of 2MB.
		Note: If you later reduce the value of this parameter, the amount of active memory is not reduced. Changing the configured memory limit can only increase the amount of active memory.
		"""
		try :
			return self._memlimit
		except Exception as e:
			raise e

	@memlimit.setter
	def memlimit(self, memlimit) :
		ur"""Amount of NetScaler memory to reserve for the memory used by LSN and Subscriber Session Store feature, in multiples of 2MB.
		Note: If you later reduce the value of this parameter, the amount of active memory is not reduced. Changing the configured memory limit can only increase the amount of active memory.
		"""
		try :
			self._memlimit = memlimit
		except Exception as e:
			raise e

	@property
	def memlimitactive(self) :
		ur"""The active memory limit for extendedmemory on the system. Active memory limit could be different from configured memory limit. This could happen when memory limit could not be increased due to unavailability, or could not be decreased as it is already in use. This active memory limit configures the current memory limit for LSN and Subscriber Session Store.
		"""
		try :
			return self._memlimitactive
		except Exception as e:
			raise e

	@property
	def maxmemlimit(self) :
		ur"""The maximum value of memory limit for extendedmemory on the system. Actual available memory may be less. This is maximum memory that can be utilized by LSN and Subscriber Session Store modules.
		"""
		try :
			return self._maxmemlimit
		except Exception as e:
			raise e

	@property
	def minrequiredmemory(self) :
		ur"""The minimum memory requirement for extendedmemory. This is minimum memory required for LSN and Subscriber Session Store Modules.
		"""
		try :
			return self._minrequiredmemory
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(extendedmemoryparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.extendedmemoryparam
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update extendedmemoryparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = extendedmemoryparam()
				updateresource.memlimit = resource.memlimit
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of extendedmemoryparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = extendedmemoryparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the extendedmemoryparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = extendedmemoryparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class extendedmemoryparam_response(base_response) :
	def __init__(self, length=1) :
		self.extendedmemoryparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.extendedmemoryparam = [extendedmemoryparam() for _ in range(length)]

