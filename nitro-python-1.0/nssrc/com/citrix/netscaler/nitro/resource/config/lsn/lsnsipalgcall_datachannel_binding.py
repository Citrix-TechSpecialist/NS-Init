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

class lsnsipalgcall_datachannel_binding(base_resource) :
	""" Binding class showing the datachannel that can be bound to lsnsipalgcall.
	"""
	def __init__(self) :
		self._channelip = ""
		self._channelnatip = ""
		self._channelport = 0
		self._channelnatport = 0
		self._channelprotocol = ""
		self._channelflags = 0
		self._channeltimeout = 0
		self._callid = ""
		self.___count = 0

	@property
	def channelip(self) :
		ur"""IP address of the channel.
		"""
		try :
			return self._channelip
		except Exception as e:
			raise e

	@channelip.setter
	def channelip(self, channelip) :
		ur"""IP address of the channel.
		"""
		try :
			self._channelip = channelip
		except Exception as e:
			raise e

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
	def channelnatip(self) :
		ur"""Natted IP address of the channel.
		"""
		try :
			return self._channelnatip
		except Exception as e:
			raise e

	@property
	def channelport(self) :
		ur"""port for the channel.
		"""
		try :
			return self._channelport
		except Exception as e:
			raise e

	@property
	def channelflags(self) :
		ur"""Flags for the call entry.
		"""
		try :
			return self._channelflags
		except Exception as e:
			raise e

	@property
	def channeltimeout(self) :
		ur"""Timeout for the channel.
		"""
		try :
			return self._channeltimeout
		except Exception as e:
			raise e

	@property
	def channelnatport(self) :
		ur"""Natted port for the channel.
		"""
		try :
			return self._channelnatport
		except Exception as e:
			raise e

	@property
	def channelprotocol(self) :
		ur"""Channel transport protocol.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, HTTPSVR, HTTPCLIENT, NAT, HA, AAA, SINCTCP, VPN AFTP, MONITORS, SSLVPN UDP, SINCUDP, RIP, UDP CLNT, SASP, RPCCLNTS, ROUTE, AUDIT, STA HTTP, STA SSL, DNS RESOLVE, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE, ICA, RADIUS, RADIUSListener, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, TFTP_DATA.
		"""
		try :
			return self._channelprotocol
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnsipalgcall_datachannel_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnsipalgcall_datachannel_binding
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
	def get(cls, service, callid) :
		ur""" Use this API to fetch lsnsipalgcall_datachannel_binding resources.
		"""
		try :
			obj = lsnsipalgcall_datachannel_binding()
			obj.callid = callid
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, callid, filter_) :
		ur""" Use this API to fetch filtered set of lsnsipalgcall_datachannel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnsipalgcall_datachannel_binding()
			obj.callid = callid
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, callid) :
		ur""" Use this API to count lsnsipalgcall_datachannel_binding resources configued on NetScaler.
		"""
		try :
			obj = lsnsipalgcall_datachannel_binding()
			obj.callid = callid
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, callid, filter_) :
		ur""" Use this API to count the filtered set of lsnsipalgcall_datachannel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnsipalgcall_datachannel_binding()
			obj.callid = callid
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Channelprotocol:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		NNTP = "NNTP"
		RPCSVR = "RPCSVR"
		DNS = "DNS"
		ADNS = "ADNS"
		SNMP = "SNMP"
		RTSP = "RTSP"
		DHCPRA = "DHCPRA"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		DNS_TCP = "DNS_TCP"
		ADNS_TCP = "ADNS_TCP"
		HTTPSVR = "HTTPSVR"
		HTTPCLIENT = "HTTPCLIENT"
		NAT = "NAT"
		HA = "HA"
		AAA = "AAA"
		SINCTCP = "SINCTCP"
		VPN_AFTP = "VPN AFTP"
		MONITORS = "MONITORS"
		SSLVPN_UDP = "SSLVPN UDP"
		SINCUDP = "SINCUDP"
		RIP = "RIP"
		UDP_CLNT = "UDP CLNT"
		SASP = "SASP"
		RPCCLNTS = "RPCCLNTS"
		ROUTE = "ROUTE"
		AUDIT = "AUDIT"
		STA_HTTP = "STA HTTP"
		STA_SSL = "STA SSL"
		DNS_RESOLVE = "DNS RESOLVE"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		ORACLE = "ORACLE"
		ICA = "ICA"
		RADIUS = "RADIUS"
		RADIUSListener = "RADIUSListener"
		SMPP = "SMPP"
		PPTP = "PPTP"
		GRE = "GRE"
		SYSLOGTCP = "SYSLOGTCP"
		SYSLOGUDP = "SYSLOGUDP"
		FIX = "FIX"
		TFTP_DATA = "TFTP_DATA"

class lsnsipalgcall_datachannel_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsnsipalgcall_datachannel_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnsipalgcall_datachannel_binding = [lsnsipalgcall_datachannel_binding() for _ in range(length)]

