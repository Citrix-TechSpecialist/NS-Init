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


class lsnstatic_args :
	ur""" Provides additional arguments required for fetching the lsnstatic resource.
	"""
	def __init__(self) :
		self._nattype = ""

	@property
	def nattype(self) :
		ur"""Type of sessions to be displayed.<br/>Possible values = NAT44, DS-Lite.
		"""
		try :
			return self._nattype
		except Exception as e:
			raise e

	@nattype.setter
	def nattype(self, nattype) :
		ur"""Type of sessions to be displayed.<br/>Possible values = NAT44, DS-Lite
		"""
		try :
			self._nattype = nattype
		except Exception as e:
			raise e

	class Nattype:
		NAT44 = "NAT44"
		DS_Lite = "DS-Lite"

