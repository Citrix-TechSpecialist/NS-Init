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

class nsservicepath(base_resource) :
	""" Configuration for service Chain resource. """
	def __init__(self) :
		self._servicepathname = ""
		self.___count = 0

	@property
	def servicepathname(self) :
		ur"""Name for the Service path. Must begin with an ASCII alphanumeric or underscore (_) character, and must 
		contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
		characters.<br/>Minimum length =  1.
		"""
		try :
			return self._servicepathname
		except Exception as e:
			raise e

	@servicepathname.setter
	def servicepathname(self, servicepathname) :
		ur"""Name for the Service path. Must begin with an ASCII alphanumeric or underscore (_) character, and must 
		contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
		characters.<br/>Minimum length =  1
		"""
		try :
			self._servicepathname = servicepathname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsservicepath_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsservicepath
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicepathname is not None :
				return str(self.servicepathname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add nsservicepath.
		"""
		try :
			if type(resource) is not list :
				addresource = nsservicepath()
				addresource.servicepathname = resource.servicepathname
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsservicepath() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].servicepathname = resource[i].servicepathname
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nsservicepath.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsservicepath()
				if type(resource) !=  type(deleteresource):
					deleteresource.servicepathname = resource
				else :
					deleteresource.servicepathname = resource.servicepathname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsservicepath() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].servicepathname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsservicepath() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].servicepathname = resource[i].servicepathname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsservicepath resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsservicepath()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nsservicepath()
						obj.servicepathname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nsservicepath() for _ in range(len(name))]
							obj = [nsservicepath() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nsservicepath()
								obj[i].servicepathname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nsservicepath resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsservicepath()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nsservicepath resources configured on NetScaler.
		"""
		try :
			obj = nsservicepath()
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
		ur""" Use this API to count filtered the set of nsservicepath resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsservicepath()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nsservicepath_response(base_response) :
	def __init__(self, length=1) :
		self.nsservicepath = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsservicepath = [nsservicepath() for _ in range(length)]

