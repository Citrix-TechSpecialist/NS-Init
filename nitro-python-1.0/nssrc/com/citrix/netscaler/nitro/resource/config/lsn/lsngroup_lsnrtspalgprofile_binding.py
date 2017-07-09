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

class lsngroup_lsnrtspalgprofile_binding(base_resource) :
	""" Binding class showing the lsnrtspalgprofile that can be bound to lsngroup.
	"""
	def __init__(self) :
		self._rtspalgprofilename = ""
		self._groupname = ""
		self.___count = 0

	@property
	def rtspalgprofilename(self) :
		ur"""The name of the LSN RTSP ALG Profile.
		"""
		try :
			return self._rtspalgprofilename
		except Exception as e:
			raise e

	@rtspalgprofilename.setter
	def rtspalgprofilename(self, rtspalgprofilename) :
		ur"""The name of the LSN RTSP ALG Profile.
		"""
		try :
			self._rtspalgprofilename = rtspalgprofilename
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		ur"""Name for the LSN group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN group is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn group1" or 'lsn group1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""Name for the LSN group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN group is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn group1" or 'lsn group1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsngroup_lsnrtspalgprofile_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsngroup_lsnrtspalgprofile_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.groupname is not None :
				return str(self.groupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = lsngroup_lsnrtspalgprofile_binding()
				updateresource.groupname = resource.groupname
				updateresource.rtspalgprofilename = resource.rtspalgprofilename
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lsngroup_lsnrtspalgprofile_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].groupname = resource[i].groupname
						updateresources[i].rtspalgprofilename = resource[i].rtspalgprofilename
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = lsngroup_lsnrtspalgprofile_binding()
				deleteresource.groupname = resource.groupname
				deleteresource.rtspalgprofilename = resource.rtspalgprofilename
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lsngroup_lsnrtspalgprofile_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].groupname = resource[i].groupname
						deleteresources[i].rtspalgprofilename = resource[i].rtspalgprofilename
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, groupname) :
		ur""" Use this API to fetch lsngroup_lsnrtspalgprofile_binding resources.
		"""
		try :
			obj = lsngroup_lsnrtspalgprofile_binding()
			obj.groupname = groupname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, groupname, filter_) :
		ur""" Use this API to fetch filtered set of lsngroup_lsnrtspalgprofile_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsngroup_lsnrtspalgprofile_binding()
			obj.groupname = groupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, groupname) :
		ur""" Use this API to count lsngroup_lsnrtspalgprofile_binding resources configued on NetScaler.
		"""
		try :
			obj = lsngroup_lsnrtspalgprofile_binding()
			obj.groupname = groupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, groupname, filter_) :
		ur""" Use this API to count the filtered set of lsngroup_lsnrtspalgprofile_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsngroup_lsnrtspalgprofile_binding()
			obj.groupname = groupname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class lsngroup_lsnrtspalgprofile_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsngroup_lsnrtspalgprofile_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsngroup_lsnrtspalgprofile_binding = [lsngroup_lsnrtspalgprofile_binding() for _ in range(length)]

