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

class lsnpool(base_resource) :
	""" Configuration for LSN pool resource. """
	def __init__(self) :
		self._poolname = ""
		self._nattype = ""
		self._portblockallocation = ""
		self._portrealloctimeout = 0
		self._maxportrealloctmq = 0
		self.___count = 0

	@property
	def poolname(self) :
		ur"""Name for the LSN pool. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN pool is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn pool1" or 'lsn pool1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._poolname
		except Exception as e:
			raise e

	@poolname.setter
	def poolname(self, poolname) :
		ur"""Name for the LSN pool. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN pool is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn pool1" or 'lsn pool1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._poolname = poolname
		except Exception as e:
			raise e

	@property
	def nattype(self) :
		ur"""Type of NAT IP address and port allocation (from the LSN pools bound to an LSN group) for subscribers (of the LSN client entity bound to the LSN group):
		Available options function as follows:
		* Deterministic - Allocate a NAT IP address and a block of ports to each subscriber (of the LSN client bound to the LSN group). The NetScaler ADC sequentially allocates NAT resources to these subscribers. The NetScaler ADC assigns the first block of ports (block size determined by the port block size parameter of the LSN group) on the beginning NAT IP address to the beginning subscriber IP address. The next range of ports is assigned to the next subscriber, and so on, until the NAT address does not have enough ports for the next subscriber. In this case, the first port block on the next NAT address is used for the subscriber, and so on.  Because each subscriber now receives a deterministic NAT IP address and a block of ports, a subscriber can be identified without any need for logging. For a connection, a subscriber can be identified based only on the NAT IP address and port, and the destination IP address and port.
		* Dynamic - Allocate a random NAT IP address and a port from the LSN NAT pool for a subscriber\'s connection. If port block allocation is enabled (in LSN pool) and a port block size is specified (in the LSN group), the NetScaler ADC allocates a random NAT IP address and a block of ports for a subscriber when it initiates a connection for the first time. The ADC allocates this NAT IP address and a port (from the allocated block of ports) for different connections from this subscriber. If all the ports are allocated (for different subscriber\'s connections) from the subscriber\'s allocated port block, the ADC allocates a new random port block for the subscriber.
		Only LSN Pools and LSN groups with the same NAT type settings can be bound together. Multiples LSN pools can be bound to an LSN group. A maximum of 16 LSN pools can be bound to an LSN group. .<br/>Default value: DYNAMIC<br/>Possible values = DYNAMIC, DETERMINISTIC.
		"""
		try :
			return self._nattype
		except Exception as e:
			raise e

	@nattype.setter
	def nattype(self, nattype) :
		ur"""Type of NAT IP address and port allocation (from the LSN pools bound to an LSN group) for subscribers (of the LSN client entity bound to the LSN group):
		Available options function as follows:
		* Deterministic - Allocate a NAT IP address and a block of ports to each subscriber (of the LSN client bound to the LSN group). The NetScaler ADC sequentially allocates NAT resources to these subscribers. The NetScaler ADC assigns the first block of ports (block size determined by the port block size parameter of the LSN group) on the beginning NAT IP address to the beginning subscriber IP address. The next range of ports is assigned to the next subscriber, and so on, until the NAT address does not have enough ports for the next subscriber. In this case, the first port block on the next NAT address is used for the subscriber, and so on.  Because each subscriber now receives a deterministic NAT IP address and a block of ports, a subscriber can be identified without any need for logging. For a connection, a subscriber can be identified based only on the NAT IP address and port, and the destination IP address and port.
		* Dynamic - Allocate a random NAT IP address and a port from the LSN NAT pool for a subscriber\'s connection. If port block allocation is enabled (in LSN pool) and a port block size is specified (in the LSN group), the NetScaler ADC allocates a random NAT IP address and a block of ports for a subscriber when it initiates a connection for the first time. The ADC allocates this NAT IP address and a port (from the allocated block of ports) for different connections from this subscriber. If all the ports are allocated (for different subscriber\'s connections) from the subscriber\'s allocated port block, the ADC allocates a new random port block for the subscriber.
		Only LSN Pools and LSN groups with the same NAT type settings can be bound together. Multiples LSN pools can be bound to an LSN group. A maximum of 16 LSN pools can be bound to an LSN group. .<br/>Default value: DYNAMIC<br/>Possible values = DYNAMIC, DETERMINISTIC
		"""
		try :
			self._nattype = nattype
		except Exception as e:
			raise e

	@property
	def portblockallocation(self) :
		ur"""Allocate a random NAT port block, from the available NAT port pool of an NAT IP address, for each subscriber when the NAT allocation is set as Dynamic NAT. For any connection initiated from a subscriber, the NetScaler ADC allocates a NAT port from the subscriber\'s allocated NAT port block to create the LSN session.
		You must set the port block size in the bound LSN group. For a subscriber, if all the ports are allocated from the subscriber\'s allocated port block, the NetScaler ADC allocates a new random port block for the subscriber.
		For Deterministic NAT, this parameter is enabled by default, and you cannot disable it.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._portblockallocation
		except Exception as e:
			raise e

	@portblockallocation.setter
	def portblockallocation(self, portblockallocation) :
		ur"""Allocate a random NAT port block, from the available NAT port pool of an NAT IP address, for each subscriber when the NAT allocation is set as Dynamic NAT. For any connection initiated from a subscriber, the NetScaler ADC allocates a NAT port from the subscriber\'s allocated NAT port block to create the LSN session.
		You must set the port block size in the bound LSN group. For a subscriber, if all the ports are allocated from the subscriber\'s allocated port block, the NetScaler ADC allocates a new random port block for the subscriber.
		For Deterministic NAT, this parameter is enabled by default, and you cannot disable it.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._portblockallocation = portblockallocation
		except Exception as e:
			raise e

	@property
	def portrealloctimeout(self) :
		ur"""The waiting time, in seconds, between deallocating LSN NAT ports (when an LSN mapping is removed) and reallocating them for a new LSN session. This parameter is necessary in order to prevent collisions between old and new mappings and sessions. It ensures that all established sessions are broken instead of redirected to a different subscriber. This is not applicable for ports used in:
		* Deterministic NAT
		* Address-Dependent filtering and Address-Port-Dependent filtering
		* Dynamic NAT with port block allocation
		In these cases, ports are immediately reallocated.<br/>Default value: 0<br/>Maximum length =  600.
		"""
		try :
			return self._portrealloctimeout
		except Exception as e:
			raise e

	@portrealloctimeout.setter
	def portrealloctimeout(self, portrealloctimeout) :
		ur"""The waiting time, in seconds, between deallocating LSN NAT ports (when an LSN mapping is removed) and reallocating them for a new LSN session. This parameter is necessary in order to prevent collisions between old and new mappings and sessions. It ensures that all established sessions are broken instead of redirected to a different subscriber. This is not applicable for ports used in:
		* Deterministic NAT
		* Address-Dependent filtering and Address-Port-Dependent filtering
		* Dynamic NAT with port block allocation
		In these cases, ports are immediately reallocated.<br/>Default value: 0<br/>Maximum length =  600
		"""
		try :
			self._portrealloctimeout = portrealloctimeout
		except Exception as e:
			raise e

	@property
	def maxportrealloctmq(self) :
		ur"""Maximum number of ports for which the port reallocation timeout applies for each NAT IP address. In other words, the maximum deallocated-port queue size for which the reallocation timeout applies for each NAT IP address.
		When the queue size is full, the next port deallocated is reallocated immediately for a new LSN session.<br/>Default value: 65536<br/>Maximum length =  65536.
		"""
		try :
			return self._maxportrealloctmq
		except Exception as e:
			raise e

	@maxportrealloctmq.setter
	def maxportrealloctmq(self, maxportrealloctmq) :
		ur"""Maximum number of ports for which the port reallocation timeout applies for each NAT IP address. In other words, the maximum deallocated-port queue size for which the reallocation timeout applies for each NAT IP address.
		When the queue size is full, the next port deallocated is reallocated immediately for a new LSN session.<br/>Default value: 65536<br/>Maximum length =  65536
		"""
		try :
			self._maxportrealloctmq = maxportrealloctmq
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnpool_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnpool
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.poolname is not None :
				return str(self.poolname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add lsnpool.
		"""
		try :
			if type(resource) is not list :
				addresource = lsnpool()
				addresource.poolname = resource.poolname
				addresource.nattype = resource.nattype
				addresource.portblockallocation = resource.portblockallocation
				addresource.portrealloctimeout = resource.portrealloctimeout
				addresource.maxportrealloctmq = resource.maxportrealloctmq
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsnpool() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].poolname = resource[i].poolname
						addresources[i].nattype = resource[i].nattype
						addresources[i].portblockallocation = resource[i].portblockallocation
						addresources[i].portrealloctimeout = resource[i].portrealloctimeout
						addresources[i].maxportrealloctmq = resource[i].maxportrealloctmq
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lsnpool.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsnpool()
				if type(resource) !=  type(deleteresource):
					deleteresource.poolname = resource
				else :
					deleteresource.poolname = resource.poolname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnpool() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].poolname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnpool() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].poolname = resource[i].poolname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update lsnpool.
		"""
		try :
			if type(resource) is not list :
				updateresource = lsnpool()
				updateresource.poolname = resource.poolname
				updateresource.portrealloctimeout = resource.portrealloctimeout
				updateresource.maxportrealloctmq = resource.maxportrealloctmq
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lsnpool() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].poolname = resource[i].poolname
						updateresources[i].portrealloctimeout = resource[i].portrealloctimeout
						updateresources[i].maxportrealloctmq = resource[i].maxportrealloctmq
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lsnpool resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lsnpool()
				if type(resource) !=  type(unsetresource):
					unsetresource.poolname = resource
				else :
					unsetresource.poolname = resource.poolname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnpool() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].poolname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnpool() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].poolname = resource[i].poolname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lsnpool resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnpool()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lsnpool()
						obj.poolname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lsnpool() for _ in range(len(name))]
							obj = [lsnpool() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lsnpool()
								obj[i].poolname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lsnpool resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnpool()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lsnpool resources configured on NetScaler.
		"""
		try :
			obj = lsnpool()
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
		ur""" Use this API to count filtered the set of lsnpool resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnpool()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Portblockallocation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nattype:
		DYNAMIC = "DYNAMIC"
		DETERMINISTIC = "DETERMINISTIC"

class lsnpool_response(base_response) :
	def __init__(self, length=1) :
		self.lsnpool = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnpool = [lsnpool() for _ in range(length)]

