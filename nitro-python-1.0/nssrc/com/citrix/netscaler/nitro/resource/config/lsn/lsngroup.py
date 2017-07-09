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

class lsngroup(base_resource) :
	""" Configuration for LSN group resource. """
	def __init__(self) :
		self._groupname = ""
		self._clientname = ""
		self._nattype = ""
		self._portblocksize = 0
		self._logging = ""
		self._sessionlogging = ""
		self._sessionsync = ""
		self._snmptraplimit = 0
		self._ftp = ""
		self._pptp = ""
		self._sipalg = ""
		self._rtspalg = ""
		self._ip6profile = ""
		self._groupid = 0
		self.___count = 0

	@property
	def groupname(self) :
		ur"""Name for the LSN group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN group is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn group1" or 'lsn group1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""Name for the LSN group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN group is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn group1" or 'lsn group1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def clientname(self) :
		ur"""Name of the LSN client entity to be associated with the LSN group. You can associate only one LSN client entity with an LSN group.You cannot remove this association or replace with another LSN client entity once the LSN group is created.
		"""
		try :
			return self._clientname
		except Exception as e:
			raise e

	@clientname.setter
	def clientname(self, clientname) :
		ur"""Name of the LSN client entity to be associated with the LSN group. You can associate only one LSN client entity with an LSN group.You cannot remove this association or replace with another LSN client entity once the LSN group is created.
		"""
		try :
			self._clientname = clientname
		except Exception as e:
			raise e

	@property
	def nattype(self) :
		ur"""Type of NAT IP address and port allocation (from the bound LSN pools) for subscribers:
		Available options function as follows:
		* Deterministic - Allocate a NAT IP address and a block of ports to each subscriber (of the LSN client bound to the LSN group). The NetScaler ADC sequentially allocates NAT resources to these subscribers. The NetScaler ADC assigns the first block of ports (block size determined by the port block size parameter of the LSN group) on the beginning NAT IP address to the beginning subscriber IP address. The next range of ports is assigned to the next subscriber, and so on, until the NAT address does not have enough ports for the next subscriber. In this case, the first port block on the next NAT address is used for the subscriber, and so on.  Because each subscriber now receives a deterministic NAT IP address and a block of ports, a subscriber can be identified without any need for logging. For a connection, a subscriber can be identified based only on the NAT IP address and port, and the destination IP address and port. The maximum number of LSN subscribers allowed, globally, is 1 million.  
		* Dynamic - Allocate a random NAT IP address and a port from the LSN NAT pool for a subscriber\'s connection. If port block allocation is enabled (in LSN pool) and a port block size is specified (in the LSN group), the NetScaler ADC allocates a random NAT IP address and a block of ports for a subscriber when it initiates a connection for the first time. The ADC allocates this NAT IP address and a port (from the allocated block of ports) for different connections from this subscriber. If all the ports are allocated (for different subscriber\'s connections) from the subscriber\'s allocated port block, the ADC allocates a new random port block for the subscriber.<br/>Default value: DYNAMIC<br/>Possible values = DYNAMIC, DETERMINISTIC.
		"""
		try :
			return self._nattype
		except Exception as e:
			raise e

	@nattype.setter
	def nattype(self, nattype) :
		ur"""Type of NAT IP address and port allocation (from the bound LSN pools) for subscribers:
		Available options function as follows:
		* Deterministic - Allocate a NAT IP address and a block of ports to each subscriber (of the LSN client bound to the LSN group). The NetScaler ADC sequentially allocates NAT resources to these subscribers. The NetScaler ADC assigns the first block of ports (block size determined by the port block size parameter of the LSN group) on the beginning NAT IP address to the beginning subscriber IP address. The next range of ports is assigned to the next subscriber, and so on, until the NAT address does not have enough ports for the next subscriber. In this case, the first port block on the next NAT address is used for the subscriber, and so on.  Because each subscriber now receives a deterministic NAT IP address and a block of ports, a subscriber can be identified without any need for logging. For a connection, a subscriber can be identified based only on the NAT IP address and port, and the destination IP address and port. The maximum number of LSN subscribers allowed, globally, is 1 million.  
		* Dynamic - Allocate a random NAT IP address and a port from the LSN NAT pool for a subscriber\'s connection. If port block allocation is enabled (in LSN pool) and a port block size is specified (in the LSN group), the NetScaler ADC allocates a random NAT IP address and a block of ports for a subscriber when it initiates a connection for the first time. The ADC allocates this NAT IP address and a port (from the allocated block of ports) for different connections from this subscriber. If all the ports are allocated (for different subscriber\'s connections) from the subscriber\'s allocated port block, the ADC allocates a new random port block for the subscriber.<br/>Default value: DYNAMIC<br/>Possible values = DYNAMIC, DETERMINISTIC
		"""
		try :
			self._nattype = nattype
		except Exception as e:
			raise e

	@property
	def portblocksize(self) :
		ur"""Size of the NAT port block to be allocated for each subscriber.
		To set this parameter for Dynamic NAT, you must enable the port block allocation parameter in the bound LSN pool. For Deterministic NAT, the port block allocation parameter is always  enabled, and you cannot disable it.
		In Dynamic NAT, the NetScaler ADC allocates a random NAT port block, from the available NAT port pool of an NAT IP address, for each subscriber. For a subscriber, if all the ports are allocated from the subscriber\'s allocated port block, the ADC allocates a new random port block for the subscriber.
		The default port block size is 256 for Deterministic NAT, and 0 for Dynamic NAT.<br/>Default value: 0<br/>Minimum length =  256<br/>Maximum length =  65536.
		"""
		try :
			return self._portblocksize
		except Exception as e:
			raise e

	@portblocksize.setter
	def portblocksize(self, portblocksize) :
		ur"""Size of the NAT port block to be allocated for each subscriber.
		To set this parameter for Dynamic NAT, you must enable the port block allocation parameter in the bound LSN pool. For Deterministic NAT, the port block allocation parameter is always  enabled, and you cannot disable it.
		In Dynamic NAT, the NetScaler ADC allocates a random NAT port block, from the available NAT port pool of an NAT IP address, for each subscriber. For a subscriber, if all the ports are allocated from the subscriber\'s allocated port block, the ADC allocates a new random port block for the subscriber.
		The default port block size is 256 for Deterministic NAT, and 0 for Dynamic NAT.<br/>Default value: 0<br/>Minimum length =  256<br/>Maximum length =  65536
		"""
		try :
			self._portblocksize = portblocksize
		except Exception as e:
			raise e

	@property
	def logging(self) :
		ur"""Log mapping entries and sessions created or deleted for this LSN group. The NetScaler ADC logs LSN sessions for this LSN group only when both logging and session logging parameters are enabled.
		The ADC uses its existing syslog and audit log framework to log LSN information. You must enable global level LSN logging by enabling the LSN parameter in the related NSLOG action and SYLOG action entities. When the Logging parameter is enabled, the NetScaler ADC generates log messages related to LSN mappings and LSN sessions of this LSN group. The ADC then sends these log messages to servers associated with the NSLOG action and SYSLOG actions entities. 
		A log message for an LSN mapping entry consists of the following information:
		* NSIP address of the NetScaler ADC
		* Time stamp
		* Entry type (MAPPING or SESSION)
		* Whether the LSN mapping entry is created or deleted
		* Subscriber's IP address, port, and traffic domain ID
		* NAT IP address and port
		* Protocol name
		* Destination IP address, port, and traffic domain ID might be  present, depending on the following conditions:
		** Destination IP address and port are not logged for Endpoint-Independent mapping
		** Only Destination IP address (and not port) is logged for Address-Dependent mapping
		** Destination IP address and port are logged for Address-Port-Dependent mapping.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logging
		except Exception as e:
			raise e

	@logging.setter
	def logging(self, logging) :
		ur"""Log mapping entries and sessions created or deleted for this LSN group. The NetScaler ADC logs LSN sessions for this LSN group only when both logging and session logging parameters are enabled.
		The ADC uses its existing syslog and audit log framework to log LSN information. You must enable global level LSN logging by enabling the LSN parameter in the related NSLOG action and SYLOG action entities. When the Logging parameter is enabled, the NetScaler ADC generates log messages related to LSN mappings and LSN sessions of this LSN group. The ADC then sends these log messages to servers associated with the NSLOG action and SYSLOG actions entities. 
		A log message for an LSN mapping entry consists of the following information:
		* NSIP address of the NetScaler ADC
		* Time stamp
		* Entry type (MAPPING or SESSION)
		* Whether the LSN mapping entry is created or deleted
		* Subscriber's IP address, port, and traffic domain ID
		* NAT IP address and port
		* Protocol name
		* Destination IP address, port, and traffic domain ID might be  present, depending on the following conditions:
		** Destination IP address and port are not logged for Endpoint-Independent mapping
		** Only Destination IP address (and not port) is logged for Address-Dependent mapping
		** Destination IP address and port are logged for Address-Port-Dependent mapping.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logging = logging
		except Exception as e:
			raise e

	@property
	def sessionlogging(self) :
		ur"""Log sessions created or deleted for the LSN group. The NetScaler ADC logs LSN sessions for this LSN group only when both logging and session logging parameters are enabled.
		A log message for an LSN session consists of the following information:
		* NSIP address of the NetScaler ADC
		* Time stamp
		* Entry type (MAPPING or SESSION)
		* Whether the LSN session is created or removed
		* Subscriber's IP address, port, and traffic domain ID
		* NAT IP address and port
		* Protocol name
		* Destination IP address, port, and traffic domain ID.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionlogging
		except Exception as e:
			raise e

	@sessionlogging.setter
	def sessionlogging(self, sessionlogging) :
		ur"""Log sessions created or deleted for the LSN group. The NetScaler ADC logs LSN sessions for this LSN group only when both logging and session logging parameters are enabled.
		A log message for an LSN session consists of the following information:
		* NSIP address of the NetScaler ADC
		* Time stamp
		* Entry type (MAPPING or SESSION)
		* Whether the LSN session is created or removed
		* Subscriber's IP address, port, and traffic domain ID
		* NAT IP address and port
		* Protocol name
		* Destination IP address, port, and traffic domain ID.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionlogging = sessionlogging
		except Exception as e:
			raise e

	@property
	def sessionsync(self) :
		ur"""In a high availability (HA) deployment, synchronize information of all LSN sessions related to this LSN group with the secondary node. After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary node (new primary).
		For this setting to work, you must enable the global session synchronization parameter.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionsync
		except Exception as e:
			raise e

	@sessionsync.setter
	def sessionsync(self, sessionsync) :
		ur"""In a high availability (HA) deployment, synchronize information of all LSN sessions related to this LSN group with the secondary node. After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary node (new primary).
		For this setting to work, you must enable the global session synchronization parameter.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionsync = sessionsync
		except Exception as e:
			raise e

	@property
	def snmptraplimit(self) :
		ur"""Maximum number of SNMP Trap messages that can be generated for the LSN group in one minute.<br/>Default value: 100<br/>Maximum length =  10000.
		"""
		try :
			return self._snmptraplimit
		except Exception as e:
			raise e

	@snmptraplimit.setter
	def snmptraplimit(self, snmptraplimit) :
		ur"""Maximum number of SNMP Trap messages that can be generated for the LSN group in one minute.<br/>Default value: 100<br/>Maximum length =  10000
		"""
		try :
			self._snmptraplimit = snmptraplimit
		except Exception as e:
			raise e

	@property
	def ftp(self) :
		ur"""Enable Application Layer Gateway (ALG) for the FTP protocol. For some application-layer protocols, the IP addresses and protocol port numbers are usually communicated in the packet's payload. When acting as an ALG, the NetScaler changes the packet's payload to ensure that the protocol continues to work over LSN. 
		Note:  The NetScaler ADC also includes ALG for ICMP and TFTP protocols. ALG for the ICMP protocol is enabled by default, and there is no provision to disable it. ALG for the TFTP protocol is disabled by default. ALG is enabled automatically for an LSN group when you bind a UDP LSN application profile, with endpoint-independent-mapping, endpoint-independent filtering, and destination port as 69 (well-known port for TFTP), to the LSN group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ftp
		except Exception as e:
			raise e

	@ftp.setter
	def ftp(self, ftp) :
		ur"""Enable Application Layer Gateway (ALG) for the FTP protocol. For some application-layer protocols, the IP addresses and protocol port numbers are usually communicated in the packet's payload. When acting as an ALG, the NetScaler changes the packet's payload to ensure that the protocol continues to work over LSN. 
		Note:  The NetScaler ADC also includes ALG for ICMP and TFTP protocols. ALG for the ICMP protocol is enabled by default, and there is no provision to disable it. ALG for the TFTP protocol is disabled by default. ALG is enabled automatically for an LSN group when you bind a UDP LSN application profile, with endpoint-independent-mapping, endpoint-independent filtering, and destination port as 69 (well-known port for TFTP), to the LSN group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ftp = ftp
		except Exception as e:
			raise e

	@property
	def pptp(self) :
		ur"""Enable the PPTP Application Layer Gateway.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._pptp
		except Exception as e:
			raise e

	@pptp.setter
	def pptp(self, pptp) :
		ur"""Enable the PPTP Application Layer Gateway.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._pptp = pptp
		except Exception as e:
			raise e

	@property
	def sipalg(self) :
		ur"""Enable the SIP ALG.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sipalg
		except Exception as e:
			raise e

	@sipalg.setter
	def sipalg(self, sipalg) :
		ur"""Enable the SIP ALG.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sipalg = sipalg
		except Exception as e:
			raise e

	@property
	def rtspalg(self) :
		ur"""Enable the RTSP ALG.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rtspalg
		except Exception as e:
			raise e

	@rtspalg.setter
	def rtspalg(self, rtspalg) :
		ur"""Enable the RTSP ALG.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rtspalg = rtspalg
		except Exception as e:
			raise e

	@property
	def ip6profile(self) :
		ur"""Name of the LSN ip6 profile to associate with the specified LSN group. An ip6 profile can be associated with a group only during group creation.
		By default, no LSN ip6 profile is associated with an LSN group during its creation. Only one ip6profile can be associated with a group.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._ip6profile
		except Exception as e:
			raise e

	@ip6profile.setter
	def ip6profile(self, ip6profile) :
		ur"""Name of the LSN ip6 profile to associate with the specified LSN group. An ip6 profile can be associated with a group only during group creation.
		By default, no LSN ip6 profile is associated with an LSN group during its creation. Only one ip6profile can be associated with a group.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._ip6profile = ip6profile
		except Exception as e:
			raise e

	@property
	def groupid(self) :
		ur""".<br/>Minimum value =  1.
		"""
		try :
			return self._groupid
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsngroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsngroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.groupname is not None :
				return str(self.groupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add lsngroup.
		"""
		try :
			if type(resource) is not list :
				addresource = lsngroup()
				addresource.groupname = resource.groupname
				addresource.clientname = resource.clientname
				addresource.nattype = resource.nattype
				addresource.portblocksize = resource.portblocksize
				addresource.logging = resource.logging
				addresource.sessionlogging = resource.sessionlogging
				addresource.sessionsync = resource.sessionsync
				addresource.snmptraplimit = resource.snmptraplimit
				addresource.ftp = resource.ftp
				addresource.pptp = resource.pptp
				addresource.sipalg = resource.sipalg
				addresource.rtspalg = resource.rtspalg
				addresource.ip6profile = resource.ip6profile
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsngroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].groupname = resource[i].groupname
						addresources[i].clientname = resource[i].clientname
						addresources[i].nattype = resource[i].nattype
						addresources[i].portblocksize = resource[i].portblocksize
						addresources[i].logging = resource[i].logging
						addresources[i].sessionlogging = resource[i].sessionlogging
						addresources[i].sessionsync = resource[i].sessionsync
						addresources[i].snmptraplimit = resource[i].snmptraplimit
						addresources[i].ftp = resource[i].ftp
						addresources[i].pptp = resource[i].pptp
						addresources[i].sipalg = resource[i].sipalg
						addresources[i].rtspalg = resource[i].rtspalg
						addresources[i].ip6profile = resource[i].ip6profile
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lsngroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsngroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.groupname = resource
				else :
					deleteresource.groupname = resource.groupname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsngroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].groupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsngroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].groupname = resource[i].groupname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update lsngroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = lsngroup()
				updateresource.groupname = resource.groupname
				updateresource.portblocksize = resource.portblocksize
				updateresource.logging = resource.logging
				updateresource.sessionlogging = resource.sessionlogging
				updateresource.sessionsync = resource.sessionsync
				updateresource.snmptraplimit = resource.snmptraplimit
				updateresource.ftp = resource.ftp
				updateresource.pptp = resource.pptp
				updateresource.sipalg = resource.sipalg
				updateresource.rtspalg = resource.rtspalg
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lsngroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].groupname = resource[i].groupname
						updateresources[i].portblocksize = resource[i].portblocksize
						updateresources[i].logging = resource[i].logging
						updateresources[i].sessionlogging = resource[i].sessionlogging
						updateresources[i].sessionsync = resource[i].sessionsync
						updateresources[i].snmptraplimit = resource[i].snmptraplimit
						updateresources[i].ftp = resource[i].ftp
						updateresources[i].pptp = resource[i].pptp
						updateresources[i].sipalg = resource[i].sipalg
						updateresources[i].rtspalg = resource[i].rtspalg
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lsngroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lsngroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.groupname = resource
				else :
					unsetresource.groupname = resource.groupname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsngroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].groupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsngroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].groupname = resource[i].groupname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lsngroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsngroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lsngroup()
						obj.groupname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lsngroup() for _ in range(len(name))]
							obj = [lsngroup() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lsngroup()
								obj[i].groupname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lsngroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsngroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lsngroup resources configured on NetScaler.
		"""
		try :
			obj = lsngroup()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of lsngroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsngroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sessionlogging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sipalg:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Pptp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rtspalg:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ftp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nattype:
		DYNAMIC = "DYNAMIC"
		DETERMINISTIC = "DETERMINISTIC"

	class Sessionsync:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lsngroup_response(base_response) :
	def __init__(self, length=1) :
		self.lsngroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsngroup = [lsngroup() for _ in range(length)]

