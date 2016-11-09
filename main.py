import nsapi

from requests.exceptions import ConnectionError
from nsapi.errorHandling import NSException
from nsapi import stations

try:
	for i in stations.getStations():
		print(i["Names"]["Long"])
		for j, v in i.items():
			print("\t", j, v)
	#print(stations.getDepartures("Utrecht Centraal"))
except ConnectionError as e:
	print("Je bent offline!")
except NSException as e:
	print(str(e))