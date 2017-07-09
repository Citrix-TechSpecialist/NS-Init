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


class lsndeterministicnat_args :
	ur""" Provides additional arguments required for fetching the lsndeterministicnat resource.
	"""
	def __init__(self) :
		self._clientname = ""
		self._network6 = ""
		self._subscrip = ""
		self._td = 0
		self._natip = ""

	@property
	def clientname(self) :
		ur"""The name of the LSN Client.
		"""
		try :
			return self._clientname
		except Exception as e:
			raise e

	@clientname.setter
	def clientname(self, clientname) :
		ur"""The name of the LSN Client.
		"""
		try :
			self._clientname = clientname
		except Exception as e:
			raise e

	@property
	def network6(self) :
		ur"""IPv6 address of the LSN subscriber or B4 device.
		"""
		try :
			return self._network6
		except Exception as e:
			raise e

	@network6.setter
	def network6(self, network6) :
		ur"""IPv6 address of the LSN subscriber or B4 device.
		"""
		try :
			self._network6 = network6
		except Exception as e:
			raise e

	@property
	def subscrip(self) :
		ur"""The Client IP address.
		"""
		try :
			return self._subscrip
		except Exception as e:
			raise e

	@subscrip.setter
	def subscrip(self, subscrip) :
		ur"""The Client IP address.
		"""
		try :
			self._subscrip = subscrip
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""The LSN client TD.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""The LSN client TD.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def natip(self) :
		ur"""The NAT IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._natip
		except Exception as e:
			raise e

	@natip.setter
	def natip(self, natip) :
		ur"""The NAT IP address.<br/>Minimum length =  1
		"""
		try :
			self._natip = natip
		except Exception as e:
			raise e

