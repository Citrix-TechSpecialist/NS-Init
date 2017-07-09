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

class lsngroup_binding(base_resource):
	""" Binding class showing the resources that can be bound to lsngroup_binding. 
	"""
	def __init__(self) :
		self._groupname = ""
		self.lsngroup_lsnsipalgprofile_binding = []
		self.lsngroup_lsntransportprofile_binding = []
		self.lsngroup_lsnlogprofile_binding = []
		self.lsngroup_lsnhttphdrlogprofile_binding = []
		self.lsngroup_lsnpool_binding = []
		self.lsngroup_lsnrtspalgprofile_binding = []
		self.lsngroup_lsnappsprofile_binding = []

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

	@property
	def lsngroup_lsnhttphdrlogprofile_bindings(self) :
		ur"""lsnhttphdrlogprofile that can be bound to lsngroup.
		"""
		try :
			return self._lsngroup_lsnhttphdrlogprofile_binding
		except Exception as e:
			raise e

	@property
	def lsngroup_lsnrtspalgprofile_bindings(self) :
		ur"""lsnrtspalgprofile that can be bound to lsngroup.
		"""
		try :
			return self._lsngroup_lsnrtspalgprofile_binding
		except Exception as e:
			raise e

	@property
	def lsngroup_lsnsipalgprofile_bindings(self) :
		ur"""lsnsipalgprofile that can be bound to lsngroup.
		"""
		try :
			return self._lsngroup_lsnsipalgprofile_binding
		except Exception as e:
			raise e

	@property
	def lsngroup_lsnlogprofile_bindings(self) :
		ur"""lsnlogprofile that can be bound to lsngroup.
		"""
		try :
			return self._lsngroup_lsnlogprofile_binding
		except Exception as e:
			raise e

	@property
	def lsngroup_lsnappsprofile_bindings(self) :
		ur"""lsnappsprofile that can be bound to lsngroup.
		"""
		try :
			return self._lsngroup_lsnappsprofile_binding
		except Exception as e:
			raise e

	@property
	def lsngroup_lsnpool_bindings(self) :
		ur"""lsnpool that can be bound to lsngroup.
		"""
		try :
			return self._lsngroup_lsnpool_binding
		except Exception as e:
			raise e

	@property
	def lsngroup_lsntransportprofile_bindings(self) :
		ur"""lsntransportprofile that can be bound to lsngroup.
		"""
		try :
			return self._lsngroup_lsntransportprofile_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsngroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsngroup_binding
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
	def get(self, service, groupname) :
		ur""" Use this API to fetch lsngroup_binding resource.
		"""
		try :
			if type(groupname) is not list :
				obj = lsngroup_binding()
				obj.groupname = groupname
				response = obj.get_resource(service)
			else :
				if groupname and len(groupname) > 0 :
					obj = [lsngroup_binding() for _ in range(len(groupname))]
					for i in range(len(groupname)) :
						obj[i].groupname = groupname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class lsngroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsngroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsngroup_binding = [lsngroup_binding() for _ in range(length)]

