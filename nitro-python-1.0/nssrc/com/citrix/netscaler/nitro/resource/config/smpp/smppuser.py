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

class smppuser(base_resource) :
	""" Configuration for SMPP user resource. """
	def __init__(self) :
		self._username = ""
		self._password = ""
		self.___count = 0

	@property
	def username(self) :
		ur"""Name of the SMPP user. Must be the same as the user name specified in the SMPP server.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""Name of the SMPP user. Must be the same as the user name specified in the SMPP server.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password for binding to the SMPP server. Must be the same as the password specified in the SMPP server.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password for binding to the SMPP server. Must be the same as the password specified in the SMPP server.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(smppuser_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.smppuser
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.username is not None :
				return str(self.username)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add smppuser.
		"""
		try :
			if type(resource) is not list :
				addresource = smppuser()
				addresource.username = resource.username
				addresource.password = resource.password
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ smppuser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].username = resource[i].username
						addresources[i].password = resource[i].password
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete smppuser.
		"""
		try :
			if type(resource) is not list :
				deleteresource = smppuser()
				if type(resource) !=  type(deleteresource):
					deleteresource.username = resource
				else :
					deleteresource.username = resource.username
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ smppuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].username = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ smppuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].username = resource[i].username
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update smppuser.
		"""
		try :
			if type(resource) is not list :
				updateresource = smppuser()
				updateresource.username = resource.username
				updateresource.password = resource.password
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ smppuser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].username = resource[i].username
						updateresources[i].password = resource[i].password
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the smppuser resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = smppuser()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = smppuser()
						obj.username = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [smppuser() for _ in range(len(name))]
							obj = [smppuser() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = smppuser()
								obj[i].username = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of smppuser resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = smppuser()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the smppuser resources configured on NetScaler.
		"""
		try :
			obj = smppuser()
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
		ur""" Use this API to count filtered the set of smppuser resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = smppuser()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class smppuser_response(base_response) :
	def __init__(self, length=1) :
		self.smppuser = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.smppuser = [smppuser() for _ in range(length)]

