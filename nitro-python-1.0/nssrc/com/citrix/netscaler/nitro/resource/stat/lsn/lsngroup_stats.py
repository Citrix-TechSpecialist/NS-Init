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

class lsngroup_stats(base_resource) :
	ur""" Statistics for LSN group resource.
	"""
	def __init__(self) :
		self._groupname = ""
		self._clearstats = ""
		self._lsngrpcursessions = 0
		self._lsngrpcursessionsrate = 0
		self._lsngrptottranslbytes = 0
		self._lsngrptranslbytesrate = 0
		self._lsngrptottranslpkts = 0
		self._lsngrptranslpktsrate = 0
		self._lsngrptottcptranslpkts = 0
		self._lsngrptcptranslpktsrate = 0
		self._lsngrptottcptranslbytes = 0
		self._lsngrptcptranslbytesrate = 0
		self._lsngrptottcpdrppkts = 0
		self._lsngrptcpdrppktsrate = 0
		self._lsngrpcurtcpsessions = 0
		self._lsngrpcurtcpsessionsrate = 0
		self._lsngrptotudptranslpkts = 0
		self._lsngrpudptranslpktsrate = 0
		self._lsngrptotudptranslbytes = 0
		self._lsngrpudptranslbytesrate = 0
		self._lsngrptotudpdrppkts = 0
		self._lsngrpudpdrppktsrate = 0
		self._lsngrpcurudpsessions = 0
		self._lsngrpcurudpsessionsrate = 0
		self._lsngrptoticmptranslpkts = 0
		self._lsngrpicmptranslpktsrate = 0
		self._lsngrptoticmptranslbytes = 0
		self._lsngrpicmptranslbytesrate = 0
		self._lsngrptoticmpdrppkts = 0
		self._lsngrpicmpdrppktsrate = 0
		self._lsngrpcuricmpsessions = 0
		self._lsngrpcuricmpsessionsrate = 0
		self._lsngrpcursubscribers = 0
		self._lsngrpcursubscribersrate = 0

	@property
	def groupname(self) :
		ur"""Name of the LSN Group.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""Name of the LSN Group.
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		ur"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		ur"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def lsngrptcptranslbytesrate(self) :
		ur"""Rate (/s) counter for lsngrptottcptranslbytes.
		"""
		try :
			return self._lsngrptcptranslbytesrate
		except Exception as e:
			raise e

	@property
	def lsngrptottranslpkts(self) :
		ur"""Number of Translated Pkts for LSN group.
		"""
		try :
			return self._lsngrptottranslpkts
		except Exception as e:
			raise e

	@property
	def lsngrptoticmptranslpkts(self) :
		ur"""Number of ICMP Translated Pkts for LSN group.
		"""
		try :
			return self._lsngrptoticmptranslpkts
		except Exception as e:
			raise e

	@property
	def lsngrpcurtcpsessions(self) :
		ur"""Number of TCP Current Sessions for LSN group.
		"""
		try :
			return self._lsngrpcurtcpsessions
		except Exception as e:
			raise e

	@property
	def lsngrpicmptranslbytesrate(self) :
		ur"""Rate (/s) counter for lsngrptoticmptranslbytes.
		"""
		try :
			return self._lsngrpicmptranslbytesrate
		except Exception as e:
			raise e

	@property
	def lsngrptotudptranslpkts(self) :
		ur"""Number of UDP Translated Pkts for LSN group.
		"""
		try :
			return self._lsngrptotudptranslpkts
		except Exception as e:
			raise e

	@property
	def lsngrptottcpdrppkts(self) :
		ur"""Number of TCP Dropped Pkts for LSN group.
		"""
		try :
			return self._lsngrptottcpdrppkts
		except Exception as e:
			raise e

	@property
	def lsngrptranslbytesrate(self) :
		ur"""Rate (/s) counter for lsngrptottranslbytes.
		"""
		try :
			return self._lsngrptranslbytesrate
		except Exception as e:
			raise e

	@property
	def lsngrptotudptranslbytes(self) :
		ur"""Number of UDP Translated Bytes for LSN group.
		"""
		try :
			return self._lsngrptotudptranslbytes
		except Exception as e:
			raise e

	@property
	def lsngrptoticmptranslbytes(self) :
		ur"""Number of ICMP Translated Bytes for LSN group.
		"""
		try :
			return self._lsngrptoticmptranslbytes
		except Exception as e:
			raise e

	@property
	def lsngrpcursubscribersrate(self) :
		ur"""Rate (/s) counter for lsngrpcursubscribers.
		"""
		try :
			return self._lsngrpcursubscribersrate
		except Exception as e:
			raise e

	@property
	def lsngrptottranslbytes(self) :
		ur"""Number of Translated Bytes for LSN group.
		"""
		try :
			return self._lsngrptottranslbytes
		except Exception as e:
			raise e

	@property
	def lsngrptoticmpdrppkts(self) :
		ur"""Number of ICMP Dropped Pkts for LSN group.
		"""
		try :
			return self._lsngrptoticmpdrppkts
		except Exception as e:
			raise e

	@property
	def lsngrptcptranslpktsrate(self) :
		ur"""Rate (/s) counter for lsngrptottcptranslpkts.
		"""
		try :
			return self._lsngrptcptranslpktsrate
		except Exception as e:
			raise e

	@property
	def lsngrpudptranslpktsrate(self) :
		ur"""Rate (/s) counter for lsngrptotudptranslpkts.
		"""
		try :
			return self._lsngrpudptranslpktsrate
		except Exception as e:
			raise e

	@property
	def lsngrpcursubscribers(self) :
		ur"""Number of ICMP Current Sessions for LSN group.
		"""
		try :
			return self._lsngrpcursubscribers
		except Exception as e:
			raise e

	@property
	def lsngrpudptranslbytesrate(self) :
		ur"""Rate (/s) counter for lsngrptotudptranslbytes.
		"""
		try :
			return self._lsngrpudptranslbytesrate
		except Exception as e:
			raise e

	@property
	def lsngrpcuricmpsessionsrate(self) :
		ur"""Rate (/s) counter for lsngrpcuricmpsessions.
		"""
		try :
			return self._lsngrpcuricmpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsngrpcurudpsessions(self) :
		ur"""Number of UDP Current Sessions for LSN group.
		"""
		try :
			return self._lsngrpcurudpsessions
		except Exception as e:
			raise e

	@property
	def lsngrptottcptranslpkts(self) :
		ur"""Number of TCP Translated Pkts for LSN group.
		"""
		try :
			return self._lsngrptottcptranslpkts
		except Exception as e:
			raise e

	@property
	def lsngrptotudpdrppkts(self) :
		ur"""Number of UDP Dropped Pkts for LSN group.
		"""
		try :
			return self._lsngrptotudpdrppkts
		except Exception as e:
			raise e

	@property
	def lsngrpicmptranslpktsrate(self) :
		ur"""Rate (/s) counter for lsngrptoticmptranslpkts.
		"""
		try :
			return self._lsngrpicmptranslpktsrate
		except Exception as e:
			raise e

	@property
	def lsngrpcuricmpsessions(self) :
		ur"""Number of ICMP Current Sessions for LSN group.
		"""
		try :
			return self._lsngrpcuricmpsessions
		except Exception as e:
			raise e

	@property
	def lsngrpcurtcpsessionsrate(self) :
		ur"""Rate (/s) counter for lsngrpcurtcpsessions.
		"""
		try :
			return self._lsngrpcurtcpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsngrpcurudpsessionsrate(self) :
		ur"""Rate (/s) counter for lsngrpcurudpsessions.
		"""
		try :
			return self._lsngrpcurudpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsngrptranslpktsrate(self) :
		ur"""Rate (/s) counter for lsngrptottranslpkts.
		"""
		try :
			return self._lsngrptranslpktsrate
		except Exception as e:
			raise e

	@property
	def lsngrptottcptranslbytes(self) :
		ur"""Number of TCP Translated Bytes for LSN group.
		"""
		try :
			return self._lsngrptottcptranslbytes
		except Exception as e:
			raise e

	@property
	def lsngrpicmpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsngrptoticmpdrppkts.
		"""
		try :
			return self._lsngrpicmpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsngrpcursessionsrate(self) :
		ur"""Rate (/s) counter for lsngrpcursessions.
		"""
		try :
			return self._lsngrpcursessionsrate
		except Exception as e:
			raise e

	@property
	def lsngrpudpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsngrptotudpdrppkts.
		"""
		try :
			return self._lsngrpudpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsngrptcpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsngrptottcpdrppkts.
		"""
		try :
			return self._lsngrptcpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsngrpcursessions(self) :
		ur"""Number of Current Sessions for LSN group.
		"""
		try :
			return self._lsngrpcursessions
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsngroup_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsngroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.groupname is not None :
				return str(self.groupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all lsngroup_stats resources that are configured on netscaler.
		"""
		try :
			obj = lsngroup_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.groupname = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class lsngroup_response(base_response) :
	def __init__(self, length=1) :
		self.lsngroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsngroup = [lsngroup_stats() for _ in range(length)]

