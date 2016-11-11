from nsapi import config
from urllib.parse import urlencode
import urllib.parse as urlparse

def buildURL(resource, params = {}):
	"""
	Bouwt een URL op basis van de resource identifier en query params.

	buildURL("ActueleVertrekTijden", {"station": "Utrecht Centraal"}) # dit returnt de string: 'http://webservices.ns.nl/ns-api-avt?station=Utrecht Centraal'
	"""
	url_parts = [
		config.protocol,
		config.host,
		config.resourceLocations[resource],
		None,
		params,
		None
	]

	url_parts[4] = urlencode(params)

	return urlparse.urlunparse(url_parts)