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

class wfsite(base_resource) :
	""" Configuration for WF site resource. """
	def __init__(self) :
		self._sitename = ""
		self._storefronturl = ""
		self._storename = ""
		self._html5receiver = ""
		self._workspacecontrol = ""
		self._displayroamingaccounts = ""
		self._xframeoptions = ""
		self._state = ""
		self.___count = 0

	@property
	def sitename(self) :
		ur"""Name of the WebFront site being created on the NetScaler appliance.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@sitename.setter
	def sitename(self, sitename) :
		ur"""Name of the WebFront site being created on the NetScaler appliance.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._sitename = sitename
		except Exception as e:
			raise e

	@property
	def storefronturl(self) :
		ur"""FQDN or IP of Windows StoreFront server where the store is configured.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._storefronturl
		except Exception as e:
			raise e

	@storefronturl.setter
	def storefronturl(self, storefronturl) :
		ur"""FQDN or IP of Windows StoreFront server where the store is configured.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._storefronturl = storefronturl
		except Exception as e:
			raise e

	@property
	def storename(self) :
		ur"""Name of the store present in StoreFront.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._storename
		except Exception as e:
			raise e

	@storename.setter
	def storename(self, storename) :
		ur"""Name of the store present in StoreFront.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._storename = storename
		except Exception as e:
			raise e

	@property
	def html5receiver(self) :
		ur"""Specifies whether or not to use HTML5 receiver for launching apps for the WF site.<br/>Default value: FALLBACK<br/>Possible values = ALWAYS, FALLBACK, OFF.
		"""
		try :
			return self._html5receiver
		except Exception as e:
			raise e

	@html5receiver.setter
	def html5receiver(self, html5receiver) :
		ur"""Specifies whether or not to use HTML5 receiver for launching apps for the WF site.<br/>Default value: FALLBACK<br/>Possible values = ALWAYS, FALLBACK, OFF
		"""
		try :
			self._html5receiver = html5receiver
		except Exception as e:
			raise e

	@property
	def workspacecontrol(self) :
		ur"""Specifies whether of not to use workspace control for the WF site.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._workspacecontrol
		except Exception as e:
			raise e

	@workspacecontrol.setter
	def workspacecontrol(self, workspacecontrol) :
		ur"""Specifies whether of not to use workspace control for the WF site.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._workspacecontrol = workspacecontrol
		except Exception as e:
			raise e

	@property
	def displayroamingaccounts(self) :
		ur"""Specifies whether or not to display the accounts selection screen during First Time Use of Receiver .<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._displayroamingaccounts
		except Exception as e:
			raise e

	@displayroamingaccounts.setter
	def displayroamingaccounts(self, displayroamingaccounts) :
		ur"""Specifies whether or not to display the accounts selection screen during First Time Use of Receiver .<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._displayroamingaccounts = displayroamingaccounts
		except Exception as e:
			raise e

	@property
	def xframeoptions(self) :
		ur"""The value to be sent in the X-Frame-Options header. WARNING: Setting this option to ALLOW could leave the end user vulnerable to Click Jacking attacks.<br/>Default value: DENY<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._xframeoptions
		except Exception as e:
			raise e

	@xframeoptions.setter
	def xframeoptions(self, xframeoptions) :
		ur"""The value to be sent in the X-Frame-Options header. WARNING: Setting this option to ALLOW could leave the end user vulnerable to Click Jacking attacks.<br/>Default value: DENY<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._xframeoptions = xframeoptions
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""State of wf site.<br/>Default value: UP<br/>Possible values = UP, INITIALIZING, DOWN-HostUnknown, DOWN-ReqTimeout, DOWN-Wrong Store, DOWN-SF Error, DOWN-SSL Error, DOWN-Conn Reset, DOWN.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wfsite_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wfsite
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sitename is not None :
				return str(self.sitename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add wfsite.
		"""
		try :
			if type(resource) is not list :
				addresource = wfsite()
				addresource.sitename = resource.sitename
				addresource.storefronturl = resource.storefronturl
				addresource.storename = resource.storename
				addresource.html5receiver = resource.html5receiver
				addresource.workspacecontrol = resource.workspacecontrol
				addresource.displayroamingaccounts = resource.displayroamingaccounts
				addresource.xframeoptions = resource.xframeoptions
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ wfsite() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].sitename = resource[i].sitename
						addresources[i].storefronturl = resource[i].storefronturl
						addresources[i].storename = resource[i].storename
						addresources[i].html5receiver = resource[i].html5receiver
						addresources[i].workspacecontrol = resource[i].workspacecontrol
						addresources[i].displayroamingaccounts = resource[i].displayroamingaccounts
						addresources[i].xframeoptions = resource[i].xframeoptions
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete wfsite.
		"""
		try :
			if type(resource) is not list :
				deleteresource = wfsite()
				if type(resource) !=  type(deleteresource):
					deleteresource.sitename = resource
				else :
					deleteresource.sitename = resource.sitename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ wfsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sitename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ wfsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sitename = resource[i].sitename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update wfsite.
		"""
		try :
			if type(resource) is not list :
				updateresource = wfsite()
				updateresource.sitename = resource.sitename
				updateresource.storefronturl = resource.storefronturl
				updateresource.storename = resource.storename
				updateresource.html5receiver = resource.html5receiver
				updateresource.workspacecontrol = resource.workspacecontrol
				updateresource.displayroamingaccounts = resource.displayroamingaccounts
				updateresource.xframeoptions = resource.xframeoptions
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ wfsite() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].sitename = resource[i].sitename
						updateresources[i].storefronturl = resource[i].storefronturl
						updateresources[i].storename = resource[i].storename
						updateresources[i].html5receiver = resource[i].html5receiver
						updateresources[i].workspacecontrol = resource[i].workspacecontrol
						updateresources[i].displayroamingaccounts = resource[i].displayroamingaccounts
						updateresources[i].xframeoptions = resource[i].xframeoptions
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the wfsite resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = wfsite()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = wfsite()
						obj.sitename = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [wfsite() for _ in range(len(name))]
							obj = [wfsite() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = wfsite()
								obj[i].sitename = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of wfsite resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wfsite()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the wfsite resources configured on NetScaler.
		"""
		try :
			obj = wfsite()
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
		ur""" Use this API to count filtered the set of wfsite resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wfsite()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Displayroamingaccounts:
		ON = "ON"
		OFF = "OFF"

	class Xframeoptions:
		ALLOW = "ALLOW"
		DENY = "DENY"

	class State:
		UP = "UP"
		INITIALIZING = "INITIALIZING"
		DOWN_HostUnknown = "DOWN-HostUnknown"
		DOWN_ReqTimeout = "DOWN-ReqTimeout"
		DOWN_Wrong_Store = "DOWN-Wrong Store"
		DOWN_SF_Error = "DOWN-SF Error"
		DOWN_SSL_Error = "DOWN-SSL Error"
		DOWN_Conn_Reset = "DOWN-Conn Reset"
		DOWN = "DOWN"

	class Html5receiver:
		ALWAYS = "ALWAYS"
		FALLBACK = "FALLBACK"
		OFF = "OFF"

	class Workspacecontrol:
		ON = "ON"
		OFF = "OFF"

class wfsite_response(base_response) :
	def __init__(self, length=1) :
		self.wfsite = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wfsite = [wfsite() for _ in range(length)]

