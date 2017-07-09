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

class lsnhttphdrlogprofile(base_resource) :
	""" Configuration for LSN HTTP header logging Profile resource. """
	def __init__(self) :
		self._httphdrlogprofilename = ""
		self._logurl = ""
		self._logmethod = ""
		self._logversion = ""
		self._loghost = ""
		self.___count = 0

	@property
	def httphdrlogprofilename(self) :
		ur"""The name of the HTTP header logging Profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._httphdrlogprofilename
		except Exception as e:
			raise e

	@httphdrlogprofilename.setter
	def httphdrlogprofilename(self, httphdrlogprofilename) :
		ur"""The name of the HTTP header logging Profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._httphdrlogprofilename = httphdrlogprofilename
		except Exception as e:
			raise e

	@property
	def logurl(self) :
		ur"""URL information is logged if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logurl
		except Exception as e:
			raise e

	@logurl.setter
	def logurl(self, logurl) :
		ur"""URL information is logged if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logurl = logurl
		except Exception as e:
			raise e

	@property
	def logmethod(self) :
		ur"""HTTP method information is logged if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logmethod
		except Exception as e:
			raise e

	@logmethod.setter
	def logmethod(self, logmethod) :
		ur"""HTTP method information is logged if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logmethod = logmethod
		except Exception as e:
			raise e

	@property
	def logversion(self) :
		ur"""Version information is logged if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logversion
		except Exception as e:
			raise e

	@logversion.setter
	def logversion(self, logversion) :
		ur"""Version information is logged if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logversion = logversion
		except Exception as e:
			raise e

	@property
	def loghost(self) :
		ur"""Host information is logged if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._loghost
		except Exception as e:
			raise e

	@loghost.setter
	def loghost(self, loghost) :
		ur"""Host information is logged if option is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._loghost = loghost
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnhttphdrlogprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnhttphdrlogprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.httphdrlogprofilename is not None :
				return str(self.httphdrlogprofilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add lsnhttphdrlogprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = lsnhttphdrlogprofile()
				addresource.httphdrlogprofilename = resource.httphdrlogprofilename
				addresource.logurl = resource.logurl
				addresource.logmethod = resource.logmethod
				addresource.logversion = resource.logversion
				addresource.loghost = resource.loghost
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsnhttphdrlogprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].httphdrlogprofilename = resource[i].httphdrlogprofilename
						addresources[i].logurl = resource[i].logurl
						addresources[i].logmethod = resource[i].logmethod
						addresources[i].logversion = resource[i].logversion
						addresources[i].loghost = resource[i].loghost
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lsnhttphdrlogprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsnhttphdrlogprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.httphdrlogprofilename = resource
				else :
					deleteresource.httphdrlogprofilename = resource.httphdrlogprofilename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnhttphdrlogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].httphdrlogprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnhttphdrlogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].httphdrlogprofilename = resource[i].httphdrlogprofilename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update lsnhttphdrlogprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = lsnhttphdrlogprofile()
				updateresource.httphdrlogprofilename = resource.httphdrlogprofilename
				updateresource.logurl = resource.logurl
				updateresource.logmethod = resource.logmethod
				updateresource.logversion = resource.logversion
				updateresource.loghost = resource.loghost
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lsnhttphdrlogprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].httphdrlogprofilename = resource[i].httphdrlogprofilename
						updateresources[i].logurl = resource[i].logurl
						updateresources[i].logmethod = resource[i].logmethod
						updateresources[i].logversion = resource[i].logversion
						updateresources[i].loghost = resource[i].loghost
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lsnhttphdrlogprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lsnhttphdrlogprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.httphdrlogprofilename = resource
				else :
					unsetresource.httphdrlogprofilename = resource.httphdrlogprofilename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnhttphdrlogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].httphdrlogprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnhttphdrlogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].httphdrlogprofilename = resource[i].httphdrlogprofilename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lsnhttphdrlogprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnhttphdrlogprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lsnhttphdrlogprofile()
						obj.httphdrlogprofilename = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lsnhttphdrlogprofile() for _ in range(len(name))]
							obj = [lsnhttphdrlogprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lsnhttphdrlogprofile()
								obj[i].httphdrlogprofilename = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lsnhttphdrlogprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnhttphdrlogprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lsnhttphdrlogprofile resources configured on NetScaler.
		"""
		try :
			obj = lsnhttphdrlogprofile()
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
		ur""" Use this API to count filtered the set of lsnhttphdrlogprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnhttphdrlogprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Logversion:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logmethod:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logurl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Loghost:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lsnhttphdrlogprofile_response(base_response) :
	def __init__(self, length=1) :
		self.lsnhttphdrlogprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnhttphdrlogprofile = [lsnhttphdrlogprofile() for _ in range(length)]

