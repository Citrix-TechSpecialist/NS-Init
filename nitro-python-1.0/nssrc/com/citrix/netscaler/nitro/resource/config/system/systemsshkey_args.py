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


class systemsshkey_args :
	ur""" Provides additional arguments required for fetching the systemsshkey resource.
	"""
	def __init__(self) :
		self._sshkeytype = ""

	@property
	def sshkeytype(self) :
		ur"""The type of the ssh key whether public or private key.<br/>Possible values = PRIVATE, PUBLIC.
		"""
		try :
			return self._sshkeytype
		except Exception as e:
			raise e

	@sshkeytype.setter
	def sshkeytype(self, sshkeytype) :
		ur"""The type of the ssh key whether public or private key.<br/>Possible values = PRIVATE, PUBLIC
		"""
		try :
			self._sshkeytype = sshkeytype
		except Exception as e:
			raise e

	class Sshkeytype:
		PRIVATE = "PRIVATE"
		PUBLIC = "PUBLIC"

