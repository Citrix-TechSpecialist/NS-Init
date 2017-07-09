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

class lsn_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._lsntottcprxpkts = 0
		self._lsntcprxpktsrate = 0
		self._lsntottcprxbytes = 0
		self._lsntcprxbytesrate = 0
		self._lsntottcptxpkts = 0
		self._lsntcptxpktsrate = 0
		self._lsntottcptxbytes = 0
		self._lsntcptxbytesrate = 0
		self._lsntottcpdrppkts = 0
		self._lsntcpdrppktsrate = 0
		self._lsncurtcpsessions = 0
		self._lsncurtcpsessionsrate = 0
		self._lsntotudprxpkts = 0
		self._lsnudprxpktsrate = 0
		self._lsntotudprxbytes = 0
		self._lsnudprxbytesrate = 0
		self._lsntotudptxpkts = 0
		self._lsnudptxpktsrate = 0
		self._lsntotudptxbytes = 0
		self._lsnudptxbytesrate = 0
		self._lsntotudpdrppkts = 0
		self._lsnudpdrppktsrate = 0
		self._lsncurudpsessions = 0
		self._lsncurudpsessionsrate = 0
		self._lsntoticmprxpkts = 0
		self._lsnicmprxpktsrate = 0
		self._lsntoticmprxbytes = 0
		self._lsnicmprxbytesrate = 0
		self._lsntoticmptxpkts = 0
		self._lsnicmptxpktsrate = 0
		self._lsntoticmptxbytes = 0
		self._lsnicmptxbytesrate = 0
		self._lsntoticmpdrppkts = 0
		self._lsnicmpdrppktsrate = 0
		self._lsncuricmpsessions = 0
		self._lsncuricmpsessionsrate = 0
		self._lsncursessions = 0
		self._lsncursessionsrate = 0
		self._lsncursubscribers = 0
		self._lsncursubscribersrate = 0

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
	def lsncursubscribersrate(self) :
		ur"""Rate (/s) counter for lsncursubscribers.
		"""
		try :
			return self._lsncursubscribersrate
		except Exception as e:
			raise e

	@property
	def lsntotudptxbytes(self) :
		ur"""Number of LSN UDP Transmitted bytes.
		"""
		try :
			return self._lsntotudptxbytes
		except Exception as e:
			raise e

	@property
	def lsncuricmpsessionsrate(self) :
		ur"""Rate (/s) counter for lsncuricmpsessions.
		"""
		try :
			return self._lsncuricmpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsncursessions(self) :
		ur"""Current number of LSN sessions.
		"""
		try :
			return self._lsncursessions
		except Exception as e:
			raise e

	@property
	def lsntottcptxbytes(self) :
		ur"""Number of LSN TCP Transmitted bytes.
		"""
		try :
			return self._lsntottcptxbytes
		except Exception as e:
			raise e

	@property
	def lsnudptxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotudptxbytes.
		"""
		try :
			return self._lsnudptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntotudpdrppkts(self) :
		ur"""Number of LSN UDP Dropped packets.
		"""
		try :
			return self._lsntotudpdrppkts
		except Exception as e:
			raise e

	@property
	def lsntottcpdrppkts(self) :
		ur"""Number of LSN TCP Dropped packets.
		"""
		try :
			return self._lsntottcpdrppkts
		except Exception as e:
			raise e

	@property
	def lsntoticmptxpkts(self) :
		ur"""Number of LSN ICMP Transmitted packets.
		"""
		try :
			return self._lsntoticmptxpkts
		except Exception as e:
			raise e

	@property
	def lsntcptxbytesrate(self) :
		ur"""Rate (/s) counter for lsntottcptxbytes.
		"""
		try :
			return self._lsntcptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsnudprxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotudprxbytes.
		"""
		try :
			return self._lsnudprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntcpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsntottcpdrppkts.
		"""
		try :
			return self._lsntcpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsntotudprxbytes(self) :
		ur"""Number of LSN UDP Received bytes.
		"""
		try :
			return self._lsntotudprxbytes
		except Exception as e:
			raise e

	@property
	def lsnicmpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsntoticmpdrppkts.
		"""
		try :
			return self._lsnicmpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsntottcprxbytes(self) :
		ur"""Number of LSN TCP Received bytes.
		"""
		try :
			return self._lsntottcprxbytes
		except Exception as e:
			raise e

	@property
	def lsntoticmptxbytes(self) :
		ur"""Number of LSN ICMP Transmitted bytes.
		"""
		try :
			return self._lsntoticmptxbytes
		except Exception as e:
			raise e

	@property
	def lsntoticmprxpkts(self) :
		ur"""Number of LSN ICMP Received packets.
		"""
		try :
			return self._lsntoticmprxpkts
		except Exception as e:
			raise e

	@property
	def lsnicmptxpktsrate(self) :
		ur"""Rate (/s) counter for lsntoticmptxpkts.
		"""
		try :
			return self._lsnicmptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsnicmprxbytesrate(self) :
		ur"""Rate (/s) counter for lsntoticmprxbytes.
		"""
		try :
			return self._lsnicmprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntoticmpdrppkts(self) :
		ur"""Number of LSN ICMP Dropped packets.
		"""
		try :
			return self._lsntoticmpdrppkts
		except Exception as e:
			raise e

	@property
	def lsntcprxpktsrate(self) :
		ur"""Rate (/s) counter for lsntottcprxpkts.
		"""
		try :
			return self._lsntcprxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntottcptxpkts(self) :
		ur"""Number of LSN TCP Transmitted packets.
		"""
		try :
			return self._lsntottcptxpkts
		except Exception as e:
			raise e

	@property
	def lsncurtcpsessionsrate(self) :
		ur"""Rate (/s) counter for lsncurtcpsessions.
		"""
		try :
			return self._lsncurtcpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsncursubscribers(self) :
		ur"""Current number of LSN subscribers.
		"""
		try :
			return self._lsncursubscribers
		except Exception as e:
			raise e

	@property
	def lsncurudpsessionsrate(self) :
		ur"""Rate (/s) counter for lsncurudpsessions.
		"""
		try :
			return self._lsncurudpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsnudptxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotudptxpkts.
		"""
		try :
			return self._lsnudptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntottcprxpkts(self) :
		ur"""Number of LSN TCP Received packets.
		"""
		try :
			return self._lsntottcprxpkts
		except Exception as e:
			raise e

	@property
	def lsnicmptxbytesrate(self) :
		ur"""Rate (/s) counter for lsntoticmptxbytes.
		"""
		try :
			return self._lsnicmptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntotudprxpkts(self) :
		ur"""Number of LSN UDP Received packets.
		"""
		try :
			return self._lsntotudprxpkts
		except Exception as e:
			raise e

	@property
	def lsncursessionsrate(self) :
		ur"""Rate (/s) counter for lsncursessions.
		"""
		try :
			return self._lsncursessionsrate
		except Exception as e:
			raise e

	@property
	def lsntcptxpktsrate(self) :
		ur"""Rate (/s) counter for lsntottcptxpkts.
		"""
		try :
			return self._lsntcptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsnudprxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotudprxpkts.
		"""
		try :
			return self._lsnudprxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotudptxpkts(self) :
		ur"""Number of LSN UDP Transmitted packets.
		"""
		try :
			return self._lsntotudptxpkts
		except Exception as e:
			raise e

	@property
	def lsncurudpsessions(self) :
		ur"""Number of LSN UDP Current Sessions.
		"""
		try :
			return self._lsncurudpsessions
		except Exception as e:
			raise e

	@property
	def lsnudpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsntotudpdrppkts.
		"""
		try :
			return self._lsnudpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsntoticmprxbytes(self) :
		ur"""Number of LSN ICMP Received bytes.
		"""
		try :
			return self._lsntoticmprxbytes
		except Exception as e:
			raise e

	@property
	def lsncuricmpsessions(self) :
		ur"""Number of LSN ICMP Current Sessions.
		"""
		try :
			return self._lsncuricmpsessions
		except Exception as e:
			raise e

	@property
	def lsncurtcpsessions(self) :
		ur"""Number of LSN TCP Current Sessions.
		"""
		try :
			return self._lsncurtcpsessions
		except Exception as e:
			raise e

	@property
	def lsntcprxbytesrate(self) :
		ur"""Rate (/s) counter for lsntottcprxbytes.
		"""
		try :
			return self._lsntcprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsnicmprxpktsrate(self) :
		ur"""Rate (/s) counter for lsntoticmprxpkts.
		"""
		try :
			return self._lsnicmprxpktsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsn_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsn
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all lsn_stats resources that are configured on netscaler.
		"""
		try :
			obj = lsn_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class lsn_response(base_response) :
	def __init__(self, length=1) :
		self.lsn = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsn = [lsn_stats() for _ in range(length)]

