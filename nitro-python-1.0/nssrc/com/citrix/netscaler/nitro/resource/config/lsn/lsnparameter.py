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

class lsnparameter(base_resource) :
	""" Configuration for LSN parameter resource. """
	def __init__(self) :
		self._memlimit = 0
		self._sessionsync = ""
		self._memlimitactive = 0
		self._maxmemlimit = 0

	@property
	def memlimit(self) :
		ur"""Amount of NetScaler memory to reserve for the LSN feature, in multiples of 2MB.
		Note: If you later reduce the value of this parameter, the amount of active memory is not reduced. Changing the configured memory limit can only increase the amount of active memory.
		This command is deprecated, use 'set extendedmemoryparam -memlimit' instead.
		"""
		try :
			return self._memlimit
		except Exception as e:
			raise e

	@memlimit.setter
	def memlimit(self, memlimit) :
		ur"""Amount of NetScaler memory to reserve for the LSN feature, in multiples of 2MB.
		Note: If you later reduce the value of this parameter, the amount of active memory is not reduced. Changing the configured memory limit can only increase the amount of active memory.
		This command is deprecated, use 'set extendedmemoryparam -memlimit' instead.
		"""
		try :
			self._memlimit = memlimit
		except Exception as e:
			raise e

	@property
	def sessionsync(self) :
		ur"""Synchronize all LSN sessions with the secondary node in a high availability (HA) deployment (global synchronization). After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary node (new primary).
		The global session synchronization parameter and session synchronization parameters (group level) of all LSN groups are enabled by default.
		For a group, when both the global level and the group level LSN session synchronization parameters are enabled, the primary node synchronizes information of all LSN sessions related to this LSN group with the secondary node.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionsync
		except Exception as e:
			raise e

	@sessionsync.setter
	def sessionsync(self, sessionsync) :
		ur"""Synchronize all LSN sessions with the secondary node in a high availability (HA) deployment (global synchronization). After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary node (new primary).
		The global session synchronization parameter and session synchronization parameters (group level) of all LSN groups are enabled by default.
		For a group, when both the global level and the group level LSN session synchronization parameters are enabled, the primary node synchronizes information of all LSN sessions related to this LSN group with the secondary node.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionsync = sessionsync
		except Exception as e:
			raise e

	@property
	def memlimitactive(self) :
		ur"""Amount of actual memory reserved for the LSN feature. 
		The amount of active memory for the LSN feature might be less than the configured memory, because the available memory is shared across features.
		"""
		try :
			return self._memlimitactive
		except Exception as e:
			raise e

	@property
	def maxmemlimit(self) :
		ur"""Maximum amount of NetScaler memory that can be reserved for the LSN feature.
		"""
		try :
			return self._maxmemlimit
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnparameter
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
		ur""" Use this API to update lsnparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = lsnparameter()
				updateresource.memlimit = resource.memlimit
				updateresource.sessionsync = resource.sessionsync
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lsnparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lsnparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lsnparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Sessionsync:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lsnparameter_response(base_response) :
	def __init__(self, length=1) :
		self.lsnparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnparameter = [lsnparameter() for _ in range(length)]

