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

class lsnclient_nsacl6_binding(base_resource) :
	""" Binding class showing the nsacl6 that can be bound to lsnclient.
	"""
	def __init__(self) :
		self._acl6name = ""
		self._clientname = ""
		self._td = 0
		self.___count = 0

	@property
	def clientname(self) :
		ur"""Name for the LSN client entity. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN client is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn client1" or 'lsn client1'). .<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._clientname
		except Exception as e:
			raise e

	@clientname.setter
	def clientname(self, clientname) :
		ur"""Name for the LSN client entity. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN client is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn client1" or 'lsn client1'). .<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._clientname = clientname
		except Exception as e:
			raise e

	@property
	def acl6name(self) :
		ur"""Name of any configured extended ACL6 whose action is ALLOW. The condition specified in the extended ACL6 rule is used as the condition for the LSN client.<br/>Minimum length =  1.
		"""
		try :
			return self._acl6name
		except Exception as e:
			raise e

	@acl6name.setter
	def acl6name(self, acl6name) :
		ur"""Name of any configured extended ACL6 whose action is ALLOW. The condition specified in the extended ACL6 rule is used as the condition for the LSN client.<br/>Minimum length =  1
		"""
		try :
			self._acl6name = acl6name
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""ID of the traffic domain on which this subscriber or the subscriber network (as specified by the network parameter) belongs. 
		If you do not specify an ID, the subscriber or the subscriber network becomes part of the default traffic domain.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""ID of the traffic domain on which this subscriber or the subscriber network (as specified by the network parameter) belongs. 
		If you do not specify an ID, the subscriber or the subscriber network becomes part of the default traffic domain.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnclient_nsacl6_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnclient_nsacl6_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.clientname is not None :
				return str(self.clientname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = lsnclient_nsacl6_binding()
				updateresource.clientname = resource.clientname
				updateresource.acl6name = resource.acl6name
				updateresource.td = resource.td
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lsnclient_nsacl6_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].clientname = resource[i].clientname
						updateresources[i].acl6name = resource[i].acl6name
						updateresources[i].td = resource[i].td
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = lsnclient_nsacl6_binding()
				deleteresource.clientname = resource.clientname
				deleteresource.acl6name = resource.acl6name
				deleteresource.td = resource.td
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lsnclient_nsacl6_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].clientname = resource[i].clientname
						deleteresources[i].acl6name = resource[i].acl6name
						deleteresources[i].td = resource[i].td
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, clientname) :
		ur""" Use this API to fetch lsnclient_nsacl6_binding resources.
		"""
		try :
			obj = lsnclient_nsacl6_binding()
			obj.clientname = clientname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, clientname, filter_) :
		ur""" Use this API to fetch filtered set of lsnclient_nsacl6_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnclient_nsacl6_binding()
			obj.clientname = clientname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, clientname) :
		ur""" Use this API to count lsnclient_nsacl6_binding resources configued on NetScaler.
		"""
		try :
			obj = lsnclient_nsacl6_binding()
			obj.clientname = clientname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, clientname, filter_) :
		ur""" Use this API to count the filtered set of lsnclient_nsacl6_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnclient_nsacl6_binding()
			obj.clientname = clientname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class lsnclient_nsacl6_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsnclient_nsacl6_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnclient_nsacl6_binding = [lsnclient_nsacl6_binding() for _ in range(length)]

