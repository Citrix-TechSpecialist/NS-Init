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

class lsnstatic(base_resource) :
	""" Configuration for static mapping resource. """
	def __init__(self) :
		self._name = ""
		self._transportprotocol = ""
		self._subscrip = ""
		self._subscrport = 0
		self._network6 = ""
		self._td = 0
		self._natip = ""
		self._natport = 0
		self._destip = ""
		self._dsttd = 0
		self._nattype = ""
		self._status = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the LSN static mapping entry. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN group is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn static1" or 'lsn static1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the LSN static mapping entry. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN group is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn static1" or 'lsn static1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def transportprotocol(self) :
		ur"""Protocol for the LSN mapping entry.<br/>Possible values = TCP, UDP, ICMP.
		"""
		try :
			return self._transportprotocol
		except Exception as e:
			raise e

	@transportprotocol.setter
	def transportprotocol(self, transportprotocol) :
		ur"""Protocol for the LSN mapping entry.<br/>Possible values = TCP, UDP, ICMP
		"""
		try :
			self._transportprotocol = transportprotocol
		except Exception as e:
			raise e

	@property
	def subscrip(self) :
		ur"""IPv4(NAT44 & DS-Lite)/IPv6(NAT64) address of an LSN subscriber for the LSN static mapping entry.
		"""
		try :
			return self._subscrip
		except Exception as e:
			raise e

	@subscrip.setter
	def subscrip(self, subscrip) :
		ur"""IPv4(NAT44 & DS-Lite)/IPv6(NAT64) address of an LSN subscriber for the LSN static mapping entry.
		"""
		try :
			self._subscrip = subscrip
		except Exception as e:
			raise e

	@property
	def subscrport(self) :
		ur"""Port of the LSN subscriber for the LSN mapping entry.<br/>Maximum length =  65535.
		"""
		try :
			return self._subscrport
		except Exception as e:
			raise e

	@subscrport.setter
	def subscrport(self, subscrport) :
		ur"""Port of the LSN subscriber for the LSN mapping entry.<br/>Maximum length =  65535
		"""
		try :
			self._subscrport = subscrport
		except Exception as e:
			raise e

	@property
	def network6(self) :
		ur"""B4 address in DS-Lite setup.<br/>Minimum length =  1.
		"""
		try :
			return self._network6
		except Exception as e:
			raise e

	@network6.setter
	def network6(self, network6) :
		ur"""B4 address in DS-Lite setup.<br/>Minimum length =  1
		"""
		try :
			self._network6 = network6
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""ID of the traffic domain to which the subscriber belongs. 
		If you do not specify an ID, the subscriber is assumed to be a part of the default traffic domain.<br/>Default value: 0<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""ID of the traffic domain to which the subscriber belongs. 
		If you do not specify an ID, the subscriber is assumed to be a part of the default traffic domain.<br/>Default value: 0<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def natip(self) :
		ur"""IPv4 address, already existing on the NetScaler ADC as type LSN, to be used as NAT IP address for this mapping entry.
		"""
		try :
			return self._natip
		except Exception as e:
			raise e

	@natip.setter
	def natip(self, natip) :
		ur"""IPv4 address, already existing on the NetScaler ADC as type LSN, to be used as NAT IP address for this mapping entry.
		"""
		try :
			self._natip = natip
		except Exception as e:
			raise e

	@property
	def natport(self) :
		ur"""NAT port for this LSN mapping entry.
		"""
		try :
			return self._natport
		except Exception as e:
			raise e

	@natport.setter
	def natport(self, natport) :
		ur"""NAT port for this LSN mapping entry.
		"""
		try :
			self._natport = natport
		except Exception as e:
			raise e

	@property
	def destip(self) :
		ur"""Destination IP address for the LSN mapping entry.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		ur"""Destination IP address for the LSN mapping entry.
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def dsttd(self) :
		ur"""ID of the traffic domain through which the destination IP address for this LSN mapping entry is reachable from the NetScaler ADC.
		If you do not specify an ID, the destination IP address is assumed to be reachable through the default traffic domain, which has an ID of 0.<br/>Default value: 0<br/>Maximum length =  4094.
		"""
		try :
			return self._dsttd
		except Exception as e:
			raise e

	@dsttd.setter
	def dsttd(self, dsttd) :
		ur"""ID of the traffic domain through which the destination IP address for this LSN mapping entry is reachable from the NetScaler ADC.
		If you do not specify an ID, the destination IP address is assumed to be reachable through the default traffic domain, which has an ID of 0.<br/>Default value: 0<br/>Maximum length =  4094
		"""
		try :
			self._dsttd = dsttd
		except Exception as e:
			raise e

	@property
	def nattype(self) :
		ur"""Type of sessions to be displayed.<br/>Possible values = NAT44, DS-Lite.
		"""
		try :
			return self._nattype
		except Exception as e:
			raise e

	@nattype.setter
	def nattype(self, nattype) :
		ur"""Type of sessions to be displayed.<br/>Possible values = NAT44, DS-Lite
		"""
		try :
			self._nattype = nattype
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""The status of the Mapping. Status could be Inactive, if mapping addition failed due to already existing dynamic/static mapping, port allocation failure.<br/>Possible values = ACTIVE, INACTIVE.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnstatic_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnstatic
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add lsnstatic.
		"""
		try :
			if type(resource) is not list :
				addresource = lsnstatic()
				addresource.name = resource.name
				addresource.transportprotocol = resource.transportprotocol
				addresource.subscrip = resource.subscrip
				addresource.subscrport = resource.subscrport
				addresource.network6 = resource.network6
				addresource.td = resource.td
				addresource.natip = resource.natip
				addresource.natport = resource.natport
				addresource.destip = resource.destip
				addresource.dsttd = resource.dsttd
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsnstatic() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].transportprotocol = resource[i].transportprotocol
						addresources[i].subscrip = resource[i].subscrip
						addresources[i].subscrport = resource[i].subscrport
						addresources[i].network6 = resource[i].network6
						addresources[i].td = resource[i].td
						addresources[i].natip = resource[i].natip
						addresources[i].natport = resource[i].natport
						addresources[i].destip = resource[i].destip
						addresources[i].dsttd = resource[i].dsttd
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lsnstatic.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsnstatic()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnstatic() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnstatic() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lsnstatic resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnstatic()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lsnstatic()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lsnstatic() for _ in range(len(name))]
							obj = [lsnstatic() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lsnstatic()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the lsnstatic resources that are configured on netscaler.
	# This uses lsnstatic_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = lsnstatic()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lsnstatic resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnstatic()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lsnstatic resources configured on NetScaler.
		"""
		try :
			obj = lsnstatic()
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
		ur""" Use this API to count filtered the set of lsnstatic resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnstatic()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Transportprotocol:
		TCP = "TCP"
		UDP = "UDP"
		ICMP = "ICMP"

	class Status:
		ACTIVE = "ACTIVE"
		INACTIVE = "INACTIVE"

	class Nattype:
		NAT44 = "NAT44"
		DS_Lite = "DS-Lite"

class lsnstatic_response(base_response) :
	def __init__(self, length=1) :
		self.lsnstatic = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnstatic = [lsnstatic() for _ in range(length)]

