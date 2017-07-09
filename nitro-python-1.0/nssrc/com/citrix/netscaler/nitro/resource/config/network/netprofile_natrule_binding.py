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

class netprofile_natrule_binding(base_resource) :
	""" Binding class showing the natrule that can be bound to netprofile.
	"""
	def __init__(self) :
		self._natrule = ""
		self._netmask = ""
		self._rewriteip = ""
		self._name = ""
		self.___count = 0

	@property
	def rewriteip(self) :
		try :
			return self._rewriteip
		except Exception as e:
			raise e

	@rewriteip.setter
	def rewriteip(self, rewriteip) :
		try :
			self._rewriteip = rewriteip
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Name of the netprofile to which to bind port ranges.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the netprofile to which to bind port ranges.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def natrule(self) :
		ur"""IPv4 network address on whose traffic you want the NetScaler appliance to do rewrite ip prefix.
		"""
		try :
			return self._natrule
		except Exception as e:
			raise e

	@natrule.setter
	def natrule(self, natrule) :
		ur"""IPv4 network address on whose traffic you want the NetScaler appliance to do rewrite ip prefix.
		"""
		try :
			self._natrule = natrule
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(netprofile_natrule_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.netprofile_natrule_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = netprofile_natrule_binding()
				updateresource.name = resource.name
				updateresource.natrule = resource.natrule
				updateresource.netmask = resource.netmask
				updateresource.rewriteip = resource.rewriteip
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [netprofile_natrule_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].natrule = resource[i].natrule
						updateresources[i].netmask = resource[i].netmask
						updateresources[i].rewriteip = resource[i].rewriteip
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = netprofile_natrule_binding()
				deleteresource.name = resource.name
				deleteresource.natrule = resource.natrule
				deleteresource.netmask = resource.netmask
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [netprofile_natrule_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].natrule = resource[i].natrule
						deleteresources[i].netmask = resource[i].netmask
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch netprofile_natrule_binding resources.
		"""
		try :
			obj = netprofile_natrule_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of netprofile_natrule_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = netprofile_natrule_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count netprofile_natrule_binding resources configued on NetScaler.
		"""
		try :
			obj = netprofile_natrule_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		ur""" Use this API to count the filtered set of netprofile_natrule_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = netprofile_natrule_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class netprofile_natrule_binding_response(base_response) :
	def __init__(self, length=1) :
		self.netprofile_natrule_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.netprofile_natrule_binding = [netprofile_natrule_binding() for _ in range(length)]

