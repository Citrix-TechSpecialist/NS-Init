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

class subscribergxinterface(base_resource) :
	""" Configuration for Gx interface Parameters resource. """
	def __init__(self) :
		self._vserver = ""
		self._service = ""
		self._pcrfrealm = ""
		self._holdonsubscriberabsence = ""
		self._requesttimeout = 0
		self._requestretryattempts = 0
		self._idlettl = 0
		self._revalidationtimeout = 0
		self._negativettl = 0
		self._servicepathavp = []
		self._servicepathvendorid = 0
		self._svrstate = ""
		self._identity = ""
		self._realm = ""
		self._status = ""
		self._servicepathinfomode = ""

	@property
	def vserver(self) :
		ur"""Name of the load balancing, or content switching vserver to which the Gx connections are established. The service type of the virtual server must be DIAMETER/SSL_DIAMETER. Mutually exclusive with the service parameter. Therefore, you cannot set both service and the Virtual Server in the Gx Interface.<br/>Minimum length =  1.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		ur"""Name of the load balancing, or content switching vserver to which the Gx connections are established. The service type of the virtual server must be DIAMETER/SSL_DIAMETER. Mutually exclusive with the service parameter. Therefore, you cannot set both service and the Virtual Server in the Gx Interface.<br/>Minimum length =  1
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

	@property
	def service(self) :
		ur"""Name of DIAMETER/SSL_DIAMETER service corresponding to PCRF to which the Gx connection is established. The service type of the service must be DIAMETER/SSL_DIAMETER. Mutually exclusive with vserver parameter. Therefore, you cannot set both Service and the Virtual Server in the Gx Interface.<br/>Minimum length =  1.
		"""
		try :
			return self._service
		except Exception as e:
			raise e

	@service.setter
	def service(self, service) :
		ur"""Name of DIAMETER/SSL_DIAMETER service corresponding to PCRF to which the Gx connection is established. The service type of the service must be DIAMETER/SSL_DIAMETER. Mutually exclusive with vserver parameter. Therefore, you cannot set both Service and the Virtual Server in the Gx Interface.<br/>Minimum length =  1
		"""
		try :
			self._service = service
		except Exception as e:
			raise e

	@property
	def pcrfrealm(self) :
		ur"""PCRF realm is of type DiameterIdentity and contains the realm of PCRF to which the message is to be routed. This is the realm used in Destination-Realm AVP by Netscaler Gx client (as a Diameter node).
		<br/>Minimum length =  1.
		"""
		try :
			return self._pcrfrealm
		except Exception as e:
			raise e

	@pcrfrealm.setter
	def pcrfrealm(self, pcrfrealm) :
		ur"""PCRF realm is of type DiameterIdentity and contains the realm of PCRF to which the message is to be routed. This is the realm used in Destination-Realm AVP by Netscaler Gx client (as a Diameter node).
		<br/>Minimum length =  1
		"""
		try :
			self._pcrfrealm = pcrfrealm
		except Exception as e:
			raise e

	@property
	def holdonsubscriberabsence(self) :
		ur"""Set this setting to yes if Netscaler needs to Hold pakcets till subscriber session is fetched from PCRF. Else set to NO. By default set to yes. If this setting is set to NO, then till NetScaler fetches subscriber from PCRF, default subscriber profile will be applied to this subscriber if configured. If default subscriber profile is also not configured an undef would be raised to expressions which use Subscriber attributes. .<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._holdonsubscriberabsence
		except Exception as e:
			raise e

	@holdonsubscriberabsence.setter
	def holdonsubscriberabsence(self, holdonsubscriberabsence) :
		ur"""Set this setting to yes if Netscaler needs to Hold pakcets till subscriber session is fetched from PCRF. Else set to NO. By default set to yes. If this setting is set to NO, then till NetScaler fetches subscriber from PCRF, default subscriber profile will be applied to this subscriber if configured. If default subscriber profile is also not configured an undef would be raised to expressions which use Subscriber attributes. .<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._holdonsubscriberabsence = holdonsubscriberabsence
		except Exception as e:
			raise e

	@property
	def requesttimeout(self) :
		ur"""q!Time, in seconds, within which the Gx CCR request must complete. If the request does not complete within this time, the request is retransmitted for requestRetryAttempts time. If still reuqest is not complete then default subscriber profile will be applied to this subscriber if configured. If default subscriber profile is also not configured an undef would be raised to expressions which use Subscriber attributes.
		Zero disables the timeout. !.<br/>Default value: 10<br/>Maximum length =  86400.
		"""
		try :
			return self._requesttimeout
		except Exception as e:
			raise e

	@requesttimeout.setter
	def requesttimeout(self, requesttimeout) :
		ur"""q!Time, in seconds, within which the Gx CCR request must complete. If the request does not complete within this time, the request is retransmitted for requestRetryAttempts time. If still reuqest is not complete then default subscriber profile will be applied to this subscriber if configured. If default subscriber profile is also not configured an undef would be raised to expressions which use Subscriber attributes.
		Zero disables the timeout. !.<br/>Default value: 10<br/>Maximum length =  86400
		"""
		try :
			self._requesttimeout = requesttimeout
		except Exception as e:
			raise e

	@property
	def requestretryattempts(self) :
		ur"""If the request does not complete within requestTimeout time, the request is retransmitted for requestRetryAttempts time.<br/>Default value: 3.
		"""
		try :
			return self._requestretryattempts
		except Exception as e:
			raise e

	@requestretryattempts.setter
	def requestretryattempts(self, requestretryattempts) :
		ur"""If the request does not complete within requestTimeout time, the request is retransmitted for requestRetryAttempts time.<br/>Default value: 3
		"""
		try :
			self._requestretryattempts = requestretryattempts
		except Exception as e:
			raise e

	@property
	def idlettl(self) :
		ur"""q!Idle Time, in seconds, after which the Gx CCR-U request will be sent after any PCRF activity on a session. Any RAR or CCA message resets the timer.
		Zero value disables the idle timeout. !.<br/>Default value: 900<br/>Maximum length =  86400.
		"""
		try :
			return self._idlettl
		except Exception as e:
			raise e

	@idlettl.setter
	def idlettl(self, idlettl) :
		ur"""q!Idle Time, in seconds, after which the Gx CCR-U request will be sent after any PCRF activity on a session. Any RAR or CCA message resets the timer.
		Zero value disables the idle timeout. !.<br/>Default value: 900<br/>Maximum length =  86400
		"""
		try :
			self._idlettl = idlettl
		except Exception as e:
			raise e

	@property
	def revalidationtimeout(self) :
		ur"""q!Revalidation Timeout, in seconds, after which the Gx CCR-U request will be sent after any PCRF activity on a session. Any RAR or CCA message resets the timer.
		Zero value disables the idle timeout. !.<br/>Default value: 0<br/>Maximum length =  86400.
		"""
		try :
			return self._revalidationtimeout
		except Exception as e:
			raise e

	@revalidationtimeout.setter
	def revalidationtimeout(self, revalidationtimeout) :
		ur"""q!Revalidation Timeout, in seconds, after which the Gx CCR-U request will be sent after any PCRF activity on a session. Any RAR or CCA message resets the timer.
		Zero value disables the idle timeout. !.<br/>Default value: 0<br/>Maximum length =  86400
		"""
		try :
			self._revalidationtimeout = revalidationtimeout
		except Exception as e:
			raise e

	@property
	def negativettl(self) :
		ur"""q!Negative TTL, in seconds, after which the Gx CCR-I request will be resent for sessions that have not been resolved by PCRF due to server being down or no response or failed response. Instead of polling the PCRF server constantly, negative-TTL makes NS stick to un-resolved session. Meanwhile Netscaler installs a negative session to avoid going to PCRF.
		For Negative Sessions, Netcaler inherits the attributes from default subscriber profile if default subscriber is configured. A default subscriber could be configured as 'add subscriber profile *'. Or these attributes can be inherited from Radius as well if Radius is configued.
		Zero value disables the Negative Sessions. And Netscaler does not install Negative sessions even if subscriber session could not be fetched. !.<br/>Default value: 600<br/>Maximum length =  86400.
		"""
		try :
			return self._negativettl
		except Exception as e:
			raise e

	@negativettl.setter
	def negativettl(self, negativettl) :
		ur"""q!Negative TTL, in seconds, after which the Gx CCR-I request will be resent for sessions that have not been resolved by PCRF due to server being down or no response or failed response. Instead of polling the PCRF server constantly, negative-TTL makes NS stick to un-resolved session. Meanwhile Netscaler installs a negative session to avoid going to PCRF.
		For Negative Sessions, Netcaler inherits the attributes from default subscriber profile if default subscriber is configured. A default subscriber could be configured as 'add subscriber profile *'. Or these attributes can be inherited from Radius as well if Radius is configued.
		Zero value disables the Negative Sessions. And Netscaler does not install Negative sessions even if subscriber session could not be fetched. !.<br/>Default value: 600<br/>Maximum length =  86400
		"""
		try :
			self._negativettl = negativettl
		except Exception as e:
			raise e

	@property
	def servicepathavp(self) :
		ur""" The AVP code in which PCRF sends service path applicable for subscriber.<br/>Minimum length =  1.
		"""
		try :
			return self._servicepathavp
		except Exception as e:
			raise e

	@servicepathavp.setter
	def servicepathavp(self, servicepathavp) :
		ur""" The AVP code in which PCRF sends service path applicable for subscriber.<br/>Minimum length =  1
		"""
		try :
			self._servicepathavp = servicepathavp
		except Exception as e:
			raise e

	@property
	def servicepathvendorid(self) :
		ur""" The vendorid of the AVP in which PCRF sends service path for subscriber.
		"""
		try :
			return self._servicepathvendorid
		except Exception as e:
			raise e

	@servicepathvendorid.setter
	def servicepathvendorid(self, servicepathvendorid) :
		ur""" The vendorid of the AVP in which PCRF sends service path for subscriber.
		"""
		try :
			self._servicepathvendorid = servicepathvendorid
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		ur"""The state of the gx service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	@property
	def identity(self) :
		ur"""DiameterIdentity to be used by NS. DiameterIdentity is used to identify a Diameter node uniquely. Before setting up diameter configuration, Netscaler (as a Diameter node) MUST be assigned a unique DiameterIdentity.
		example =>
		set ns diameter -identity netscaler.com
		Now whenever Netscaler system needs to use identity in diameter messages. It will use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
		.<br/>Minimum length =  1.
		"""
		try :
			return self._identity
		except Exception as e:
			raise e

	@property
	def realm(self) :
		ur"""Diameter Realm to be used by NS.
		example =>
		set ns diameter -realm com
		Now whenever Netscaler system needs to use realm in diameter messages. It will use 'com' as Origin-Realm AVP as defined in RFC3588
		.<br/>Minimum length =  1.
		"""
		try :
			return self._realm
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""NetScaler PCRF connection Status. (Gx Protocol State).
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def servicepathinfomode(self) :
		ur""" The type of info in which service path is passed from PCRF,
		SERVICE_FUNCTION: Denotes the service chain is passed as servicefunction names in-order in AVPS with code servicepathAVP
		SERVICE_PATH: Denotes the service path name is passed in AVPS with code servicepathAVP.q.<br/>Default value: SERVICEPATH<br/>Possible values = SERVICEFUNCTIONS, SERVICEPATH.
		"""
		try :
			return self._servicepathinfomode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(subscribergxinterface_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.subscribergxinterface
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
	def update(cls, client, resource) :
		ur""" Use this API to update subscribergxinterface.
		"""
		try :
			if type(resource) is not list :
				updateresource = subscribergxinterface()
				updateresource.vserver = resource.vserver
				updateresource.service = resource.service
				updateresource.pcrfrealm = resource.pcrfrealm
				updateresource.holdonsubscriberabsence = resource.holdonsubscriberabsence
				updateresource.requesttimeout = resource.requesttimeout
				updateresource.requestretryattempts = resource.requestretryattempts
				updateresource.idlettl = resource.idlettl
				updateresource.revalidationtimeout = resource.revalidationtimeout
				updateresource.negativettl = resource.negativettl
				updateresource.servicepathavp = resource.servicepathavp
				updateresource.servicepathvendorid = resource.servicepathvendorid
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of subscribergxinterface resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = subscribergxinterface()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the subscribergxinterface resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = subscribergxinterface()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Servicepathinfomode:
		SERVICEFUNCTIONS = "SERVICEFUNCTIONS"
		SERVICEPATH = "SERVICEPATH"

	class Svrstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Holdonsubscriberabsence:
		YES = "YES"
		NO = "NO"

class subscribergxinterface_response(base_response) :
	def __init__(self, length=1) :
		self.subscribergxinterface = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.subscribergxinterface = [subscribergxinterface() for _ in range(length)]

