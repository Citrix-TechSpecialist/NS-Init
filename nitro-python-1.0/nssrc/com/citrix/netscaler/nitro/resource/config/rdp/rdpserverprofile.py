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

class rdpserverprofile(base_resource) :
	""" Configuration for RDP serverprofile resource. """
	def __init__(self) :
		self._name = ""
		self._rdpip = ""
		self._rdpport = 0
		self._psk = ""
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""The name of the rdp server profile.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The name of the rdp server profile.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def rdpip(self) :
		ur"""IPv4 or IPv6 address of RDP listener. This terminates client RDP connections.<br/>Minimum length =  1.
		"""
		try :
			return self._rdpip
		except Exception as e:
			raise e

	@rdpip.setter
	def rdpip(self, rdpip) :
		ur"""IPv4 or IPv6 address of RDP listener. This terminates client RDP connections.<br/>Minimum length =  1
		"""
		try :
			self._rdpip = rdpip
		except Exception as e:
			raise e

	@property
	def rdpport(self) :
		ur"""TCP port on which the RDP connection is established.<br/>Default value: 3389<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._rdpport
		except Exception as e:
			raise e

	@rdpport.setter
	def rdpport(self, rdpport) :
		ur"""TCP port on which the RDP connection is established.<br/>Default value: 3389<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._rdpport = rdpport
		except Exception as e:
			raise e

	@property
	def psk(self) :
		ur"""Pre shared key value.
		"""
		try :
			return self._psk
		except Exception as e:
			raise e

	@psk.setter
	def psk(self, psk) :
		ur"""Pre shared key value.
		"""
		try :
			self._psk = psk
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rdpserverprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rdpserverprofile
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
		ur""" Use this API to add rdpserverprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = rdpserverprofile()
				addresource.name = resource.name
				addresource.rdpip = resource.rdpip
				addresource.rdpport = resource.rdpport
				addresource.psk = resource.psk
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ rdpserverprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].rdpip = resource[i].rdpip
						addresources[i].rdpport = resource[i].rdpport
						addresources[i].psk = resource[i].psk
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update rdpserverprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = rdpserverprofile()
				updateresource.name = resource.name
				updateresource.rdpip = resource.rdpip
				updateresource.rdpport = resource.rdpport
				updateresource.psk = resource.psk
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ rdpserverprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].rdpip = resource[i].rdpip
						updateresources[i].rdpport = resource[i].rdpport
						updateresources[i].psk = resource[i].psk
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of rdpserverprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = rdpserverprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ rdpserverprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ rdpserverprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete rdpserverprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = rdpserverprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ rdpserverprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ rdpserverprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the rdpserverprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = rdpserverprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = rdpserverprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [rdpserverprofile() for _ in range(len(name))]
							obj = [rdpserverprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = rdpserverprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of rdpserverprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rdpserverprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the rdpserverprofile resources configured on NetScaler.
		"""
		try :
			obj = rdpserverprofile()
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
		ur""" Use this API to count filtered the set of rdpserverprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rdpserverprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

class rdpserverprofile_response(base_response) :
	def __init__(self, length=1) :
		self.rdpserverprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rdpserverprofile = [rdpserverprofile() for _ in range(length)]

