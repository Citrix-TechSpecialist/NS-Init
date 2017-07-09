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

class lsnappsprofile_port_binding(base_resource) :
	""" Binding class showing the port that can be bound to lsnappsprofile.
	"""
	def __init__(self) :
		self._lsnport = ""
		self._appsprofilename = ""
		self.___count = 0

	@property
	def appsprofilename(self) :
		ur"""Name for the LSN application profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN application profile is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn application profile1" or 'lsn application profile1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._appsprofilename
		except Exception as e:
			raise e

	@appsprofilename.setter
	def appsprofilename(self, appsprofilename) :
		ur"""Name for the LSN application profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN application profile is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn application profile1" or 'lsn application profile1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._appsprofilename = appsprofilename
		except Exception as e:
			raise e

	@property
	def lsnport(self) :
		ur"""Port numbers or range of port numbers to match against the destination port of the incoming packet from a subscriber. When the destination port is matched, the LSN application profile is applied for the LSN session. Separate a range of ports with a hyphen. For example, 40-90.
		"""
		try :
			return self._lsnport
		except Exception as e:
			raise e

	@lsnport.setter
	def lsnport(self, lsnport) :
		ur"""Port numbers or range of port numbers to match against the destination port of the incoming packet from a subscriber. When the destination port is matched, the LSN application profile is applied for the LSN session. Separate a range of ports with a hyphen. For example, 40-90.
		"""
		try :
			self._lsnport = lsnport
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnappsprofile_port_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnappsprofile_port_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.appsprofilename is not None :
				return str(self.appsprofilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = lsnappsprofile_port_binding()
				updateresource.appsprofilename = resource.appsprofilename
				updateresource.lsnport = resource.lsnport
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lsnappsprofile_port_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].appsprofilename = resource[i].appsprofilename
						updateresources[i].lsnport = resource[i].lsnport
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = lsnappsprofile_port_binding()
				deleteresource.appsprofilename = resource.appsprofilename
				deleteresource.lsnport = resource.lsnport
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lsnappsprofile_port_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].appsprofilename = resource[i].appsprofilename
						deleteresources[i].lsnport = resource[i].lsnport
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, appsprofilename) :
		ur""" Use this API to fetch lsnappsprofile_port_binding resources.
		"""
		try :
			obj = lsnappsprofile_port_binding()
			obj.appsprofilename = appsprofilename
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, appsprofilename, filter_) :
		ur""" Use this API to fetch filtered set of lsnappsprofile_port_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnappsprofile_port_binding()
			obj.appsprofilename = appsprofilename
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, appsprofilename) :
		ur""" Use this API to count lsnappsprofile_port_binding resources configued on NetScaler.
		"""
		try :
			obj = lsnappsprofile_port_binding()
			obj.appsprofilename = appsprofilename
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, appsprofilename, filter_) :
		ur""" Use this API to count the filtered set of lsnappsprofile_port_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnappsprofile_port_binding()
			obj.appsprofilename = appsprofilename
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class lsnappsprofile_port_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsnappsprofile_port_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnappsprofile_port_binding = [lsnappsprofile_port_binding() for _ in range(length)]

