class NSException(Exception):
	pass

def checkForError(url, xml):
	error = "unknown"
	if "error" in xml:
		error = xml["error"]["message"]

		raise NSException("{} responded with an error: {}".format(url, error))