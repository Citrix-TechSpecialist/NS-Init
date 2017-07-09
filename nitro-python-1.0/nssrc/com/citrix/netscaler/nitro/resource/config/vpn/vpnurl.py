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

class vpnurl(base_resource) :
	""" Configuration for VPN URL resource. """
	def __init__(self) :
		self._urlname = ""
		self._linkname = ""
		self._actualurl = ""
		self._vservername = ""
		self._clientlessaccess = ""
		self._comment = ""
		self._iconurl = ""
		self._ssotype = ""
		self._applicationtype = ""
		self._samlssoprofile = ""
		self.___count = 0

	@property
	def urlname(self) :
		ur"""Name of the bookmark link.<br/>Minimum length =  1.
		"""
		try :
			return self._urlname
		except Exception as e:
			raise e

	@urlname.setter
	def urlname(self, urlname) :
		ur"""Name of the bookmark link.<br/>Minimum length =  1
		"""
		try :
			self._urlname = urlname
		except Exception as e:
			raise e

	@property
	def linkname(self) :
		ur"""Description of the bookmark link. The description appears in the Access Interface.<br/>Minimum length =  1.
		"""
		try :
			return self._linkname
		except Exception as e:
			raise e

	@linkname.setter
	def linkname(self, linkname) :
		ur"""Description of the bookmark link. The description appears in the Access Interface.<br/>Minimum length =  1
		"""
		try :
			self._linkname = linkname
		except Exception as e:
			raise e

	@property
	def actualurl(self) :
		ur"""Web address for the bookmark link.<br/>Minimum length =  1.
		"""
		try :
			return self._actualurl
		except Exception as e:
			raise e

	@actualurl.setter
	def actualurl(self, actualurl) :
		ur"""Web address for the bookmark link.<br/>Minimum length =  1
		"""
		try :
			self._actualurl = actualurl
		except Exception as e:
			raise e

	@property
	def vservername(self) :
		ur"""Name of the associated LB/CS vserver.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		ur"""Name of the associated LB/CS vserver.
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	@property
	def clientlessaccess(self) :
		ur"""If clientless access to the resource hosting the link is allowed, also use clientless access for the bookmarked web address in the Secure Client Access based session. Allows single sign-on and other HTTP processing on NetScaler Gateway for HTTPS resources.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._clientlessaccess
		except Exception as e:
			raise e

	@clientlessaccess.setter
	def clientlessaccess(self, clientlessaccess) :
		ur"""If clientless access to the resource hosting the link is allowed, also use clientless access for the bookmarked web address in the Secure Client Access based session. Allows single sign-on and other HTTP processing on NetScaler Gateway for HTTPS resources.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._clientlessaccess = clientlessaccess
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments associated with the bookmark link.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments associated with the bookmark link.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def iconurl(self) :
		ur"""URL to fetch icon file for displaying this resource.
		"""
		try :
			return self._iconurl
		except Exception as e:
			raise e

	@iconurl.setter
	def iconurl(self, iconurl) :
		ur"""URL to fetch icon file for displaying this resource.
		"""
		try :
			self._iconurl = iconurl
		except Exception as e:
			raise e

	@property
	def ssotype(self) :
		ur"""Single sign on type for unified gateway.<br/>Possible values = unifiedgateway, selfauth, samlauth.
		"""
		try :
			return self._ssotype
		except Exception as e:
			raise e

	@ssotype.setter
	def ssotype(self, ssotype) :
		ur"""Single sign on type for unified gateway.<br/>Possible values = unifiedgateway, selfauth, samlauth
		"""
		try :
			self._ssotype = ssotype
		except Exception as e:
			raise e

	@property
	def applicationtype(self) :
		ur"""The type of application this VPN URL represents. Possible values are CVPN/SaaS/VPN.<br/>Possible values = CVPN, VPN, SaaS.
		"""
		try :
			return self._applicationtype
		except Exception as e:
			raise e

	@applicationtype.setter
	def applicationtype(self, applicationtype) :
		ur"""The type of application this VPN URL represents. Possible values are CVPN/SaaS/VPN.<br/>Possible values = CVPN, VPN, SaaS
		"""
		try :
			self._applicationtype = applicationtype
		except Exception as e:
			raise e

	@property
	def samlssoprofile(self) :
		ur"""Profile to be used for doing SAML SSO.
		"""
		try :
			return self._samlssoprofile
		except Exception as e:
			raise e

	@samlssoprofile.setter
	def samlssoprofile(self, samlssoprofile) :
		ur"""Profile to be used for doing SAML SSO.
		"""
		try :
			self._samlssoprofile = samlssoprofile
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnurl_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnurl
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.urlname is not None :
				return str(self.urlname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add vpnurl.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnurl()
				addresource.urlname = resource.urlname
				addresource.linkname = resource.linkname
				addresource.actualurl = resource.actualurl
				addresource.vservername = resource.vservername
				addresource.clientlessaccess = resource.clientlessaccess
				addresource.comment = resource.comment
				addresource.iconurl = resource.iconurl
				addresource.ssotype = resource.ssotype
				addresource.applicationtype = resource.applicationtype
				addresource.samlssoprofile = resource.samlssoprofile
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnurl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].urlname = resource[i].urlname
						addresources[i].linkname = resource[i].linkname
						addresources[i].actualurl = resource[i].actualurl
						addresources[i].vservername = resource[i].vservername
						addresources[i].clientlessaccess = resource[i].clientlessaccess
						addresources[i].comment = resource[i].comment
						addresources[i].iconurl = resource[i].iconurl
						addresources[i].ssotype = resource[i].ssotype
						addresources[i].applicationtype = resource[i].applicationtype
						addresources[i].samlssoprofile = resource[i].samlssoprofile
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete vpnurl.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnurl()
				if type(resource) !=  type(deleteresource):
					deleteresource.urlname = resource
				else :
					deleteresource.urlname = resource.urlname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnurl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].urlname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnurl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].urlname = resource[i].urlname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update vpnurl.
		"""
		try :
			if type(resource) is not list :
				updateresource = vpnurl()
				updateresource.urlname = resource.urlname
				updateresource.linkname = resource.linkname
				updateresource.actualurl = resource.actualurl
				updateresource.vservername = resource.vservername
				updateresource.clientlessaccess = resource.clientlessaccess
				updateresource.comment = resource.comment
				updateresource.iconurl = resource.iconurl
				updateresource.ssotype = resource.ssotype
				updateresource.applicationtype = resource.applicationtype
				updateresource.samlssoprofile = resource.samlssoprofile
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpnurl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].urlname = resource[i].urlname
						updateresources[i].linkname = resource[i].linkname
						updateresources[i].actualurl = resource[i].actualurl
						updateresources[i].vservername = resource[i].vservername
						updateresources[i].clientlessaccess = resource[i].clientlessaccess
						updateresources[i].comment = resource[i].comment
						updateresources[i].iconurl = resource[i].iconurl
						updateresources[i].ssotype = resource[i].ssotype
						updateresources[i].applicationtype = resource[i].applicationtype
						updateresources[i].samlssoprofile = resource[i].samlssoprofile
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of vpnurl resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpnurl()
				if type(resource) !=  type(unsetresource):
					unsetresource.urlname = resource
				else :
					unsetresource.urlname = resource.urlname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnurl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].urlname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnurl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].urlname = resource[i].urlname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the vpnurl resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnurl()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = vpnurl()
						obj.urlname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [vpnurl() for _ in range(len(name))]
							obj = [vpnurl() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = vpnurl()
								obj[i].urlname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of vpnurl resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnurl()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the vpnurl resources configured on NetScaler.
		"""
		try :
			obj = vpnurl()
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
		ur""" Use this API to count filtered the set of vpnurl resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnurl()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Applicationtype:
		CVPN = "CVPN"
		VPN = "VPN"
		SaaS = "SaaS"

	class Clientlessaccess:
		ON = "ON"
		OFF = "OFF"

	class Ssotype:
		unifiedgateway = "unifiedgateway"
		selfauth = "selfauth"
		samlauth = "samlauth"

class vpnurl_response(base_response) :
	def __init__(self, length=1) :
		self.vpnurl = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnurl = [vpnurl() for _ in range(length)]

