import config
import requests
import xmltodict
from errorHandling import NSException, checkForError

def getDepartures(station):
	"""
	Haalt alle vertrekkende treinen op van het opgegeven station.
	"""
	departures = []
	url = config.buildURL("ActueleVertrekTijden", {"station": station})
	
	response = requests.get(url, auth = config.authDetails)
	xml = xmltodict.parse(response.text)

	checkForError(url, xml)

	for vertrek in xml["ActueleVertrekTijden"]["VertrekkendeTrein"]:
		# De volgende waarden zijn altijd beschikbaar
		departure = {
			"RideNumber": vertrek["RitNummer"],
			"DepartureTime": vertrek["VertrekTijd"][11:16],
			"DepartureDate": vertrek["VertrekTijd"][0:10],
			"Destination": vertrek["EindBestemming"],
			"TrainType": vertrek["TreinSoort"],
			"Transporter": vertrek["Vervoerder"],
			"DeparturePlatform": vertrek["VertrekSpoor"]["#text"],
			"DeparturePlatformChanged": vertrek["VertrekSpoor"]["@wijziging"]	
		}

		# De volgende waarden zijn niet altijd beschikbaar
		if "VertrekVertraging" in vertrek:
			departure["DepartureDelay"] = vertrek["VertrekVertraging"]

		if "VertrekVertragingTekst" in vertrek:
			departure["DepartureDelayText"] = vertrek["VertrekVertragingTekst"]

		if "RouteTekst" in vertrek:
			departure["RouteText"] = vertrek["RouteTekst"]

		if "ReisTip" in vertrek:
			departure["TravelTip"] = vertrek["ReisTip"]

		if "Opmerkingen" in vertrek:
			departure["Comments"] = vertrek["Opmerkingen"] 

		departures.append(departure)
	return departures

try:
	print(getDepartures("Utrecht Centraal"))
except requests.exceptions.ConnectionError as e:
	print("Je bent offline!")
except NSException as e:
	print(str(e))