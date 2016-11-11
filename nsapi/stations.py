import requests
import xmltodict
from nsapi import config, urlBuilder, errorHandling
from nsapi.errorHandling import NSException, checkForError

def getStations():
	"""
	Haalt alle stations op van de NS.
	"""
	url = urlBuilder.buildURL("Stations")

	stations = []
	response = requests.get(url, auth = (config.username, config.password))
	xml = xmltodict.parse(response.text)

	for xmlStation in xml["Stations"]["Station"]:
		station = {}
		
		station["Code"] = xmlStation["Code"]
		station["Type"] = xmlStation["Type"]
		station["Names"] = {}
		namesDict = station["Names"]

		for index, value in xmlStation["Namen"].items():
			if index == "Kort":
				namesDict["Short"] = value
			elif index == "Middel":
				namesDict["Medium"] = value
			elif index == "Lang":
				namesDict["Long"] = value

		station["Country"] = xmlStation["Land"]
		station["UICCode"] = xmlStation["UICCode"]
		station["Latitude"] = xmlStation["Lat"]
		station["Longitude"] = xmlStation["Lon"]

		if xmlStation["Synoniemen"] != None:
			synonymList = xmlStation["Synoniemen"]["Synoniem"]

			if type(synonymList) == list:
				station["Synonyms"] = synonymList
			else:
				station["Synonyms"] = [ synonymList ]
		
		stations.append(station)
	return stations

def getDepartures(station):
	"""
	Haalt alle vertrekkende treinen op van het opgegeven station.
	"""
	departures = []
	url = urlBuilder.buildURL("ActueleVertrekTijden", {"station": station})
	
	response = requests.get(url, auth = (config.username, config.password))
	xml = xmltodict.parse(response.text)

	checkForError(url, xml)

	for xmlDeparture in xml["ActueleVertrekTijden"]["VertrekkendeTrein"]:
		# De volgende waarden zijn altijd beschikbaar
		departure = {
			"RideNumber": xmlDeparture["RitNummer"],
			"DepartureTime": xmlDeparture["VertrekTijd"][11:16],
			"DepartureDate": xmlDeparture["VertrekTijd"][0:10],
			"Destination": xmlDeparture["EindBestemming"],
			"TrainType": xmlDeparture["TreinSoort"],
			"Transporter": xmlDeparture["Vervoerder"],
			"DeparturePlatform": xmlDeparture["VertrekSpoor"]["#text"],
			"DeparturePlatformChanged": xmlDeparture["VertrekSpoor"]["@wijziging"]	
		}

		# De volgende waarden zijn niet altijd beschikbaar
		if "VertrekVertraging" in xmlDeparture:
			departure["DepartureDelay"] = xmlDeparture["VertrekVertraging"]

		if "VertrekVertragingTekst" in xmlDeparture:
			departure["DepartureDelayText"] = xmlDeparture["VertrekVertragingTekst"]

		if "RouteTekst" in xmlDeparture:
			departure["RouteText"] = xmlDeparture["RouteTekst"]

		if "ReisTip" in xmlDeparture:
			departure["TravelTip"] = xmlDeparture["ReisTip"]

		if "Opmerkingen" in xmlDeparture:
			departure["Comments"] = xmlDeparture["Opmerkingen"] 

		departures.append(departure)
	return departures