import config

def setUsername(newUsername):
	"""
	Verandert de gebruikte username voor HTTP authorizatie.

	Gebruik config.reconfigure() om het door te voeren.
	"""
	config.username = newUsername
	config.reconfigure()

def setPassword(newPassword):
	"""
	Verandert de gebruikte password voor HTTP authorizatie.

	Gebruik config.reconfigure() om het door te voeren.
	"""
	config.password = newPassword
	config.reconfigure()