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

class nsextension_extensionfunction_binding(base_resource) :
	""" Binding class showing the extensionfunction that can be bound to nsextension.
	"""
	def __init__(self) :
		self._extensionfunctionname = ""
		self._extensionfunctionlinenumber = 0
		self._extensionfunctionclasstype = ""
		self._extensionfunctionreturntype = ""
		self._activeextensionfunction = 0
		self._extensionfunctionargtype = []
		self._extensionfuncdescription = ""
		self._extensionfunctionargcount = 0
		self._extensionfunctionclasses = []
		self._extensionfunctionclassescount = 0
		self._extensionfunctionallparams = []
		self._extensionfunctionallparamscount = 0
		self._name = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the extension object.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the extension object.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def extensionfunctionlinenumber(self) :
		ur"""Line number of the function in file.
		"""
		try :
			return self._extensionfunctionlinenumber
		except Exception as e:
			raise e

	@property
	def extensionfunctionclasses(self) :
		ur"""List of classes (including inherited) that the function is present in.
		"""
		try :
			return self._extensionfunctionclasses
		except Exception as e:
			raise e

	@property
	def extensionfunctionargtype(self) :
		ur"""List of extension function's arguments types.
		"""
		try :
			return self._extensionfunctionargtype
		except Exception as e:
			raise e

	@property
	def activeextensionfunction(self) :
		ur"""Extension function is in use or not.
		"""
		try :
			return self._activeextensionfunction
		except Exception as e:
			raise e

	@property
	def extensionfunctionname(self) :
		ur"""Name of extension function given in the extension.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._extensionfunctionname
		except Exception as e:
			raise e

	@property
	def extensionfunctionclasstype(self) :
		ur"""Extension function class type.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._extensionfunctionclasstype
		except Exception as e:
			raise e

	@property
	def extensionfuncdescription(self) :
		ur"""Any description to preserve information about the extension function.<br/>Maximum length =  1023.
		"""
		try :
			return self._extensionfuncdescription
		except Exception as e:
			raise e

	@property
	def extensionfunctionallparams(self) :
		ur"""List of parameters (including promotions) that the function can accept.
		"""
		try :
			return self._extensionfunctionallparams
		except Exception as e:
			raise e

	@property
	def extensionfunctionargcount(self) :
		ur"""Number of parameters in the extension function.
		"""
		try :
			return self._extensionfunctionargcount
		except Exception as e:
			raise e

	@property
	def extensionfunctionreturntype(self) :
		ur"""Extension function return type.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._extensionfunctionreturntype
		except Exception as e:
			raise e

	@property
	def extensionfunctionclassescount(self) :
		ur"""Number of classes the function is present in.
		"""
		try :
			return self._extensionfunctionclassescount
		except Exception as e:
			raise e

	@property
	def extensionfunctionallparamscount(self) :
		ur"""Number of parameters (including promotions) that the function can accept.
		"""
		try :
			return self._extensionfunctionallparamscount
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsextension_extensionfunction_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsextension_extensionfunction_binding
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
	def get(cls, service, name) :
		ur""" Use this API to fetch nsextension_extensionfunction_binding resources.
		"""
		try :
			obj = nsextension_extensionfunction_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of nsextension_extensionfunction_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsextension_extensionfunction_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count nsextension_extensionfunction_binding resources configued on NetScaler.
		"""
		try :
			obj = nsextension_extensionfunction_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		ur""" Use this API to count the filtered set of nsextension_extensionfunction_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsextension_extensionfunction_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class nsextension_extensionfunction_binding_response(base_response) :
	def __init__(self, length=1) :
		self.nsextension_extensionfunction_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsextension_extensionfunction_binding = [nsextension_extensionfunction_binding() for _ in range(length)]

