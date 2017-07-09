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

class lsndslite_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._lsntotdsliterxpkts = 0
		self._lsndsliterxpktsrate = 0
		self._lsntotdsliterxbytes = 0
		self._lsndsliterxbytesrate = 0
		self._lsntotdslitetxpkts = 0
		self._lsndslitetxpktsrate = 0
		self._lsntotdslitetxbytes = 0
		self._lsndslitetxbytesrate = 0
		self._lsntotdslitetcprxpkts = 0
		self._lsndslitetcprxpktsrate = 0
		self._lsntotdslitetcprxbytes = 0
		self._lsndslitetcprxbytesrate = 0
		self._lsntotdslitetcptxpkts = 0
		self._lsndslitetcptxpktsrate = 0
		self._lsntotdslitetcptxbytes = 0
		self._lsndslitetcptxbytesrate = 0
		self._lsntotdslitetcpdrppkts = 0
		self._lsndslitetcpdrppktsrate = 0
		self._lsncurdslitetcpsessions = 0
		self._lsncurdslitetcpsessionsrate = 0
		self._lsntotdsliteudprxpkts = 0
		self._lsndsliteudprxpktsrate = 0
		self._lsntotdsliteudprxbytes = 0
		self._lsndsliteudprxbytesrate = 0
		self._lsntotdsliteudptxpkts = 0
		self._lsndsliteudptxpktsrate = 0
		self._lsntotdsliteudptxbytes = 0
		self._lsndsliteudptxbytesrate = 0
		self._lsntotdsliteudpdrppkts = 0
		self._lsndsliteudpdrppktsrate = 0
		self._lsncurdsliteudpsessions = 0
		self._lsncurdsliteudpsessionsrate = 0
		self._lsntotdsliteicmprxpkts = 0
		self._lsndsliteicmprxpktsrate = 0
		self._lsntotdsliteicmprxbytes = 0
		self._lsndsliteicmprxbytesrate = 0
		self._lsntotdsliteicmptxpkts = 0
		self._lsndsliteicmptxpktsrate = 0
		self._lsntotdsliteicmptxbytes = 0
		self._lsndsliteicmptxbytesrate = 0
		self._lsntotdsliteicmpdrppkts = 0
		self._lsndsliteicmpdrppktsrate = 0
		self._lsncurdsliteicmpsessions = 0
		self._lsncurdsliteicmpsessionsrate = 0
		self._lsncurdslitesessions = 0
		self._lsncurdslitesessionsrate = 0
		self._lsndslitecursubscribers = 0
		self._lsndslitecursubscribersrate = 0

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
	def lsntotdsliteudpdrppkts(self) :
		ur"""Number of LSN DS-Lite UDP Dropped packets.
		"""
		try :
			return self._lsntotdsliteudpdrppkts
		except Exception as e:
			raise e

	@property
	def lsndsliteudprxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteudprxpkts.
		"""
		try :
			return self._lsndsliteudprxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotdsliterxpkts(self) :
		ur"""Total number of LSN DS-Lite rx pkts.
		"""
		try :
			return self._lsntotdsliterxpkts
		except Exception as e:
			raise e

	@property
	def lsntotdslitetxbytes(self) :
		ur"""Total number of LSN DS-Lite tx bytes.
		"""
		try :
			return self._lsntotdslitetxbytes
		except Exception as e:
			raise e

	@property
	def lsncurdsliteicmpsessionsrate(self) :
		ur"""Rate (/s) counter for lsncurdsliteicmpsessions.
		"""
		try :
			return self._lsncurdsliteicmpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsntotdsliteudptxbytes(self) :
		ur"""Number of LSN DS-Lite UDP Transmitted bytes.
		"""
		try :
			return self._lsntotdsliteudptxbytes
		except Exception as e:
			raise e

	@property
	def lsntotdsliteicmptxpkts(self) :
		ur"""Number of LSN DS-Lite ICMP Transmitted packets.
		"""
		try :
			return self._lsntotdsliteicmptxpkts
		except Exception as e:
			raise e

	@property
	def lsndslitetxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotdslitetxpkts.
		"""
		try :
			return self._lsndslitetxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotdsliteicmptxbytes(self) :
		ur"""Number of LSN DS-Lite ICMP Transmitted bytes.
		"""
		try :
			return self._lsntotdsliteicmptxbytes
		except Exception as e:
			raise e

	@property
	def lsntotdsliterxbytes(self) :
		ur"""Total number of LSN DS-Lite rx bytes.
		"""
		try :
			return self._lsntotdsliterxbytes
		except Exception as e:
			raise e

	@property
	def lsntotdsliteicmpdrppkts(self) :
		ur"""Number of LSN DS-Lite ICMP Dropped packets.
		"""
		try :
			return self._lsntotdsliteicmpdrppkts
		except Exception as e:
			raise e

	@property
	def lsncurdslitetcpsessionsrate(self) :
		ur"""Rate (/s) counter for lsncurdslitetcpsessions.
		"""
		try :
			return self._lsncurdslitetcpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsndsliteudptxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteudptxbytes.
		"""
		try :
			return self._lsndsliteudptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntotdsliteudprxbytes(self) :
		ur"""Number of LSN DS-Lite UDP Received bytes.
		"""
		try :
			return self._lsntotdsliteudprxbytes
		except Exception as e:
			raise e

	@property
	def lsndsliterxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotdsliterxbytes.
		"""
		try :
			return self._lsndsliterxbytesrate
		except Exception as e:
			raise e

	@property
	def lsncurdsliteicmpsessions(self) :
		ur"""Number of LSN DS-Lite ICMP Current Sessions.
		"""
		try :
			return self._lsncurdsliteicmpsessions
		except Exception as e:
			raise e

	@property
	def lsndsliteicmprxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteicmprxbytes.
		"""
		try :
			return self._lsndsliteicmprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsndsliteudpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteudpdrppkts.
		"""
		try :
			return self._lsndsliteudpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsntotdslitetcpdrppkts(self) :
		ur"""Number of LSN DS-Lite TCP Dropped packets.
		"""
		try :
			return self._lsntotdslitetcpdrppkts
		except Exception as e:
			raise e

	@property
	def lsntotdsliteicmprxbytes(self) :
		ur"""Number of LSN DS-Lite ICMP Received bytes.
		"""
		try :
			return self._lsntotdsliteicmprxbytes
		except Exception as e:
			raise e

	@property
	def lsncurdslitesessionsrate(self) :
		ur"""Rate (/s) counter for lsncurdslitesessions.
		"""
		try :
			return self._lsncurdslitesessionsrate
		except Exception as e:
			raise e

	@property
	def lsntotdsliteicmprxpkts(self) :
		ur"""Number of LSN DS-Lite ICMP Received packets.
		"""
		try :
			return self._lsntotdsliteicmprxpkts
		except Exception as e:
			raise e

	@property
	def lsntotdslitetxpkts(self) :
		ur"""Total number of LSN DS-Lite tx pkts.
		"""
		try :
			return self._lsntotdslitetxpkts
		except Exception as e:
			raise e

	@property
	def lsncurdsliteudpsessionsrate(self) :
		ur"""Rate (/s) counter for lsncurdsliteudpsessions.
		"""
		try :
			return self._lsncurdsliteudpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsndslitetcptxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotdslitetcptxpkts.
		"""
		try :
			return self._lsndslitetcptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotdslitetcptxpkts(self) :
		ur"""Number of LSN DS-Lite TCP Transmitted packets.
		"""
		try :
			return self._lsntotdslitetcptxpkts
		except Exception as e:
			raise e

	@property
	def lsndsliteicmptxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteicmptxpkts.
		"""
		try :
			return self._lsndsliteicmptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsndsliteicmpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteicmpdrppkts.
		"""
		try :
			return self._lsndsliteicmpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsntotdsliteudprxpkts(self) :
		ur"""Number of LSN DS-Lite UDP Received packets.
		"""
		try :
			return self._lsntotdsliteudprxpkts
		except Exception as e:
			raise e

	@property
	def lsncurdslitetcpsessions(self) :
		ur"""Number of LSN DS-Lite TCP Current Sessions.
		"""
		try :
			return self._lsncurdslitetcpsessions
		except Exception as e:
			raise e

	@property
	def lsndslitetxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotdslitetxbytes.
		"""
		try :
			return self._lsndslitetxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntotdslitetcprxbytes(self) :
		ur"""Number of LSN DS-Lite TCP Received bytes.
		"""
		try :
			return self._lsntotdslitetcprxbytes
		except Exception as e:
			raise e

	@property
	def lsndsliteicmptxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteicmptxbytes.
		"""
		try :
			return self._lsndsliteicmptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsndsliteicmprxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteicmprxpkts.
		"""
		try :
			return self._lsndsliteicmprxpktsrate
		except Exception as e:
			raise e

	@property
	def lsncurdslitesessions(self) :
		ur"""Current number of LSN DS-Lite sessions.
		"""
		try :
			return self._lsncurdslitesessions
		except Exception as e:
			raise e

	@property
	def lsndslitetcprxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotdslitetcprxbytes.
		"""
		try :
			return self._lsndslitetcprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsndslitecursubscribers(self) :
		ur"""Current number of LSN DS-Lite subscribers.
		"""
		try :
			return self._lsndslitecursubscribers
		except Exception as e:
			raise e

	@property
	def lsntotdslitetcprxpkts(self) :
		ur"""Number of LSN DS-Lite TCP Received packets.
		"""
		try :
			return self._lsntotdslitetcprxpkts
		except Exception as e:
			raise e

	@property
	def lsndsliterxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotdsliterxpkts.
		"""
		try :
			return self._lsndsliterxpktsrate
		except Exception as e:
			raise e

	@property
	def lsncurdsliteudpsessions(self) :
		ur"""Number of LSN DS-Lite UDP Current Sessions.
		"""
		try :
			return self._lsncurdsliteudpsessions
		except Exception as e:
			raise e

	@property
	def lsndslitetcprxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotdslitetcprxpkts.
		"""
		try :
			return self._lsndslitetcprxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotdsliteudptxpkts(self) :
		ur"""Number of LSN DS-Lite UDP Transmitted packets.
		"""
		try :
			return self._lsntotdsliteudptxpkts
		except Exception as e:
			raise e

	@property
	def lsntotdslitetcptxbytes(self) :
		ur"""Number of LSN DS-Lite TCP Transmitted bytes.
		"""
		try :
			return self._lsntotdslitetcptxbytes
		except Exception as e:
			raise e

	@property
	def lsndslitetcpdrppktsrate(self) :
		ur"""Rate (/s) counter for lsntotdslitetcpdrppkts.
		"""
		try :
			return self._lsndslitetcpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsndslitetcptxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotdslitetcptxbytes.
		"""
		try :
			return self._lsndslitetcptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsndsliteudprxbytesrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteudprxbytes.
		"""
		try :
			return self._lsndsliteudprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsndsliteudptxpktsrate(self) :
		ur"""Rate (/s) counter for lsntotdsliteudptxpkts.
		"""
		try :
			return self._lsndsliteudptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsndslitecursubscribersrate(self) :
		ur"""Rate (/s) counter for lsndslitecursubscribers.
		"""
		try :
			return self._lsndslitecursubscribersrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsndslite_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsndslite
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
		ur""" Use this API to fetch the statistics of all lsndslite_stats resources that are configured on netscaler.
		"""
		try :
			obj = lsndslite_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class lsndslite_response(base_response) :
	def __init__(self, length=1) :
		self.lsndslite = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsndslite = [lsndslite_stats() for _ in range(length)]

