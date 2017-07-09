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

class wfpackage(base_resource) :
	""" Configuration for Web Front resource. """
	def __init__(self) :
		self._jre = ""
		self._wf = ""

	@property
	def jre(self) :
		ur"""Complete path to the JRE tar file. 
		You can use OpenJDK7 package for FreeBSD 8.x/amd64.The Java package can be downloaded from http://ftp.freebsd.org/pub/FreeBSD/releases/amd64/amd64/8.4-RELEASE/packages/java/openjdk-7.17.02_2.tbz or http://www.freebsdfoundation.org/cgi-bin/download?download=diablo-jdk-freebsd6.amd64.1.7.17.07.02.tbz.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._jre
		except Exception as e:
			raise e

	@jre.setter
	def jre(self, jre) :
		ur"""Complete path to the JRE tar file. 
		You can use OpenJDK7 package for FreeBSD 8.x/amd64.The Java package can be downloaded from http://ftp.freebsd.org/pub/FreeBSD/releases/amd64/amd64/8.4-RELEASE/packages/java/openjdk-7.17.02_2.tbz or http://www.freebsdfoundation.org/cgi-bin/download?download=diablo-jdk-freebsd6.amd64.1.7.17.07.02.tbz.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._jre = jre
		except Exception as e:
			raise e

	@property
	def wf(self) :
		ur"""Complete path to the WebFront tar file for installing the WebFront on the NetScaler appliance. This file includes Apache Tomcat Web server. The file name has the following format: nswf-<version number>.tar (for example, nswf-1.5.tar).<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._wf
		except Exception as e:
			raise e

	@wf.setter
	def wf(self, wf) :
		ur"""Complete path to the WebFront tar file for installing the WebFront on the NetScaler appliance. This file includes Apache Tomcat Web server. The file name has the following format: nswf-<version number>.tar (for example, nswf-1.5.tar).<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._wf = wf
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wfpackage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wfpackage
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def Install(cls, client, resource) :
		ur""" Use this API to Install wfpackage.
		"""
		try :
			if type(resource) is not list :
				Installresource = wfpackage()
				Installresource.jre = resource.jre
				Installresource.wf = resource.wf
				return Installresource.perform_operation(client,"Install")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the wfpackage resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = wfpackage()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class wfpackage_response(base_response) :
	def __init__(self, length=1) :
		self.wfpackage = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wfpackage = [wfpackage() for _ in range(length)]

