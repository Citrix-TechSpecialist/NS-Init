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

class subscriberparam(base_resource) :
	""" Configuration for Subscriber Params resource. """
	def __init__(self) :
		self._keytype = ""
		self._interfacetype = ""
		self._idlettl = 0
		self._idleaction = ""
		self._ipv6prefixlookuplist = []
		self._builtin = []

	@property
	def keytype(self) :
		ur"""Type of subscriber key type IP or IPANDVLAN.<br/>Default value: IP<br/>Possible values = IP.
		"""
		try :
			return self._keytype
		except Exception as e:
			raise e

	@keytype.setter
	def keytype(self, keytype) :
		ur"""Type of subscriber key type IP or IPANDVLAN.<br/>Default value: IP<br/>Possible values = IP
		"""
		try :
			self._keytype = keytype
		except Exception as e:
			raise e

	@property
	def interfacetype(self) :
		ur"""Subscriber Interface refers to Netscaler interaction with control plane protocols, RADIUS and GX.
		Types of subscriber interface: NONE, RadiusOnly, RadiusAndGx, GxOnly.
		NONE: Only static subscribers can be configured.
		RadiusOnly: GX interface is absent. Subscriber information is obtained through RADIUS Accounting messages.
		RadiusAndGx: Subscriber ID obtained through RADIUS Accounting is used to query PCRF. Subscriber information is obtained from both RADIUS and PCRF.
		GxOnly: RADIUS interface is absent. Subscriber information is queried using Subscriber IP.
		<br/>Default value: None<br/>Possible values = None, RadiusOnly, RadiusAndGx, GxOnly.
		"""
		try :
			return self._interfacetype
		except Exception as e:
			raise e

	@interfacetype.setter
	def interfacetype(self, interfacetype) :
		ur"""Subscriber Interface refers to Netscaler interaction with control plane protocols, RADIUS and GX.
		Types of subscriber interface: NONE, RadiusOnly, RadiusAndGx, GxOnly.
		NONE: Only static subscribers can be configured.
		RadiusOnly: GX interface is absent. Subscriber information is obtained through RADIUS Accounting messages.
		RadiusAndGx: Subscriber ID obtained through RADIUS Accounting is used to query PCRF. Subscriber information is obtained from both RADIUS and PCRF.
		GxOnly: RADIUS interface is absent. Subscriber information is queried using Subscriber IP.
		<br/>Default value: None<br/>Possible values = None, RadiusOnly, RadiusAndGx, GxOnly
		"""
		try :
			self._interfacetype = interfacetype
		except Exception as e:
			raise e

	@property
	def idlettl(self) :
		ur"""q!Idle Timeout, in seconds, after which Netscaler will take an idleAction on a subscriber session (refer to 'idleAction' arguement in 'set subscriber param' for more details on idleAction). Any data-plane or control plane activity updates the idleTimeout on subscriber session. idleAction could be to 'just delete the session' or 'delete and CCR-T' (if PCRF is configured) or 'do not delete but send a CCR-U'. 
		Zero value disables the idle timeout. !.<br/>Default value: 0<br/>Maximum length =  172800.
		"""
		try :
			return self._idlettl
		except Exception as e:
			raise e

	@idlettl.setter
	def idlettl(self, idlettl) :
		ur"""q!Idle Timeout, in seconds, after which Netscaler will take an idleAction on a subscriber session (refer to 'idleAction' arguement in 'set subscriber param' for more details on idleAction). Any data-plane or control plane activity updates the idleTimeout on subscriber session. idleAction could be to 'just delete the session' or 'delete and CCR-T' (if PCRF is configured) or 'do not delete but send a CCR-U'. 
		Zero value disables the idle timeout. !.<br/>Default value: 0<br/>Maximum length =  172800
		"""
		try :
			self._idlettl = idlettl
		except Exception as e:
			raise e

	@property
	def idleaction(self) :
		ur"""q!Once idleTTL exprires on a subscriber session, Netscaler will take an idle action on that session. idleAction could be chosen from one of these ==>
		1. ccrTerminate: (default) send CCR-T to inform PCRF about session termination and delete the session.  
		2. delete: Just delete the subscriber session without informing PCRF.
		3. ccrUpdate: Do not delete the session and instead send a CCR-U to PCRF requesting for an updated session. !.<br/>Default value: ccrTerminate<br/>Possible values = ccrTerminate, delete, ccrUpdate.
		"""
		try :
			return self._idleaction
		except Exception as e:
			raise e

	@idleaction.setter
	def idleaction(self, idleaction) :
		ur"""q!Once idleTTL exprires on a subscriber session, Netscaler will take an idle action on that session. idleAction could be chosen from one of these ==>
		1. ccrTerminate: (default) send CCR-T to inform PCRF about session termination and delete the session.  
		2. delete: Just delete the subscriber session without informing PCRF.
		3. ccrUpdate: Do not delete the session and instead send a CCR-U to PCRF requesting for an updated session. !.<br/>Default value: ccrTerminate<br/>Possible values = ccrTerminate, delete, ccrUpdate
		"""
		try :
			self._idleaction = idleaction
		except Exception as e:
			raise e

	@property
	def ipv6prefixlookuplist(self) :
		ur""" The ipv6PrefixLookupList should consist of all the ipv6 prefix lengths assigned to the UE's'.<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._ipv6prefixlookuplist
		except Exception as e:
			raise e

	@ipv6prefixlookuplist.setter
	def ipv6prefixlookuplist(self, ipv6prefixlookuplist) :
		ur""" The ipv6PrefixLookupList should consist of all the ipv6 prefix lengths assigned to the UE's'.<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._ipv6prefixlookuplist = ipv6prefixlookuplist
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur""".<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(subscriberparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.subscriberparam
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
		ur""" Use this API to update subscriberparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = subscriberparam()
				updateresource.keytype = resource.keytype
				updateresource.interfacetype = resource.interfacetype
				updateresource.idlettl = resource.idlettl
				updateresource.idleaction = resource.idleaction
				updateresource.ipv6prefixlookuplist = resource.ipv6prefixlookuplist
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of subscriberparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = subscriberparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the subscriberparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = subscriberparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Interfacetype:
		NONE = "None"
		RadiusOnly = "RadiusOnly"
		RadiusAndGx = "RadiusAndGx"
		GxOnly = "GxOnly"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Keytype:
		IP = "IP"

	class Idleaction:
		ccrTerminate = "ccrTerminate"
		delete = "delete"
		ccrUpdate = "ccrUpdate"

class subscriberparam_response(base_response) :
	def __init__(self, length=1) :
		self.subscriberparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.subscriberparam = [subscriberparam() for _ in range(length)]

