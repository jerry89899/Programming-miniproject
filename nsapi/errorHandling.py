class NSException(Exception):
	pass

def checkForError(url, xml):
	"""
	Kijkt in de xml voor een aangekondigde error.

	Als er een error is gevonden, dan wordt die als exception geraised.
	"""
	error = "unknown"
	if "error" in xml:
		error = xml["error"]["message"]

		raise NSException("{} responded with an error: {}".format(url, error))