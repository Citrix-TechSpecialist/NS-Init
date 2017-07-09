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

class nslicenseproxyserver(base_resource) :
	""" Configuration for licenseproxyserver resource. """
	def __init__(self) :
		self._serverip = ""
		self._servername = ""
		self._port = 0
		self.___count = 0

	@property
	def serverip(self) :
		ur"""IP address of the License proxy server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		ur"""IP address of the License proxy server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def servername(self) :
		ur"""Fully qualified domain name of the License proxy server.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		ur"""Fully qualified domain name of the License proxy server.
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""License proxy server port.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""License proxy server port.
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslicenseproxyserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslicenseproxyserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.serverip is not None :
				return str(self.serverip)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add nslicenseproxyserver.
		"""
		try :
			if type(resource) is not list :
				addresource = nslicenseproxyserver()
				addresource.serverip = resource.serverip
				addresource.servername = resource.servername
				addresource.port = resource.port
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nslicenseproxyserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].serverip = resource[i].serverip
						addresources[i].servername = resource[i].servername
						addresources[i].port = resource[i].port
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nslicenseproxyserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nslicenseproxyserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.serverip = resource
				else :
					deleteresource.serverip = resource.serverip
					deleteresource.servername = resource.servername
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nslicenseproxyserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].serverip = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nslicenseproxyserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].serverip = resource[i].serverip
							deleteresources[i].servername = resource[i].servername
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nslicenseproxyserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = nslicenseproxyserver()
				updateresource.serverip = resource.serverip
				updateresource.servername = resource.servername
				updateresource.port = resource.port
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nslicenseproxyserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].serverip = resource[i].serverip
						updateresources[i].servername = resource[i].servername
						updateresources[i].port = resource[i].port
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nslicenseproxyserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nslicenseproxyserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) == cls :
					if type(name) is not list :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name)
						response = name.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nslicenseproxyserver() for _ in range(len(name))]
							for i in range(len(name)) :
								option_ = options()
								option_.args = nitro_util.object_to_string_withoutquotes(name[i])
								response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nslicenseproxyserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nslicenseproxyserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nslicenseproxyserver resources configured on NetScaler.
		"""
		try :
			obj = nslicenseproxyserver()
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
		ur""" Use this API to count filtered the set of nslicenseproxyserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nslicenseproxyserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nslicenseproxyserver_response(base_response) :
	def __init__(self, length=1) :
		self.nslicenseproxyserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslicenseproxyserver = [nslicenseproxyserver() for _ in range(length)]

