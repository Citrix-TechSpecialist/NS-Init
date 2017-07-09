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

class nsservicefunction(base_resource) :
	""" Configuration for service Function resource. """
	def __init__(self) :
		self._servicefunctionname = ""
		self._ingressvlan = 0
		self.___count = 0

	@property
	def servicefunctionname(self) :
		ur"""Name of the service function to be created. Leading character must be a number or letter. Other characters allowed, after the first character, are @ _ - . (period) : (colon) # and space ( ).<br/>Minimum length =  1.
		"""
		try :
			return self._servicefunctionname
		except Exception as e:
			raise e

	@servicefunctionname.setter
	def servicefunctionname(self, servicefunctionname) :
		ur"""Name of the service function to be created. Leading character must be a number or letter. Other characters allowed, after the first character, are @ _ - . (period) : (colon) # and space ( ).<br/>Minimum length =  1
		"""
		try :
			self._servicefunctionname = servicefunctionname
		except Exception as e:
			raise e

	@property
	def ingressvlan(self) :
		ur"""VLAN ID on which the traffic from service function reaches Netscaler.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._ingressvlan
		except Exception as e:
			raise e

	@ingressvlan.setter
	def ingressvlan(self, ingressvlan) :
		ur"""VLAN ID on which the traffic from service function reaches Netscaler.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._ingressvlan = ingressvlan
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsservicefunction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsservicefunction
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicefunctionname is not None :
				return str(self.servicefunctionname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add nsservicefunction.
		"""
		try :
			if type(resource) is not list :
				addresource = nsservicefunction()
				addresource.servicefunctionname = resource.servicefunctionname
				addresource.ingressvlan = resource.ingressvlan
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsservicefunction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].servicefunctionname = resource[i].servicefunctionname
						addresources[i].ingressvlan = resource[i].ingressvlan
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nsservicefunction.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsservicefunction()
				updateresource.servicefunctionname = resource.servicefunctionname
				updateresource.ingressvlan = resource.ingressvlan
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsservicefunction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicefunctionname = resource[i].servicefunctionname
						updateresources[i].ingressvlan = resource[i].ingressvlan
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nsservicefunction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsservicefunction()
				if type(resource) !=  type(deleteresource):
					deleteresource.servicefunctionname = resource
				else :
					deleteresource.servicefunctionname = resource.servicefunctionname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsservicefunction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].servicefunctionname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsservicefunction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].servicefunctionname = resource[i].servicefunctionname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsservicefunction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsservicefunction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nsservicefunction()
						obj.servicefunctionname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nsservicefunction() for _ in range(len(name))]
							obj = [nsservicefunction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nsservicefunction()
								obj[i].servicefunctionname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nsservicefunction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsservicefunction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nsservicefunction resources configured on NetScaler.
		"""
		try :
			obj = nsservicefunction()
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
		ur""" Use this API to count filtered the set of nsservicefunction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsservicefunction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nsservicefunction_response(base_response) :
	def __init__(self, length=1) :
		self.nsservicefunction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsservicefunction = [nsservicefunction() for _ in range(length)]

