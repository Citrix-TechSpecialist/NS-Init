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

class rdpclientprofile(base_resource) :
	""" Configuration for RDP clientprofile resource. """
	def __init__(self) :
		self._name = ""
		self._rdpurloverride = ""
		self._redirectclipboard = ""
		self._redirectdrives = ""
		self._redirectprinters = ""
		self._redirectcomports = ""
		self._redirectpnpdevices = ""
		self._keyboardhook = ""
		self._audiocapturemode = ""
		self._videoplaybackmode = ""
		self._multimonitorsupport = ""
		self._rdpcookievalidity = 0
		self._addusernameinrdpfile = ""
		self._rdpfilename = ""
		self._rdphost = ""
		self._rdpcustomparams = ""
		self._psk = ""
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""The name of the rdp profile.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The name of the rdp profile.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def rdpurloverride(self) :
		ur"""This setting determines whether the RDP parameters supplied in the vpn url override those specified in the RDP profile.<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._rdpurloverride
		except Exception as e:
			raise e

	@rdpurloverride.setter
	def rdpurloverride(self, rdpurloverride) :
		ur"""This setting determines whether the RDP parameters supplied in the vpn url override those specified in the RDP profile.<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._rdpurloverride = rdpurloverride
		except Exception as e:
			raise e

	@property
	def redirectclipboard(self) :
		ur"""This setting corresponds to the Clipboard check box on the Local Resources tab under Options in RDC.<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._redirectclipboard
		except Exception as e:
			raise e

	@redirectclipboard.setter
	def redirectclipboard(self, redirectclipboard) :
		ur"""This setting corresponds to the Clipboard check box on the Local Resources tab under Options in RDC.<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._redirectclipboard = redirectclipboard
		except Exception as e:
			raise e

	@property
	def redirectdrives(self) :
		ur"""This setting corresponds to the selections for Drives under More on the Local Resources tab under Options in RDC.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._redirectdrives
		except Exception as e:
			raise e

	@redirectdrives.setter
	def redirectdrives(self, redirectdrives) :
		ur"""This setting corresponds to the selections for Drives under More on the Local Resources tab under Options in RDC.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._redirectdrives = redirectdrives
		except Exception as e:
			raise e

	@property
	def redirectprinters(self) :
		ur"""This setting corresponds to the selection in the Printers check box on the Local Resources tab under Options in RDC.<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._redirectprinters
		except Exception as e:
			raise e

	@redirectprinters.setter
	def redirectprinters(self, redirectprinters) :
		ur"""This setting corresponds to the selection in the Printers check box on the Local Resources tab under Options in RDC.<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._redirectprinters = redirectprinters
		except Exception as e:
			raise e

	@property
	def redirectcomports(self) :
		ur"""This setting corresponds to the selections for comports under More on the Local Resources tab under Options in RDC.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._redirectcomports
		except Exception as e:
			raise e

	@redirectcomports.setter
	def redirectcomports(self, redirectcomports) :
		ur"""This setting corresponds to the selections for comports under More on the Local Resources tab under Options in RDC.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._redirectcomports = redirectcomports
		except Exception as e:
			raise e

	@property
	def redirectpnpdevices(self) :
		ur"""This setting corresponds to the selections for pnpdevices under More on the Local Resources tab under Options in RDC.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._redirectpnpdevices
		except Exception as e:
			raise e

	@redirectpnpdevices.setter
	def redirectpnpdevices(self, redirectpnpdevices) :
		ur"""This setting corresponds to the selections for pnpdevices under More on the Local Resources tab under Options in RDC.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._redirectpnpdevices = redirectpnpdevices
		except Exception as e:
			raise e

	@property
	def keyboardhook(self) :
		ur"""This setting corresponds to the selection in the Keyboard drop-down list on the Local Resources tab under Options in RDC.<br/>Default value: InFullScreenMode<br/>Possible values = OnLocal, OnRemote, InFullScreenMode.
		"""
		try :
			return self._keyboardhook
		except Exception as e:
			raise e

	@keyboardhook.setter
	def keyboardhook(self, keyboardhook) :
		ur"""This setting corresponds to the selection in the Keyboard drop-down list on the Local Resources tab under Options in RDC.<br/>Default value: InFullScreenMode<br/>Possible values = OnLocal, OnRemote, InFullScreenMode
		"""
		try :
			self._keyboardhook = keyboardhook
		except Exception as e:
			raise e

	@property
	def audiocapturemode(self) :
		ur"""This setting corresponds to the selections in the Remote audio area on the Local Resources tab under Options in RDC.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._audiocapturemode
		except Exception as e:
			raise e

	@audiocapturemode.setter
	def audiocapturemode(self, audiocapturemode) :
		ur"""This setting corresponds to the selections in the Remote audio area on the Local Resources tab under Options in RDC.<br/>Default value: DISABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._audiocapturemode = audiocapturemode
		except Exception as e:
			raise e

	@property
	def videoplaybackmode(self) :
		ur"""This setting determines if Remote Desktop Connection (RDC) will use RDP efficient multimedia streaming for video playback.<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._videoplaybackmode
		except Exception as e:
			raise e

	@videoplaybackmode.setter
	def videoplaybackmode(self, videoplaybackmode) :
		ur"""This setting determines if Remote Desktop Connection (RDC) will use RDP efficient multimedia streaming for video playback.<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._videoplaybackmode = videoplaybackmode
		except Exception as e:
			raise e

	@property
	def multimonitorsupport(self) :
		ur"""Enable/Disable Multiple Monitor Support for Remote Desktop Connection (RDC).<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE.
		"""
		try :
			return self._multimonitorsupport
		except Exception as e:
			raise e

	@multimonitorsupport.setter
	def multimonitorsupport(self, multimonitorsupport) :
		ur"""Enable/Disable Multiple Monitor Support for Remote Desktop Connection (RDC).<br/>Default value: ENABLE<br/>Possible values = ENABLE, DISABLE
		"""
		try :
			self._multimonitorsupport = multimonitorsupport
		except Exception as e:
			raise e

	@property
	def rdpcookievalidity(self) :
		ur"""RDP cookie validity period.<br/>Default value: 60<br/>Minimum length =  60<br/>Maximum length =  86400.
		"""
		try :
			return self._rdpcookievalidity
		except Exception as e:
			raise e

	@rdpcookievalidity.setter
	def rdpcookievalidity(self, rdpcookievalidity) :
		ur"""RDP cookie validity period.<br/>Default value: 60<br/>Minimum length =  60<br/>Maximum length =  86400
		"""
		try :
			self._rdpcookievalidity = rdpcookievalidity
		except Exception as e:
			raise e

	@property
	def addusernameinrdpfile(self) :
		ur"""Add username in rdp file.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._addusernameinrdpfile
		except Exception as e:
			raise e

	@addusernameinrdpfile.setter
	def addusernameinrdpfile(self, addusernameinrdpfile) :
		ur"""Add username in rdp file.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._addusernameinrdpfile = addusernameinrdpfile
		except Exception as e:
			raise e

	@property
	def rdpfilename(self) :
		ur"""RDP file name to be sent to End User.<br/>Minimum length =  1.
		"""
		try :
			return self._rdpfilename
		except Exception as e:
			raise e

	@rdpfilename.setter
	def rdpfilename(self, rdpfilename) :
		ur"""RDP file name to be sent to End User.<br/>Minimum length =  1
		"""
		try :
			self._rdpfilename = rdpfilename
		except Exception as e:
			raise e

	@property
	def rdphost(self) :
		ur"""Fully-qualified domain name (FQDN) of the RDP Listener.<br/>Maximum length =  252.
		"""
		try :
			return self._rdphost
		except Exception as e:
			raise e

	@rdphost.setter
	def rdphost(self, rdphost) :
		ur"""Fully-qualified domain name (FQDN) of the RDP Listener.<br/>Maximum length =  252
		"""
		try :
			self._rdphost = rdphost
		except Exception as e:
			raise e

	@property
	def rdpcustomparams(self) :
		ur"""Option for RDP custom parameters settings (if any). Custom params needs to be separated by '&'.<br/>Default value: 0<br/>Minimum length =  1.
		"""
		try :
			return self._rdpcustomparams
		except Exception as e:
			raise e

	@rdpcustomparams.setter
	def rdpcustomparams(self, rdpcustomparams) :
		ur"""Option for RDP custom parameters settings (if any). Custom params needs to be separated by '&'.<br/>Default value: 0<br/>Minimum length =  1
		"""
		try :
			self._rdpcustomparams = rdpcustomparams
		except Exception as e:
			raise e

	@property
	def psk(self) :
		ur"""Pre shared key value.<br/>Default value: 0.
		"""
		try :
			return self._psk
		except Exception as e:
			raise e

	@psk.setter
	def psk(self, psk) :
		ur"""Pre shared key value.<br/>Default value: 0
		"""
		try :
			self._psk = psk
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rdpclientprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rdpclientprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add rdpclientprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = rdpclientprofile()
				addresource.name = resource.name
				addresource.rdpurloverride = resource.rdpurloverride
				addresource.redirectclipboard = resource.redirectclipboard
				addresource.redirectdrives = resource.redirectdrives
				addresource.redirectprinters = resource.redirectprinters
				addresource.redirectcomports = resource.redirectcomports
				addresource.redirectpnpdevices = resource.redirectpnpdevices
				addresource.keyboardhook = resource.keyboardhook
				addresource.audiocapturemode = resource.audiocapturemode
				addresource.videoplaybackmode = resource.videoplaybackmode
				addresource.multimonitorsupport = resource.multimonitorsupport
				addresource.rdpcookievalidity = resource.rdpcookievalidity
				addresource.addusernameinrdpfile = resource.addusernameinrdpfile
				addresource.rdpfilename = resource.rdpfilename
				addresource.rdphost = resource.rdphost
				addresource.rdpcustomparams = resource.rdpcustomparams
				addresource.psk = resource.psk
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ rdpclientprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].rdpurloverride = resource[i].rdpurloverride
						addresources[i].redirectclipboard = resource[i].redirectclipboard
						addresources[i].redirectdrives = resource[i].redirectdrives
						addresources[i].redirectprinters = resource[i].redirectprinters
						addresources[i].redirectcomports = resource[i].redirectcomports
						addresources[i].redirectpnpdevices = resource[i].redirectpnpdevices
						addresources[i].keyboardhook = resource[i].keyboardhook
						addresources[i].audiocapturemode = resource[i].audiocapturemode
						addresources[i].videoplaybackmode = resource[i].videoplaybackmode
						addresources[i].multimonitorsupport = resource[i].multimonitorsupport
						addresources[i].rdpcookievalidity = resource[i].rdpcookievalidity
						addresources[i].addusernameinrdpfile = resource[i].addusernameinrdpfile
						addresources[i].rdpfilename = resource[i].rdpfilename
						addresources[i].rdphost = resource[i].rdphost
						addresources[i].rdpcustomparams = resource[i].rdpcustomparams
						addresources[i].psk = resource[i].psk
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update rdpclientprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = rdpclientprofile()
				updateresource.name = resource.name
				updateresource.rdpurloverride = resource.rdpurloverride
				updateresource.redirectclipboard = resource.redirectclipboard
				updateresource.redirectdrives = resource.redirectdrives
				updateresource.redirectprinters = resource.redirectprinters
				updateresource.redirectcomports = resource.redirectcomports
				updateresource.redirectpnpdevices = resource.redirectpnpdevices
				updateresource.keyboardhook = resource.keyboardhook
				updateresource.audiocapturemode = resource.audiocapturemode
				updateresource.videoplaybackmode = resource.videoplaybackmode
				updateresource.multimonitorsupport = resource.multimonitorsupport
				updateresource.rdpcookievalidity = resource.rdpcookievalidity
				updateresource.addusernameinrdpfile = resource.addusernameinrdpfile
				updateresource.rdpfilename = resource.rdpfilename
				updateresource.rdphost = resource.rdphost
				updateresource.rdpcustomparams = resource.rdpcustomparams
				updateresource.psk = resource.psk
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ rdpclientprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].rdpurloverride = resource[i].rdpurloverride
						updateresources[i].redirectclipboard = resource[i].redirectclipboard
						updateresources[i].redirectdrives = resource[i].redirectdrives
						updateresources[i].redirectprinters = resource[i].redirectprinters
						updateresources[i].redirectcomports = resource[i].redirectcomports
						updateresources[i].redirectpnpdevices = resource[i].redirectpnpdevices
						updateresources[i].keyboardhook = resource[i].keyboardhook
						updateresources[i].audiocapturemode = resource[i].audiocapturemode
						updateresources[i].videoplaybackmode = resource[i].videoplaybackmode
						updateresources[i].multimonitorsupport = resource[i].multimonitorsupport
						updateresources[i].rdpcookievalidity = resource[i].rdpcookievalidity
						updateresources[i].addusernameinrdpfile = resource[i].addusernameinrdpfile
						updateresources[i].rdpfilename = resource[i].rdpfilename
						updateresources[i].rdphost = resource[i].rdphost
						updateresources[i].rdpcustomparams = resource[i].rdpcustomparams
						updateresources[i].psk = resource[i].psk
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of rdpclientprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = rdpclientprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ rdpclientprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ rdpclientprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete rdpclientprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = rdpclientprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ rdpclientprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ rdpclientprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the rdpclientprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = rdpclientprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = rdpclientprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [rdpclientprofile() for _ in range(len(name))]
							obj = [rdpclientprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = rdpclientprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of rdpclientprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rdpclientprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the rdpclientprofile resources configured on NetScaler.
		"""
		try :
			obj = rdpclientprofile()
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
		ur""" Use this API to count filtered the set of rdpclientprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rdpclientprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Rdpurloverride:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Keyboardhook:
		OnLocal = "OnLocal"
		OnRemote = "OnRemote"
		InFullScreenMode = "InFullScreenMode"

	class Redirectcomports:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Multimonitorsupport:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Addusernameinrdpfile:
		YES = "YES"
		NO = "NO"

	class Videoplaybackmode:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Redirectclipboard:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Redirectpnpdevices:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Redirectprinters:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Audiocapturemode:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

	class Redirectdrives:
		ENABLE = "ENABLE"
		DISABLE = "DISABLE"

class rdpclientprofile_response(base_response) :
	def __init__(self, length=1) :
		self.rdpclientprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rdpclientprofile = [rdpclientprofile() for _ in range(length)]

