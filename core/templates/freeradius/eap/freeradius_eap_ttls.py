#!/usr/bin/python

freeradius_eap_ttls = '''

	## EAP-TTLS
	#
	#  The TTLS module implements the EAP-TTLS protocol,
	#  which can be described as EAP inside of Diameter,
	#  inside of TLS, inside of EAP, inside of RADIUS...
	#
	#  Surprisingly, it works quite well.
	#
	ttls {
		#  Which tls-config section the TLS negotiation parameters
		#  are in - see EAP-TLS above for an explanation.
		#
		#  In the case that an old configuration from FreeRADIUS
		#  v2.x is being used, all the options of the tls-config
		#  section may also appear instead in the 'tls' section
		#  above. If that is done, the tls= option here (and in
		#  tls above) MUST be commented out.
		#
		tls = tls-common

		#  The tunneled EAP session needs a default EAP type
		#  which is separate from the one for the non-tunneled
		#  EAP module.  Inside of the TTLS tunnel, we recommend
		#  using EAP-MD5.  If the request does not contain an
		#  EAP conversation, then this configuration entry is
		#  ignored.
		#
		default_eap_type = md5

		#  The tunneled authentication request does not usually
		#  contain useful attributes like 'Calling-Station-Id',
		#  etc.  These attributes are outside of the tunnel,
		#  and normally unavailable to the tunneled
		#  authentication request.
		#
		#  By setting this configuration entry to 'yes',
		#  any attribute which is NOT in the tunneled
		#  authentication request, but which IS available
		#  outside of the tunnel, is copied to the tunneled
		#  request.
		#
		#  allowed values: {no, yes}
		#
		copy_request_to_tunnel = no

		#
		#  As of version 3.0.5, this configuration item
		#  is deprecated.  Instead, you should use
		#
		# 	update outer.session-state {
		#		...
		#
		#	}
		#
		#  This will cache attributes for the final Access-Accept.
		#
		#  The reply attributes sent to the NAS are usually
		#  based on the name of the user 'outside' of the
		#  tunnel (usually 'anonymous').  If you want to send
		#  the reply attributes based on the user name inside
		#  of the tunnel, then set this configuration entry to
		#  'yes', and the reply to the NAS will be taken from
		#  the reply to the tunneled request.
		#
		#  allowed values: {no, yes}
		#
		use_tunneled_reply = no

		#
		#  The inner tunneled request can be sent
		#  through a virtual server constructed
		#  specifically for this purpose.
		#
		#  If this entry is commented out, the inner
		#  tunneled request will be sent through
		#  the virtual server that processed the
		#  outer requests.
		#
		virtual_server = "inner-tunnel"

		#  This has the same meaning, and overwrites, the
		#  same field in the "tls" configuration, above.
		#  The default value here is "yes".
		#
	#	include_length = yes

		#
		# Unlike EAP-TLS, EAP-TTLS does not require a client
		# certificate. However, you can require one by setting the
		# following option. You can also override this option by
		# setting
		#
		#	EAP-TLS-Require-Client-Cert = Yes
		#
		# in the control items for a request.
		#
	#	require_client_cert = yes
	}

'''
