import urllib.parse as urlparse
from urllib.parse import urlencode

protocol = "http"
host = "webservices.ns.nl"

resourceLocations = {
	"Stations": "/ns-api-stations-v2",
	"ActueleVertrekTijden": "/ns-api-avt"
}

username = "jerrylooman87@gmail.com"
password = "ox8ZKmRylP2hf71QCmuq-3_XcKp_iemmoOJFTgyVRaRkDdiZw1d4Fg"

authDetails = (username, password)

def reconfigure():
	"""
	Herinitialiseert de configuratie
	"""
	authDetails = (username, password)

def buildURL(resource, params = {}):
	url_parts = [
		protocol,
		host,
		resourceLocations[resource],
		None,
		params,
		None
	]

	url_parts[4] = urlencode(params)

	return urlparse.urlunparse(url_parts)
