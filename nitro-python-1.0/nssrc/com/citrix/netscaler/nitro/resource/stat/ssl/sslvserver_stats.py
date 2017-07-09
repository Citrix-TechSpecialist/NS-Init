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

class sslvserver_stats(base_resource) :
	ur""" Statistics for SSL virtual server resource.
	"""
	def __init__(self) :
		self._vservername = ""
		self._clearstats = ""
		self._vslbhealth = 0
		self._primaryipaddress = ""
		self._primaryport = 0
		self._type = ""
		self._state = ""
		self._actsvcs = 0
		self._ssltotclientauthsuccess = 0
		self._ssltotclientauthfailure = 0

	@property
	def vservername(self) :
		ur"""Name of the SSL virtual server for which to show detailed statistics.<br/>Minimum length =  1.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		ur"""Name of the SSL virtual server for which to show detailed statistics
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		ur"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		ur"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Current state of the server. Possible values are UP, DOWN, UNKNOWN, OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN(Down When going Out of Service).
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def vslbhealth(self) :
		ur"""Health of the vserver. This gives percentage of UP services bound to this vserver.
		"""
		try :
			return self._vslbhealth
		except Exception as e:
			raise e

	@property
	def actsvcs(self) :
		ur"""number of ACTIVE services bound to a vserver.
		"""
		try :
			return self._actsvcs
		except Exception as e:
			raise e

	@property
	def primaryipaddress(self) :
		ur"""IP address of the vserver.
		"""
		try :
			return self._primaryipaddress
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Protocol associated with the vserver.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def primaryport(self) :
		ur"""The port on which the service is running.
		"""
		try :
			return self._primaryport
		except Exception as e:
			raise e

	@property
	def ssltotclientauthfailure(self) :
		ur"""Number of failure client authentication on this vserver.
		"""
		try :
			return self._ssltotclientauthfailure
		except Exception as e:
			raise e

	@property
	def ssltotclientauthsuccess(self) :
		ur"""Number of successful client authentication on this vserver.
		"""
		try :
			return self._ssltotclientauthsuccess
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslvserver_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslvserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.vservername is not None :
				return str(self.vservername)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all sslvserver_stats resources that are configured on netscaler.
		"""
		try :
			obj = sslvserver_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.vservername = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class sslvserver_response(base_response) :
	def __init__(self, length=1) :
		self.sslvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslvserver = [sslvserver_stats() for _ in range(length)]

