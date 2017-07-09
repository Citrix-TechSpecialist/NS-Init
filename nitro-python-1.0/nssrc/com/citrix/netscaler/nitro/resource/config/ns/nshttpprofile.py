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

class nshttpprofile(base_resource) :
	""" Configuration for HTTP profile resource. """
	def __init__(self) :
		self._name = ""
		self._dropinvalreqs = ""
		self._markhttp09inval = ""
		self._markconnreqinval = ""
		self._cmponpush = ""
		self._conmultiplex = ""
		self._maxreusepool = 0
		self._dropextracrlf = ""
		self._incomphdrdelay = 0
		self._websocket = ""
		self._rtsptunnel = ""
		self._reqtimeout = 0
		self._adpttimeout = ""
		self._reqtimeoutaction = ""
		self._dropextradata = ""
		self._weblog = ""
		self._clientiphdrexpr = ""
		self._maxreq = 0
		self._persistentetag = ""
		self._spdy = ""
		self._http2 = ""
		self._reusepooltimeout = 0
		self._maxheaderlen = 0
		self._minreusepool = 0
		self._http2maxheaderlistsize = 0
		self._http2maxframesize = 0
		self._http2maxconcurrentstreams = 0
		self._http2initialwindowsize = 0
		self._http2headertablesize = 0
		self._refcnt = 0
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for an HTTP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a HTTP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my http profile" or 'my http profile'\).<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for an HTTP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a HTTP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my http profile" or 'my http profile'\).<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def dropinvalreqs(self) :
		ur"""Drop invalid HTTP requests or responses.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropinvalreqs
		except Exception as e:
			raise e

	@dropinvalreqs.setter
	def dropinvalreqs(self, dropinvalreqs) :
		ur"""Drop invalid HTTP requests or responses.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropinvalreqs = dropinvalreqs
		except Exception as e:
			raise e

	@property
	def markhttp09inval(self) :
		ur"""Mark HTTP/0.9 requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._markhttp09inval
		except Exception as e:
			raise e

	@markhttp09inval.setter
	def markhttp09inval(self, markhttp09inval) :
		ur"""Mark HTTP/0.9 requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._markhttp09inval = markhttp09inval
		except Exception as e:
			raise e

	@property
	def markconnreqinval(self) :
		ur"""Mark CONNECT requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._markconnreqinval
		except Exception as e:
			raise e

	@markconnreqinval.setter
	def markconnreqinval(self, markconnreqinval) :
		ur"""Mark CONNECT requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._markconnreqinval = markconnreqinval
		except Exception as e:
			raise e

	@property
	def cmponpush(self) :
		ur"""Start data compression on receiving a TCP packet with PUSH flag set.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cmponpush
		except Exception as e:
			raise e

	@cmponpush.setter
	def cmponpush(self, cmponpush) :
		ur"""Start data compression on receiving a TCP packet with PUSH flag set.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cmponpush = cmponpush
		except Exception as e:
			raise e

	@property
	def conmultiplex(self) :
		ur"""Reuse server connections for requests from more than one client connections.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._conmultiplex
		except Exception as e:
			raise e

	@conmultiplex.setter
	def conmultiplex(self, conmultiplex) :
		ur"""Reuse server connections for requests from more than one client connections.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._conmultiplex = conmultiplex
		except Exception as e:
			raise e

	@property
	def maxreusepool(self) :
		ur"""Maximum limit on the number of connections, from the NetScaler to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time. Zero implies no limit on reuse pool size.<br/>Default value: 0<br/>Maximum length =  360000.
		"""
		try :
			return self._maxreusepool
		except Exception as e:
			raise e

	@maxreusepool.setter
	def maxreusepool(self, maxreusepool) :
		ur"""Maximum limit on the number of connections, from the NetScaler to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time. Zero implies no limit on reuse pool size.<br/>Default value: 0<br/>Maximum length =  360000
		"""
		try :
			self._maxreusepool = maxreusepool
		except Exception as e:
			raise e

	@property
	def dropextracrlf(self) :
		ur"""Drop any extra 'CR' and 'LF' characters present after the header.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropextracrlf
		except Exception as e:
			raise e

	@dropextracrlf.setter
	def dropextracrlf(self, dropextracrlf) :
		ur"""Drop any extra 'CR' and 'LF' characters present after the header.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropextracrlf = dropextracrlf
		except Exception as e:
			raise e

	@property
	def incomphdrdelay(self) :
		ur"""Maximum time to wait, in milliseconds, between incomplete header packets. If the header packets take longer to arrive at NetScaler, the connection is silently dropped.<br/>Default value: 7000<br/>Minimum length =  1<br/>Maximum length =  360000.
		"""
		try :
			return self._incomphdrdelay
		except Exception as e:
			raise e

	@incomphdrdelay.setter
	def incomphdrdelay(self, incomphdrdelay) :
		ur"""Maximum time to wait, in milliseconds, between incomplete header packets. If the header packets take longer to arrive at NetScaler, the connection is silently dropped.<br/>Default value: 7000<br/>Minimum length =  1<br/>Maximum length =  360000
		"""
		try :
			self._incomphdrdelay = incomphdrdelay
		except Exception as e:
			raise e

	@property
	def websocket(self) :
		ur"""HTTP connection to be upgraded to a web socket connection. Once upgraded, NetScaler does not process Layer 7 traffic on this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._websocket
		except Exception as e:
			raise e

	@websocket.setter
	def websocket(self, websocket) :
		ur"""HTTP connection to be upgraded to a web socket connection. Once upgraded, NetScaler does not process Layer 7 traffic on this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._websocket = websocket
		except Exception as e:
			raise e

	@property
	def rtsptunnel(self) :
		ur"""Allow RTSP tunnel in HTTP. Once application/x-rtsp-tunnelled is seen in Accept or Content-Type header, NetScaler does not process Layer 7 traffic on this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rtsptunnel
		except Exception as e:
			raise e

	@rtsptunnel.setter
	def rtsptunnel(self, rtsptunnel) :
		ur"""Allow RTSP tunnel in HTTP. Once application/x-rtsp-tunnelled is seen in Accept or Content-Type header, NetScaler does not process Layer 7 traffic on this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rtsptunnel = rtsptunnel
		except Exception as e:
			raise e

	@property
	def reqtimeout(self) :
		ur"""Time, in seconds, within which the HTTP request must complete. If the request does not complete within this time, the specified request timeout action is executed. Zero disables the timeout.<br/>Default value: 0<br/>Maximum length =  86400.
		"""
		try :
			return self._reqtimeout
		except Exception as e:
			raise e

	@reqtimeout.setter
	def reqtimeout(self, reqtimeout) :
		ur"""Time, in seconds, within which the HTTP request must complete. If the request does not complete within this time, the specified request timeout action is executed. Zero disables the timeout.<br/>Default value: 0<br/>Maximum length =  86400
		"""
		try :
			self._reqtimeout = reqtimeout
		except Exception as e:
			raise e

	@property
	def adpttimeout(self) :
		ur"""Adapts the configured request timeout based on flow conditions. The timeout is increased or decreased internally and applied on the flow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._adpttimeout
		except Exception as e:
			raise e

	@adpttimeout.setter
	def adpttimeout(self, adpttimeout) :
		ur"""Adapts the configured request timeout based on flow conditions. The timeout is increased or decreased internally and applied on the flow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._adpttimeout = adpttimeout
		except Exception as e:
			raise e

	@property
	def reqtimeoutaction(self) :
		ur"""Action to take when the HTTP request does not complete within the specified request timeout duration. You can configure the following actions:
		* RESET - Send RST (reset) to client when timeout occurs.
		* DROP - Drop silently when timeout occurs.
		* Custom responder action - Name of the responder action to trigger when timeout occurs, used to send custom message.
		"""
		try :
			return self._reqtimeoutaction
		except Exception as e:
			raise e

	@reqtimeoutaction.setter
	def reqtimeoutaction(self, reqtimeoutaction) :
		ur"""Action to take when the HTTP request does not complete within the specified request timeout duration. You can configure the following actions:
		* RESET - Send RST (reset) to client when timeout occurs.
		* DROP - Drop silently when timeout occurs.
		* Custom responder action - Name of the responder action to trigger when timeout occurs, used to send custom message.
		"""
		try :
			self._reqtimeoutaction = reqtimeoutaction
		except Exception as e:
			raise e

	@property
	def dropextradata(self) :
		ur"""Drop any extra data when server sends more data than the specified content-length.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropextradata
		except Exception as e:
			raise e

	@dropextradata.setter
	def dropextradata(self, dropextradata) :
		ur"""Drop any extra data when server sends more data than the specified content-length.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropextradata = dropextradata
		except Exception as e:
			raise e

	@property
	def weblog(self) :
		ur"""Enable or disable web logging.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._weblog
		except Exception as e:
			raise e

	@weblog.setter
	def weblog(self, weblog) :
		ur"""Enable or disable web logging.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._weblog = weblog
		except Exception as e:
			raise e

	@property
	def clientiphdrexpr(self) :
		ur"""Name of the header that contains the real client IP address.
		"""
		try :
			return self._clientiphdrexpr
		except Exception as e:
			raise e

	@clientiphdrexpr.setter
	def clientiphdrexpr(self, clientiphdrexpr) :
		ur"""Name of the header that contains the real client IP address.
		"""
		try :
			self._clientiphdrexpr = clientiphdrexpr
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		ur"""Maximum number of requests allowed on a single connection. Zero implies no limit on the number of requests.<br/>Default value: 0<br/>Maximum length =  65534.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@maxreq.setter
	def maxreq(self, maxreq) :
		ur"""Maximum number of requests allowed on a single connection. Zero implies no limit on the number of requests.<br/>Default value: 0<br/>Maximum length =  65534
		"""
		try :
			self._maxreq = maxreq
		except Exception as e:
			raise e

	@property
	def persistentetag(self) :
		ur"""Generate the persistent NetScaler specific ETag for the HTTP response with ETag header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._persistentetag
		except Exception as e:
			raise e

	@persistentetag.setter
	def persistentetag(self, persistentetag) :
		ur"""Generate the persistent NetScaler specific ETag for the HTTP response with ETag header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._persistentetag = persistentetag
		except Exception as e:
			raise e

	@property
	def spdy(self) :
		ur"""Enable SPDYv2 or SPDYv3 or both over SSL vserver. SSL will advertise SPDY support either during NPN Handshake or when client will advertises SPDY support during ALPN handshake. Both SPDY versions are enabled when this parameter is set to ENABLED.<br/>Default value: DISABLED<br/>Possible values = DISABLED, ENABLED, V2, V3.
		"""
		try :
			return self._spdy
		except Exception as e:
			raise e

	@spdy.setter
	def spdy(self, spdy) :
		ur"""Enable SPDYv2 or SPDYv3 or both over SSL vserver. SSL will advertise SPDY support either during NPN Handshake or when client will advertises SPDY support during ALPN handshake. Both SPDY versions are enabled when this parameter is set to ENABLED.<br/>Default value: DISABLED<br/>Possible values = DISABLED, ENABLED, V2, V3
		"""
		try :
			self._spdy = spdy
		except Exception as e:
			raise e

	@property
	def http2(self) :
		ur"""Choose whether to enable support for HTTP/2 (draft-14).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._http2
		except Exception as e:
			raise e

	@http2.setter
	def http2(self, http2) :
		ur"""Choose whether to enable support for HTTP/2 (draft-14).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._http2 = http2
		except Exception as e:
			raise e

	@property
	def reusepooltimeout(self) :
		ur"""Idle timeout (in seconds) for server connections in re-use pool. Connections in the re-use pool are flushed, if they remain idle for the configured timeout.<br/>Default value: 0<br/>Maximum length =  31536000.
		"""
		try :
			return self._reusepooltimeout
		except Exception as e:
			raise e

	@reusepooltimeout.setter
	def reusepooltimeout(self, reusepooltimeout) :
		ur"""Idle timeout (in seconds) for server connections in re-use pool. Connections in the re-use pool are flushed, if they remain idle for the configured timeout.<br/>Default value: 0<br/>Maximum length =  31536000
		"""
		try :
			self._reusepooltimeout = reusepooltimeout
		except Exception as e:
			raise e

	@property
	def maxheaderlen(self) :
		ur"""Number of bytes to be queued to look for complete header before returning error. If complete header is not obtained after queuing these many bytes, request will be marked as invalid and no L7 processing will be done for that TCP connection.<br/>Default value: 24820<br/>Minimum length =  2048<br/>Maximum length =  61440.
		"""
		try :
			return self._maxheaderlen
		except Exception as e:
			raise e

	@maxheaderlen.setter
	def maxheaderlen(self, maxheaderlen) :
		ur"""Number of bytes to be queued to look for complete header before returning error. If complete header is not obtained after queuing these many bytes, request will be marked as invalid and no L7 processing will be done for that TCP connection.<br/>Default value: 24820<br/>Minimum length =  2048<br/>Maximum length =  61440
		"""
		try :
			self._maxheaderlen = maxheaderlen
		except Exception as e:
			raise e

	@property
	def minreusepool(self) :
		ur"""Minimum limit on the number of connections, from the NetScaler to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time. Zero implies no limit on reuse pool size.<br/>Default value: 0<br/>Maximum length =  360000.
		"""
		try :
			return self._minreusepool
		except Exception as e:
			raise e

	@minreusepool.setter
	def minreusepool(self, minreusepool) :
		ur"""Minimum limit on the number of connections, from the NetScaler to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time. Zero implies no limit on reuse pool size.<br/>Default value: 0<br/>Maximum length =  360000
		"""
		try :
			self._minreusepool = minreusepool
		except Exception as e:
			raise e

	@property
	def http2maxheaderlistsize(self) :
		ur"""Maximum size of header list that the NetScaler is prepared to accept, in bytes. NOTE: The actual plain text header size that the NetScaler accepts is limited by maxHeaderLen. Please change this parameter as well when modifying http2MaxHeaderListSize.<br/>Default value: 24576<br/>Minimum length =  8192<br/>Maximum length =  65535.
		"""
		try :
			return self._http2maxheaderlistsize
		except Exception as e:
			raise e

	@http2maxheaderlistsize.setter
	def http2maxheaderlistsize(self, http2maxheaderlistsize) :
		ur"""Maximum size of header list that the NetScaler is prepared to accept, in bytes. NOTE: The actual plain text header size that the NetScaler accepts is limited by maxHeaderLen. Please change this parameter as well when modifying http2MaxHeaderListSize.<br/>Default value: 24576<br/>Minimum length =  8192<br/>Maximum length =  65535
		"""
		try :
			self._http2maxheaderlistsize = http2maxheaderlistsize
		except Exception as e:
			raise e

	@property
	def http2maxframesize(self) :
		ur"""Maximum size of the frame payload that the NetScaler is willing to receive, in bytes.<br/>Default value: 16384<br/>Minimum length =  16384<br/>Maximum length =  16777215.
		"""
		try :
			return self._http2maxframesize
		except Exception as e:
			raise e

	@http2maxframesize.setter
	def http2maxframesize(self, http2maxframesize) :
		ur"""Maximum size of the frame payload that the NetScaler is willing to receive, in bytes.<br/>Default value: 16384<br/>Minimum length =  16384<br/>Maximum length =  16777215
		"""
		try :
			self._http2maxframesize = http2maxframesize
		except Exception as e:
			raise e

	@property
	def http2maxconcurrentstreams(self) :
		ur"""Maximum number of concurrent streams that is allowed per connection.<br/>Default value: 100<br/>Maximum length =  1000.
		"""
		try :
			return self._http2maxconcurrentstreams
		except Exception as e:
			raise e

	@http2maxconcurrentstreams.setter
	def http2maxconcurrentstreams(self, http2maxconcurrentstreams) :
		ur"""Maximum number of concurrent streams that is allowed per connection.<br/>Default value: 100<br/>Maximum length =  1000
		"""
		try :
			self._http2maxconcurrentstreams = http2maxconcurrentstreams
		except Exception as e:
			raise e

	@property
	def http2initialwindowsize(self) :
		ur"""Initial window size for stream level flow control, in bytes.<br/>Default value: 65535<br/>Minimum length =  8192<br/>Maximum length =  20971520.
		"""
		try :
			return self._http2initialwindowsize
		except Exception as e:
			raise e

	@http2initialwindowsize.setter
	def http2initialwindowsize(self, http2initialwindowsize) :
		ur"""Initial window size for stream level flow control, in bytes.<br/>Default value: 65535<br/>Minimum length =  8192<br/>Maximum length =  20971520
		"""
		try :
			self._http2initialwindowsize = http2initialwindowsize
		except Exception as e:
			raise e

	@property
	def http2headertablesize(self) :
		ur"""Maximum size of the header compression table used to decode header blocks, in bytes.<br/>Default value: 4096<br/>Maximum length =  16384.
		"""
		try :
			return self._http2headertablesize
		except Exception as e:
			raise e

	@http2headertablesize.setter
	def http2headertablesize(self, http2headertablesize) :
		ur"""Maximum size of the header compression table used to decode header blocks, in bytes.<br/>Default value: 4096<br/>Maximum length =  16384
		"""
		try :
			self._http2headertablesize = http2headertablesize
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		ur"""Number of entities using this profile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Flag to determine if http profile is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nshttpprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nshttpprofile
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
	def add(cls, client, resource) :
		ur""" Use this API to add nshttpprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = nshttpprofile()
				addresource.name = resource.name
				addresource.dropinvalreqs = resource.dropinvalreqs
				addresource.markhttp09inval = resource.markhttp09inval
				addresource.markconnreqinval = resource.markconnreqinval
				addresource.cmponpush = resource.cmponpush
				addresource.conmultiplex = resource.conmultiplex
				addresource.maxreusepool = resource.maxreusepool
				addresource.dropextracrlf = resource.dropextracrlf
				addresource.incomphdrdelay = resource.incomphdrdelay
				addresource.websocket = resource.websocket
				addresource.rtsptunnel = resource.rtsptunnel
				addresource.reqtimeout = resource.reqtimeout
				addresource.adpttimeout = resource.adpttimeout
				addresource.reqtimeoutaction = resource.reqtimeoutaction
				addresource.dropextradata = resource.dropextradata
				addresource.weblog = resource.weblog
				addresource.clientiphdrexpr = resource.clientiphdrexpr
				addresource.maxreq = resource.maxreq
				addresource.persistentetag = resource.persistentetag
				addresource.spdy = resource.spdy
				addresource.http2 = resource.http2
				addresource.reusepooltimeout = resource.reusepooltimeout
				addresource.maxheaderlen = resource.maxheaderlen
				addresource.minreusepool = resource.minreusepool
				addresource.http2maxheaderlistsize = resource.http2maxheaderlistsize
				addresource.http2maxframesize = resource.http2maxframesize
				addresource.http2maxconcurrentstreams = resource.http2maxconcurrentstreams
				addresource.http2initialwindowsize = resource.http2initialwindowsize
				addresource.http2headertablesize = resource.http2headertablesize
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nshttpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].dropinvalreqs = resource[i].dropinvalreqs
						addresources[i].markhttp09inval = resource[i].markhttp09inval
						addresources[i].markconnreqinval = resource[i].markconnreqinval
						addresources[i].cmponpush = resource[i].cmponpush
						addresources[i].conmultiplex = resource[i].conmultiplex
						addresources[i].maxreusepool = resource[i].maxreusepool
						addresources[i].dropextracrlf = resource[i].dropextracrlf
						addresources[i].incomphdrdelay = resource[i].incomphdrdelay
						addresources[i].websocket = resource[i].websocket
						addresources[i].rtsptunnel = resource[i].rtsptunnel
						addresources[i].reqtimeout = resource[i].reqtimeout
						addresources[i].adpttimeout = resource[i].adpttimeout
						addresources[i].reqtimeoutaction = resource[i].reqtimeoutaction
						addresources[i].dropextradata = resource[i].dropextradata
						addresources[i].weblog = resource[i].weblog
						addresources[i].clientiphdrexpr = resource[i].clientiphdrexpr
						addresources[i].maxreq = resource[i].maxreq
						addresources[i].persistentetag = resource[i].persistentetag
						addresources[i].spdy = resource[i].spdy
						addresources[i].http2 = resource[i].http2
						addresources[i].reusepooltimeout = resource[i].reusepooltimeout
						addresources[i].maxheaderlen = resource[i].maxheaderlen
						addresources[i].minreusepool = resource[i].minreusepool
						addresources[i].http2maxheaderlistsize = resource[i].http2maxheaderlistsize
						addresources[i].http2maxframesize = resource[i].http2maxframesize
						addresources[i].http2maxconcurrentstreams = resource[i].http2maxconcurrentstreams
						addresources[i].http2initialwindowsize = resource[i].http2initialwindowsize
						addresources[i].http2headertablesize = resource[i].http2headertablesize
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nshttpprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nshttpprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nshttpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nshttpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nshttpprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = nshttpprofile()
				updateresource.name = resource.name
				updateresource.dropinvalreqs = resource.dropinvalreqs
				updateresource.markhttp09inval = resource.markhttp09inval
				updateresource.markconnreqinval = resource.markconnreqinval
				updateresource.cmponpush = resource.cmponpush
				updateresource.conmultiplex = resource.conmultiplex
				updateresource.maxreusepool = resource.maxreusepool
				updateresource.dropextracrlf = resource.dropextracrlf
				updateresource.incomphdrdelay = resource.incomphdrdelay
				updateresource.websocket = resource.websocket
				updateresource.rtsptunnel = resource.rtsptunnel
				updateresource.reqtimeout = resource.reqtimeout
				updateresource.adpttimeout = resource.adpttimeout
				updateresource.reqtimeoutaction = resource.reqtimeoutaction
				updateresource.dropextradata = resource.dropextradata
				updateresource.weblog = resource.weblog
				updateresource.clientiphdrexpr = resource.clientiphdrexpr
				updateresource.maxreq = resource.maxreq
				updateresource.persistentetag = resource.persistentetag
				updateresource.spdy = resource.spdy
				updateresource.http2 = resource.http2
				updateresource.http2maxheaderlistsize = resource.http2maxheaderlistsize
				updateresource.http2maxframesize = resource.http2maxframesize
				updateresource.http2maxconcurrentstreams = resource.http2maxconcurrentstreams
				updateresource.http2initialwindowsize = resource.http2initialwindowsize
				updateresource.http2headertablesize = resource.http2headertablesize
				updateresource.reusepooltimeout = resource.reusepooltimeout
				updateresource.maxheaderlen = resource.maxheaderlen
				updateresource.minreusepool = resource.minreusepool
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nshttpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].dropinvalreqs = resource[i].dropinvalreqs
						updateresources[i].markhttp09inval = resource[i].markhttp09inval
						updateresources[i].markconnreqinval = resource[i].markconnreqinval
						updateresources[i].cmponpush = resource[i].cmponpush
						updateresources[i].conmultiplex = resource[i].conmultiplex
						updateresources[i].maxreusepool = resource[i].maxreusepool
						updateresources[i].dropextracrlf = resource[i].dropextracrlf
						updateresources[i].incomphdrdelay = resource[i].incomphdrdelay
						updateresources[i].websocket = resource[i].websocket
						updateresources[i].rtsptunnel = resource[i].rtsptunnel
						updateresources[i].reqtimeout = resource[i].reqtimeout
						updateresources[i].adpttimeout = resource[i].adpttimeout
						updateresources[i].reqtimeoutaction = resource[i].reqtimeoutaction
						updateresources[i].dropextradata = resource[i].dropextradata
						updateresources[i].weblog = resource[i].weblog
						updateresources[i].clientiphdrexpr = resource[i].clientiphdrexpr
						updateresources[i].maxreq = resource[i].maxreq
						updateresources[i].persistentetag = resource[i].persistentetag
						updateresources[i].spdy = resource[i].spdy
						updateresources[i].http2 = resource[i].http2
						updateresources[i].http2maxheaderlistsize = resource[i].http2maxheaderlistsize
						updateresources[i].http2maxframesize = resource[i].http2maxframesize
						updateresources[i].http2maxconcurrentstreams = resource[i].http2maxconcurrentstreams
						updateresources[i].http2initialwindowsize = resource[i].http2initialwindowsize
						updateresources[i].http2headertablesize = resource[i].http2headertablesize
						updateresources[i].reusepooltimeout = resource[i].reusepooltimeout
						updateresources[i].maxheaderlen = resource[i].maxheaderlen
						updateresources[i].minreusepool = resource[i].minreusepool
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nshttpprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nshttpprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nshttpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nshttpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nshttpprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nshttpprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nshttpprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nshttpprofile() for _ in range(len(name))]
							obj = [nshttpprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nshttpprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nshttpprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nshttpprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nshttpprofile resources configured on NetScaler.
		"""
		try :
			obj = nshttpprofile()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of nshttpprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nshttpprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Conmultiplex:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Markhttp09inval:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Adpttimeout:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Markconnreqinval:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Spdy:
		DISABLED = "DISABLED"
		ENABLED = "ENABLED"
		V2 = "V2"
		V3 = "V3"

	class Persistentetag:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rtsptunnel:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropinvalreqs:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropextracrlf:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Http2:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropextradata:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Websocket:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cmponpush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Weblog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nshttpprofile_response(base_response) :
	def __init__(self, length=1) :
		self.nshttpprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nshttpprofile = [nshttpprofile() for _ in range(length)]

