import nsapi

from requests.exceptions import ConnectionError
from nsapi.errorHandling import NSException
from nsapi import stations

stationsList = None

def updateStations():
	global stationsList
	stationsList = stations.getStations()

def search(keyword):
	response = []

	for i in  stationsList:
		if keyword.lower() in i["Names"]["Long"].lower():
			response.append(i)

	return response


# updateStations()

# print(search("utrecht"))

# try:
# 	for i in stations.getStations():
# 		print(i["Names"]["Long"])
# 		for j, v in i.items():
# 			print("\t", j, v)
# #	print(stations.getDepartures("Utrecht Centraal"))
# except ConnectionError as e:
# 	print("Je bent offline!")
# except NSException as e:
# 	print(str(e))