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


class techsupport_args :
	ur""" Provides additional arguments required for fetching the techsupport resource.
	"""
	def __init__(self) :
		self._scope = ""
		self._partitionname = ""
		self._upload = False
		self._proxy = ""
		self._casenumber = ""
		self._file = ""
		self._description = ""
		self._username = ""
		self._password = ""

	@property
	def scope(self) :
		ur"""Use this option to gather data on the present node, all cluster nodes, or for the specified partitions. The CLUSTER scope generates smaller abbreviated archives for all nodes. The PARTITION scope collects the admin partition in addition to those specified. The partitionName option is only required for the PARTITION scope.<br/>Default value: NODE<br/>Possible values = NODE, CLUSTER, PARTITION.
		"""
		try :
			return self._scope
		except Exception as e:
			raise e

	@scope.setter
	def scope(self, scope) :
		ur"""Use this option to gather data on the present node, all cluster nodes, or for the specified partitions. The CLUSTER scope generates smaller abbreviated archives for all nodes. The PARTITION scope collects the admin partition in addition to those specified. The partitionName option is only required for the PARTITION scope.<br/>Default value: NODE<br/>Possible values = NODE, CLUSTER, PARTITION
		"""
		try :
			self._scope = scope
		except Exception as e:
			raise e

	@property
	def partitionname(self) :
		ur"""Name of the partition.<br/>Minimum length =  1.
		"""
		try :
			return self._partitionname
		except Exception as e:
			raise e

	@partitionname.setter
	def partitionname(self, partitionname) :
		ur"""Name of the partition.<br/>Minimum length =  1
		"""
		try :
			self._partitionname = partitionname
		except Exception as e:
			raise e

	@property
	def upload(self) :
		ur"""Securely upload the collector archive to Citrix Technical Support using SSL. MyCitrix credentials will be required. If used with the -file option, no new collector archive is generated. Instead, the specified archive is uploaded. Note that the upload operation time depends on the size of the archive file, and the connection bandwidth.
		"""
		try :
			return self._upload
		except Exception as e:
			raise e

	@upload.setter
	def upload(self, upload) :
		ur"""Securely upload the collector archive to Citrix Technical Support using SSL. MyCitrix credentials will be required. If used with the -file option, no new collector archive is generated. Instead, the specified archive is uploaded. Note that the upload operation time depends on the size of the archive file, and the connection bandwidth.
		"""
		try :
			self._upload = upload
		except Exception as e:
			raise e

	@property
	def proxy(self) :
		ur"""Specifies the proxy server to be used when uploading a collector archive. Use this parameter if the NetScaler appliance does not have direct internet connectivity. The basic format of the proxy string is: "proxy_IP:<proxy_port>" (without quotes). If the proxy requires authentication the format is: "username:password@proxy_IP:<proxy_port>".
		"""
		try :
			return self._proxy
		except Exception as e:
			raise e

	@proxy.setter
	def proxy(self, proxy) :
		ur"""Specifies the proxy server to be used when uploading a collector archive. Use this parameter if the NetScaler appliance does not have direct internet connectivity. The basic format of the proxy string is: "proxy_IP:<proxy_port>" (without quotes). If the proxy requires authentication the format is: "username:password@proxy_IP:<proxy_port>".
		"""
		try :
			self._proxy = proxy
		except Exception as e:
			raise e

	@property
	def casenumber(self) :
		ur"""Specifies the associated case or service request number if it has already been opened with Citrix Technical Support.
		"""
		try :
			return self._casenumber
		except Exception as e:
			raise e

	@casenumber.setter
	def casenumber(self, casenumber) :
		ur"""Specifies the associated case or service request number if it has already been opened with Citrix Technical Support.
		"""
		try :
			self._casenumber = casenumber
		except Exception as e:
			raise e

	@property
	def file(self) :
		ur"""Specifies the name (with full path) of the collector archive file to be uploaded. If this is specified, no new collector archive is generated.
		"""
		try :
			return self._file
		except Exception as e:
			raise e

	@file.setter
	def file(self, file) :
		ur"""Specifies the name (with full path) of the collector archive file to be uploaded. If this is specified, no new collector archive is generated.
		"""
		try :
			self._file = file
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""Provides a text description for the the upload, and can be used for logging purposes.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@description.setter
	def description(self, description) :
		ur"""Provides a text description for the the upload, and can be used for logging purposes.
		"""
		try :
			self._description = description
		except Exception as e:
			raise e

	@property
	def username(self) :
		ur"""Specifies My Citrix user name, which is used to login to Citrix upload server.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""Specifies My Citrix user name, which is used to login to Citrix upload server.
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Specifies My Citrix password, which is used to login to Citrix upload server.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Specifies My Citrix password, which is used to login to Citrix upload server.
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	class Scope:
		NODE = "NODE"
		CLUSTER = "CLUSTER"
		PARTITION = "PARTITION"

