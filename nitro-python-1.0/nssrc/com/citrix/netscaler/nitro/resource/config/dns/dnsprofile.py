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

class dnsprofile(base_resource) :
	""" Configuration for DNS profile resource. """
	def __init__(self) :
		self._dnsprofilename = ""
		self._dnsquerylogging = ""
		self._dnsanswerseclogging = ""
		self._dnsextendedlogging = ""
		self._dnserrorlogging = ""
		self._cacherecords = ""
		self._cachenegativeresponses = ""
		self._referencecount = 0
		self.___count = 0

	@property
	def dnsprofilename(self) :
		ur"""Name of the DNS profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._dnsprofilename
		except Exception as e:
			raise e

	@dnsprofilename.setter
	def dnsprofilename(self, dnsprofilename) :
		ur"""Name of the DNS profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._dnsprofilename = dnsprofilename
		except Exception as e:
			raise e

	@property
	def dnsquerylogging(self) :
		ur"""DNS query logging; if enabled, DNS query information such as DNS query id, DNS query flags , DNS domain name and DNS query type will be logged.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnsquerylogging
		except Exception as e:
			raise e

	@dnsquerylogging.setter
	def dnsquerylogging(self, dnsquerylogging) :
		ur"""DNS query logging; if enabled, DNS query information such as DNS query id, DNS query flags , DNS domain name and DNS query type will be logged.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnsquerylogging = dnsquerylogging
		except Exception as e:
			raise e

	@property
	def dnsanswerseclogging(self) :
		ur"""DNS answer section; if enabled, answer section in the response will be logged.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnsanswerseclogging
		except Exception as e:
			raise e

	@dnsanswerseclogging.setter
	def dnsanswerseclogging(self, dnsanswerseclogging) :
		ur"""DNS answer section; if enabled, answer section in the response will be logged.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnsanswerseclogging = dnsanswerseclogging
		except Exception as e:
			raise e

	@property
	def dnsextendedlogging(self) :
		ur"""DNS extended logging; if enabled, authority and additional section in the response will be logged.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnsextendedlogging
		except Exception as e:
			raise e

	@dnsextendedlogging.setter
	def dnsextendedlogging(self, dnsextendedlogging) :
		ur"""DNS extended logging; if enabled, authority and additional section in the response will be logged.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnsextendedlogging = dnsextendedlogging
		except Exception as e:
			raise e

	@property
	def dnserrorlogging(self) :
		ur"""DNS error logging; if enabled, whenever error is encountered in DNS module reason for the error will be logged.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnserrorlogging
		except Exception as e:
			raise e

	@dnserrorlogging.setter
	def dnserrorlogging(self, dnserrorlogging) :
		ur"""DNS error logging; if enabled, whenever error is encountered in DNS module reason for the error will be logged.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnserrorlogging = dnserrorlogging
		except Exception as e:
			raise e

	@property
	def cacherecords(self) :
		ur"""Cache resource records in the DNS cache. Applies to resource records obtained through proxy configurations only. End resolver and forwarder configurations always cache records in the DNS cache, and you cannot disable this behavior. When you disable record caching, the appliance stops caching server responses. However, cached records are not flushed. The appliance does not serve requests from the cache until record caching is enabled again.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cacherecords
		except Exception as e:
			raise e

	@cacherecords.setter
	def cacherecords(self, cacherecords) :
		ur"""Cache resource records in the DNS cache. Applies to resource records obtained through proxy configurations only. End resolver and forwarder configurations always cache records in the DNS cache, and you cannot disable this behavior. When you disable record caching, the appliance stops caching server responses. However, cached records are not flushed. The appliance does not serve requests from the cache until record caching is enabled again.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cacherecords = cacherecords
		except Exception as e:
			raise e

	@property
	def cachenegativeresponses(self) :
		ur"""Cache negative responses in the DNS cache. When disabled, the appliance stops caching negative responses except referral records. This applies to all configurations - proxy, end resolver, and forwarder. However, cached responses are not flushed. The appliance does not serve negative responses from the cache until this parameter is enabled again.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cachenegativeresponses
		except Exception as e:
			raise e

	@cachenegativeresponses.setter
	def cachenegativeresponses(self, cachenegativeresponses) :
		ur"""Cache negative responses in the DNS cache. When disabled, the appliance stops caching negative responses except referral records. This applies to all configurations - proxy, end resolver, and forwarder. However, cached responses are not flushed. The appliance does not serve negative responses from the cache until this parameter is enabled again.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cachenegativeresponses = cachenegativeresponses
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		ur"""Number of entities using this profile.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.dnsprofilename is not None :
				return str(self.dnsprofilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add dnsprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = dnsprofile()
				addresource.dnsprofilename = resource.dnsprofilename
				addresource.dnsquerylogging = resource.dnsquerylogging
				addresource.dnsanswerseclogging = resource.dnsanswerseclogging
				addresource.dnsextendedlogging = resource.dnsextendedlogging
				addresource.dnserrorlogging = resource.dnserrorlogging
				addresource.cacherecords = resource.cacherecords
				addresource.cachenegativeresponses = resource.cachenegativeresponses
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnsprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].dnsprofilename = resource[i].dnsprofilename
						addresources[i].dnsquerylogging = resource[i].dnsquerylogging
						addresources[i].dnsanswerseclogging = resource[i].dnsanswerseclogging
						addresources[i].dnsextendedlogging = resource[i].dnsextendedlogging
						addresources[i].dnserrorlogging = resource[i].dnserrorlogging
						addresources[i].cacherecords = resource[i].cacherecords
						addresources[i].cachenegativeresponses = resource[i].cachenegativeresponses
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update dnsprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnsprofile()
				updateresource.dnsprofilename = resource.dnsprofilename
				updateresource.dnsquerylogging = resource.dnsquerylogging
				updateresource.dnsanswerseclogging = resource.dnsanswerseclogging
				updateresource.dnsextendedlogging = resource.dnsextendedlogging
				updateresource.dnserrorlogging = resource.dnserrorlogging
				updateresource.cacherecords = resource.cacherecords
				updateresource.cachenegativeresponses = resource.cachenegativeresponses
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnsprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].dnsprofilename = resource[i].dnsprofilename
						updateresources[i].dnsquerylogging = resource[i].dnsquerylogging
						updateresources[i].dnsanswerseclogging = resource[i].dnsanswerseclogging
						updateresources[i].dnsextendedlogging = resource[i].dnsextendedlogging
						updateresources[i].dnserrorlogging = resource[i].dnserrorlogging
						updateresources[i].cacherecords = resource[i].cacherecords
						updateresources[i].cachenegativeresponses = resource[i].cachenegativeresponses
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of dnsprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnsprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.dnsprofilename = resource
				else :
					unsetresource.dnsprofilename = resource.dnsprofilename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].dnsprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].dnsprofilename = resource[i].dnsprofilename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete dnsprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnsprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.dnsprofilename = resource
				else :
					deleteresource.dnsprofilename = resource.dnsprofilename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].dnsprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].dnsprofilename = resource[i].dnsprofilename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnsprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = dnsprofile()
						obj.dnsprofilename = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dnsprofile() for _ in range(len(name))]
							obj = [dnsprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = dnsprofile()
								obj[i].dnsprofilename = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dnsprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dnsprofile resources configured on NetScaler.
		"""
		try :
			obj = dnsprofile()
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
		ur""" Use this API to count filtered the set of dnsprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Dnsextendedlogging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cacherecords:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dnsanswerseclogging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cachenegativeresponses:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dnsquerylogging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dnserrorlogging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class dnsprofile_response(base_response) :
	def __init__(self, length=1) :
		self.dnsprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsprofile = [dnsprofile() for _ in range(length)]

