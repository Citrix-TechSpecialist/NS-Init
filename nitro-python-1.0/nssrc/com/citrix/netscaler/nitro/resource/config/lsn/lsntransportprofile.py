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

class lsntransportprofile(base_resource) :
	""" Configuration for LSN Transport Profile resource. """
	def __init__(self) :
		self._transportprofilename = ""
		self._transportprotocol = ""
		self._sessiontimeout = 0
		self._finrsttimeout = 0
		self._stuntimeout = 0
		self._synidletimeout = 0
		self._portquota = 0
		self._sessionquota = 0
		self._groupsessionlimit = 0
		self._portpreserveparity = ""
		self._portpreserverange = ""
		self._syncheck = ""
		self.___count = 0

	@property
	def transportprofilename(self) :
		ur"""Name for the LSN transport profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN transport profile is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn transport profile1" or 'lsn transport profile1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._transportprofilename
		except Exception as e:
			raise e

	@transportprofilename.setter
	def transportprofilename(self, transportprofilename) :
		ur"""Name for the LSN transport profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN transport profile is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn transport profile1" or 'lsn transport profile1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._transportprofilename = transportprofilename
		except Exception as e:
			raise e

	@property
	def transportprotocol(self) :
		ur"""Protocol for which to set the LSN transport profile parameters.<br/>Possible values = TCP, UDP, ICMP.
		"""
		try :
			return self._transportprotocol
		except Exception as e:
			raise e

	@transportprotocol.setter
	def transportprotocol(self, transportprotocol) :
		ur"""Protocol for which to set the LSN transport profile parameters.<br/>Possible values = TCP, UDP, ICMP
		"""
		try :
			self._transportprotocol = transportprotocol
		except Exception as e:
			raise e

	@property
	def sessiontimeout(self) :
		ur"""Timeout, in seconds, for an idle LSN session. If an LSN session is idle for a time that exceeds this value, the NetScaler ADC removes the session.
		This timeout does not apply for a TCP LSN session when a FIN or RST message is received from either of the endpoints. .<br/>Default value: 120<br/>Minimum length =  60.
		"""
		try :
			return self._sessiontimeout
		except Exception as e:
			raise e

	@sessiontimeout.setter
	def sessiontimeout(self, sessiontimeout) :
		ur"""Timeout, in seconds, for an idle LSN session. If an LSN session is idle for a time that exceeds this value, the NetScaler ADC removes the session.
		This timeout does not apply for a TCP LSN session when a FIN or RST message is received from either of the endpoints. .<br/>Default value: 120<br/>Minimum length =  60
		"""
		try :
			self._sessiontimeout = sessiontimeout
		except Exception as e:
			raise e

	@property
	def finrsttimeout(self) :
		ur"""Timeout, in seconds, for a TCP LSN session after a FIN or RST message is received from one of the endpoints.
		If a TCP LSN session is idle (after the NetScaler ADC receives a FIN or RST message) for a time that exceeds this value, the NetScaler ADC removes the session.
		Since the LSN feature of the NetScaler ADC does not maintain state information of any TCP LSN sessions, this timeout accommodates the transmission of the FIN or RST, and ACK messages from the other endpoint so that both endpoints can properly close the connection.<br/>Default value: 30.
		"""
		try :
			return self._finrsttimeout
		except Exception as e:
			raise e

	@finrsttimeout.setter
	def finrsttimeout(self, finrsttimeout) :
		ur"""Timeout, in seconds, for a TCP LSN session after a FIN or RST message is received from one of the endpoints.
		If a TCP LSN session is idle (after the NetScaler ADC receives a FIN or RST message) for a time that exceeds this value, the NetScaler ADC removes the session.
		Since the LSN feature of the NetScaler ADC does not maintain state information of any TCP LSN sessions, this timeout accommodates the transmission of the FIN or RST, and ACK messages from the other endpoint so that both endpoints can properly close the connection.<br/>Default value: 30
		"""
		try :
			self._finrsttimeout = finrsttimeout
		except Exception as e:
			raise e

	@property
	def stuntimeout(self) :
		ur"""STUN protocol timeout.<br/>Default value: 600<br/>Minimum length =  120<br/>Maximum length =  1200.
		"""
		try :
			return self._stuntimeout
		except Exception as e:
			raise e

	@stuntimeout.setter
	def stuntimeout(self, stuntimeout) :
		ur"""STUN protocol timeout.<br/>Default value: 600<br/>Minimum length =  120<br/>Maximum length =  1200
		"""
		try :
			self._stuntimeout = stuntimeout
		except Exception as e:
			raise e

	@property
	def synidletimeout(self) :
		ur"""SYN Idle timeout.<br/>Default value: 60<br/>Minimum length =  30<br/>Maximum length =  120.
		"""
		try :
			return self._synidletimeout
		except Exception as e:
			raise e

	@synidletimeout.setter
	def synidletimeout(self, synidletimeout) :
		ur"""SYN Idle timeout.<br/>Default value: 60<br/>Minimum length =  30<br/>Maximum length =  120
		"""
		try :
			self._synidletimeout = synidletimeout
		except Exception as e:
			raise e

	@property
	def portquota(self) :
		ur"""Maximum number of LSN NAT ports to be used at a time by each subscriber for the specified protocol. For example, each subscriber can be limited to a maximum of 500 TCP NAT ports. When the LSN NAT mappings for a subscriber reach the limit, the NetScaler ADC does not allocate additional NAT ports for that subscriber.<br/>Default value: 0<br/>Maximum length =  65535.
		"""
		try :
			return self._portquota
		except Exception as e:
			raise e

	@portquota.setter
	def portquota(self, portquota) :
		ur"""Maximum number of LSN NAT ports to be used at a time by each subscriber for the specified protocol. For example, each subscriber can be limited to a maximum of 500 TCP NAT ports. When the LSN NAT mappings for a subscriber reach the limit, the NetScaler ADC does not allocate additional NAT ports for that subscriber.<br/>Default value: 0<br/>Maximum length =  65535
		"""
		try :
			self._portquota = portquota
		except Exception as e:
			raise e

	@property
	def sessionquota(self) :
		ur"""Maximum number of concurrent LSN sessions allowed for each subscriber for the specified protocol. 
		When the number of LSN sessions reaches the limit for a subscriber, the NetScaler ADC does not allow the subscriber to open additional sessions.<br/>Default value: 0<br/>Maximum length =  65535.
		"""
		try :
			return self._sessionquota
		except Exception as e:
			raise e

	@sessionquota.setter
	def sessionquota(self, sessionquota) :
		ur"""Maximum number of concurrent LSN sessions allowed for each subscriber for the specified protocol. 
		When the number of LSN sessions reaches the limit for a subscriber, the NetScaler ADC does not allow the subscriber to open additional sessions.<br/>Default value: 0<br/>Maximum length =  65535
		"""
		try :
			self._sessionquota = sessionquota
		except Exception as e:
			raise e

	@property
	def groupsessionlimit(self) :
		ur"""Maximum number of concurrent LSN sessions(for the specified protocol) allowed for all subscriber of a group to which this profile has bound. This limit will get split across the netscalers packet engines and rounded down. When the number of LSN sessions reaches the limit for a group in packet engine, the NetScaler ADC does not allow the subscriber of that group to open additional sessions through that packet engine.<br/>Default value: 0.
		"""
		try :
			return self._groupsessionlimit
		except Exception as e:
			raise e

	@groupsessionlimit.setter
	def groupsessionlimit(self, groupsessionlimit) :
		ur"""Maximum number of concurrent LSN sessions(for the specified protocol) allowed for all subscriber of a group to which this profile has bound. This limit will get split across the netscalers packet engines and rounded down. When the number of LSN sessions reaches the limit for a group in packet engine, the NetScaler ADC does not allow the subscriber of that group to open additional sessions through that packet engine.<br/>Default value: 0
		"""
		try :
			self._groupsessionlimit = groupsessionlimit
		except Exception as e:
			raise e

	@property
	def portpreserveparity(self) :
		ur"""Enable port parity between a subscriber port and its mapped LSN NAT port. For example, if a subscriber initiates a connection from an odd numbered port, the NetScaler ADC allocates an odd numbered LSN NAT port for this connection. 
		You must set this parameter for proper functioning of protocols that require the source port to be even or odd numbered, for example, in peer-to-peer applications that use RTP or RTCP protocol.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._portpreserveparity
		except Exception as e:
			raise e

	@portpreserveparity.setter
	def portpreserveparity(self, portpreserveparity) :
		ur"""Enable port parity between a subscriber port and its mapped LSN NAT port. For example, if a subscriber initiates a connection from an odd numbered port, the NetScaler ADC allocates an odd numbered LSN NAT port for this connection. 
		You must set this parameter for proper functioning of protocols that require the source port to be even or odd numbered, for example, in peer-to-peer applications that use RTP or RTCP protocol.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._portpreserveparity = portpreserveparity
		except Exception as e:
			raise e

	@property
	def portpreserverange(self) :
		ur"""If a subscriber initiates a connection from a well-known port (0-1023), allocate a NAT port from the well-known port range (0-1023) for this connection. For example, if a subscriber initiates a connection from port 80, the NetScaler ADC can allocate port 100 as the NAT port for this connection.
		This parameter applies to dynamic NAT without port block allocation. It also applies to Deterministic NAT if the range of ports allocated includes well-known ports.
		When all the well-known ports of all the available NAT IP addresses are used in different subscribers\' connections (LSN sessions), and a subscriber initiates a connection from a well-known port, the NetScaler ADC drops this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._portpreserverange
		except Exception as e:
			raise e

	@portpreserverange.setter
	def portpreserverange(self, portpreserverange) :
		ur"""If a subscriber initiates a connection from a well-known port (0-1023), allocate a NAT port from the well-known port range (0-1023) for this connection. For example, if a subscriber initiates a connection from port 80, the NetScaler ADC can allocate port 100 as the NAT port for this connection.
		This parameter applies to dynamic NAT without port block allocation. It also applies to Deterministic NAT if the range of ports allocated includes well-known ports.
		When all the well-known ports of all the available NAT IP addresses are used in different subscribers\' connections (LSN sessions), and a subscriber initiates a connection from a well-known port, the NetScaler ADC drops this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._portpreserverange = portpreserverange
		except Exception as e:
			raise e

	@property
	def syncheck(self) :
		ur"""Silently drop any non-SYN packets for connections for which there is no LSN-NAT session present on the NetScaler ADC. 
		If you disable this parameter, the NetScaler ADC accepts any non-SYN packets and creates a new LSN session entry for this connection. 
		Following are some reasons for the NetScaler ADC to receive such packets:
		* LSN session for a connection existed but the NetScaler ADC removed this session because the LSN session was idle for a time that exceeded the configured session timeout.
		* Such packets can be a part of a DoS attack.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._syncheck
		except Exception as e:
			raise e

	@syncheck.setter
	def syncheck(self, syncheck) :
		ur"""Silently drop any non-SYN packets for connections for which there is no LSN-NAT session present on the NetScaler ADC. 
		If you disable this parameter, the NetScaler ADC accepts any non-SYN packets and creates a new LSN session entry for this connection. 
		Following are some reasons for the NetScaler ADC to receive such packets:
		* LSN session for a connection existed but the NetScaler ADC removed this session because the LSN session was idle for a time that exceeded the configured session timeout.
		* Such packets can be a part of a DoS attack.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._syncheck = syncheck
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsntransportprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsntransportprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.transportprofilename is not None :
				return str(self.transportprofilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add lsntransportprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = lsntransportprofile()
				addresource.transportprofilename = resource.transportprofilename
				addresource.transportprotocol = resource.transportprotocol
				addresource.sessiontimeout = resource.sessiontimeout
				addresource.finrsttimeout = resource.finrsttimeout
				addresource.stuntimeout = resource.stuntimeout
				addresource.synidletimeout = resource.synidletimeout
				addresource.portquota = resource.portquota
				addresource.sessionquota = resource.sessionquota
				addresource.groupsessionlimit = resource.groupsessionlimit
				addresource.portpreserveparity = resource.portpreserveparity
				addresource.portpreserverange = resource.portpreserverange
				addresource.syncheck = resource.syncheck
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsntransportprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].transportprofilename = resource[i].transportprofilename
						addresources[i].transportprotocol = resource[i].transportprotocol
						addresources[i].sessiontimeout = resource[i].sessiontimeout
						addresources[i].finrsttimeout = resource[i].finrsttimeout
						addresources[i].stuntimeout = resource[i].stuntimeout
						addresources[i].synidletimeout = resource[i].synidletimeout
						addresources[i].portquota = resource[i].portquota
						addresources[i].sessionquota = resource[i].sessionquota
						addresources[i].groupsessionlimit = resource[i].groupsessionlimit
						addresources[i].portpreserveparity = resource[i].portpreserveparity
						addresources[i].portpreserverange = resource[i].portpreserverange
						addresources[i].syncheck = resource[i].syncheck
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lsntransportprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsntransportprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.transportprofilename = resource
				else :
					deleteresource.transportprofilename = resource.transportprofilename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsntransportprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].transportprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsntransportprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].transportprofilename = resource[i].transportprofilename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update lsntransportprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = lsntransportprofile()
				updateresource.transportprofilename = resource.transportprofilename
				updateresource.sessiontimeout = resource.sessiontimeout
				updateresource.finrsttimeout = resource.finrsttimeout
				updateresource.stuntimeout = resource.stuntimeout
				updateresource.synidletimeout = resource.synidletimeout
				updateresource.portquota = resource.portquota
				updateresource.sessionquota = resource.sessionquota
				updateresource.groupsessionlimit = resource.groupsessionlimit
				updateresource.portpreserveparity = resource.portpreserveparity
				updateresource.portpreserverange = resource.portpreserverange
				updateresource.syncheck = resource.syncheck
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lsntransportprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].transportprofilename = resource[i].transportprofilename
						updateresources[i].sessiontimeout = resource[i].sessiontimeout
						updateresources[i].finrsttimeout = resource[i].finrsttimeout
						updateresources[i].stuntimeout = resource[i].stuntimeout
						updateresources[i].synidletimeout = resource[i].synidletimeout
						updateresources[i].portquota = resource[i].portquota
						updateresources[i].sessionquota = resource[i].sessionquota
						updateresources[i].groupsessionlimit = resource[i].groupsessionlimit
						updateresources[i].portpreserveparity = resource[i].portpreserveparity
						updateresources[i].portpreserverange = resource[i].portpreserverange
						updateresources[i].syncheck = resource[i].syncheck
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lsntransportprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lsntransportprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.transportprofilename = resource
				else :
					unsetresource.transportprofilename = resource.transportprofilename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsntransportprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].transportprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsntransportprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].transportprofilename = resource[i].transportprofilename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lsntransportprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsntransportprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lsntransportprofile()
						obj.transportprofilename = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lsntransportprofile() for _ in range(len(name))]
							obj = [lsntransportprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lsntransportprofile()
								obj[i].transportprofilename = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lsntransportprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsntransportprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lsntransportprofile resources configured on NetScaler.
		"""
		try :
			obj = lsntransportprofile()
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
		ur""" Use this API to count filtered the set of lsntransportprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsntransportprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Portpreserveparity:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Transportprotocol:
		TCP = "TCP"
		UDP = "UDP"
		ICMP = "ICMP"

	class Syncheck:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Portpreserverange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lsntransportprofile_response(base_response) :
	def __init__(self, length=1) :
		self.lsntransportprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsntransportprofile = [lsntransportprofile() for _ in range(length)]

