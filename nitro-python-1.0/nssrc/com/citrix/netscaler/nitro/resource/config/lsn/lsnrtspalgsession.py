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

class lsnrtspalgsession(base_resource) :
	""" Configuration for LSN RTSPALG session resource. """
	def __init__(self) :
		self._sessionid = ""
		self._callflags = 0
		self._callrefcount = 0
		self._calltimer = 0
		self.___count = 0

	@property
	def sessionid(self) :
		ur"""Session ID for the RTSP call.
		"""
		try :
			return self._sessionid
		except Exception as e:
			raise e

	@sessionid.setter
	def sessionid(self, sessionid) :
		ur"""Session ID for the RTSP call.
		"""
		try :
			self._sessionid = sessionid
		except Exception as e:
			raise e

	@property
	def callflags(self) :
		ur"""Flags for the call entry.
		"""
		try :
			return self._callflags
		except Exception as e:
			raise e

	@property
	def callrefcount(self) :
		ur"""Reference count for the call entry.
		"""
		try :
			return self._callrefcount
		except Exception as e:
			raise e

	@property
	def calltimer(self) :
		ur"""Timer for the call entry.
		"""
		try :
			return self._calltimer
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnrtspalgsession_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnrtspalgsession
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sessionid is not None :
				return str(self.sessionid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def flush(cls, client, resource) :
		ur""" Use this API to flush lsnrtspalgsession.
		"""
		try :
			if type(resource) is not list :
				flushresource = lsnrtspalgsession()
				flushresource.sessionid = resource.sessionid
				return flushresource.perform_operation(client,"flush")
			else :
				if (resource and len(resource) > 0) :
					flushresources = [ lsnrtspalgsession() for _ in range(len(resource))]
					for i in range(len(resource)) :
						flushresources[i].sessionid = resource[i].sessionid
				result = cls.perform_operation_bulk_request(client, flushresources,"flush")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lsnrtspalgsession resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnrtspalgsession()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lsnrtspalgsession()
						obj.sessionid = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lsnrtspalgsession() for _ in range(len(name))]
							obj = [lsnrtspalgsession() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lsnrtspalgsession()
								obj[i].sessionid = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lsnrtspalgsession resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnrtspalgsession()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lsnrtspalgsession resources configured on NetScaler.
		"""
		try :
			obj = lsnrtspalgsession()
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
		ur""" Use this API to count filtered the set of lsnrtspalgsession resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnrtspalgsession()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class lsnrtspalgsession_response(base_response) :
	def __init__(self, length=1) :
		self.lsnrtspalgsession = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnrtspalgsession = [lsnrtspalgsession() for _ in range(length)]

