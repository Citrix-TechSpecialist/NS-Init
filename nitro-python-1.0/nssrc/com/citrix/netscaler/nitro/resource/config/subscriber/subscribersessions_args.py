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


class subscribersessions_args :
	ur""" Provides additional arguments required for fetching the subscribersessions resource.
	"""
	def __init__(self) :
		self._ip = ""

	@property
	def ip(self) :
		ur"""Subscriber IP Address.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@ip.setter
	def ip(self, ip) :
		ur"""Subscriber IP Address.
		"""
		try :
			self._ip = ip
		except Exception as e:
			raise e

