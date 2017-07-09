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

class nspartition_vlan_binding(base_resource) :
	""" Binding class showing the vlan that can be bound to nspartition.
	"""
	def __init__(self) :
		self._vlan = 0
		self._vlan = 0
		self._partitionname = ""
		self.___count = 0

	@property
	def vlan(self) :
		ur"""Identifier of the vlan that is assigned to this partition.<br/>Minimum value =  1<br/>Maximum value =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		ur"""Identifier of the vlan that is assigned to this partition.<br/>Minimum value =  1<br/>Maximum value =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def partitionname(self) :
		ur"""Name of the Partition. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._partitionname
		except Exception as e:
			raise e

	@partitionname.setter
	def partitionname(self, partitionname) :
		ur"""Name of the Partition. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._partitionname = partitionname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nspartition_vlan_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nspartition_vlan_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.partitionname is not None :
				return str(self.partitionname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = nspartition_vlan_binding()
				updateresource.partitionname = resource.partitionname
				updateresource.vlan = resource.vlan
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [nspartition_vlan_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].partitionname = resource[i].partitionname
						updateresources[i].vlan = resource[i].vlan
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = nspartition_vlan_binding()
				deleteresource.partitionname = resource.partitionname
				deleteresource.vlan = resource.vlan
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [nspartition_vlan_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].partitionname = resource[i].partitionname
						deleteresources[i].vlan = resource[i].vlan
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, partitionname) :
		ur""" Use this API to fetch nspartition_vlan_binding resources.
		"""
		try :
			obj = nspartition_vlan_binding()
			obj.partitionname = partitionname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, partitionname, filter_) :
		ur""" Use this API to fetch filtered set of nspartition_vlan_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nspartition_vlan_binding()
			obj.partitionname = partitionname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, partitionname) :
		ur""" Use this API to count nspartition_vlan_binding resources configued on NetScaler.
		"""
		try :
			obj = nspartition_vlan_binding()
			obj.partitionname = partitionname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, partitionname, filter_) :
		ur""" Use this API to count the filtered set of nspartition_vlan_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nspartition_vlan_binding()
			obj.partitionname = partitionname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class nspartition_vlan_binding_response(base_response) :
	def __init__(self, length=1) :
		self.nspartition_vlan_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nspartition_vlan_binding = [nspartition_vlan_binding() for _ in range(length)]

