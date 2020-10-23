import json
import getpass

class Credentials:

	# @staticmethod
	# def getUserFor(service):
	# 	with open("secret", "r") as json_file:
	# 		data = json.load(json_file)
	# 		self.service = service
	# 		print(data[service])

	@staticmethod
	def getPassword():
		username = input("Inser Username: ")
		pwd = getpass.getpass("Enter Password: ")
		return {'username': username, 'password': pwd} 


creds = Credentials.getPassword()
