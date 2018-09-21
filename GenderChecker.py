import time
import requests

print("Coder: Mostafa M. Mead")
print("Github: Github/AimMead")
print("Facebook: FB/100010261237574")
print("")

def CheckToken(accessToken):
	validateUrl = 'https://graph.facebook.com/me/?access_token={}'.format(accessToken)
	if 'first_name' in str(requests.get(validateUrl).content):
		return True
	else:
		return False

def TokenGender(accessToken):
	checkUrl = 'https://graph.facebook.com/me/?fields=gender&access_token={}'.format(accessToken)
	checkReq = requests.get(checkUrl)
	checkJson = checkReq.json()
	gender = checkJson['gender']
	if gender == 'male':
		return True
	elif gender == 'female':
		return False

def main():
	with open(input("Enter Access Tokens Text: ")) as f:
		tokens = f.read().split("\n")
	for token in tokens:
		if CheckToken(token):
			gendFun = TokenGender(token)
			if gendFun:
				menFile = open('menTokens.txt' , 'a+')
				menFile.write('{}\n'.format(token))
				menFile.close()
				print("{}:Man".format(token))
			elif gendFun == False:
				womenFile = open('womenTokens.txt' , 'a+')
				womenFile.write('{}\n'.format(token))
				womenFile.close()
				print("{}:Woman".format(token))
			else:
				unknownFile = open('unknownTokens.txt' , 'a+')
				unknownFile.write('{}\n'.format(token))
				unknownFile.close()
				print("{}:Unknown".format(token))
		else:
			print("Invalid Access Token !")

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e)
		time.sleep(1000)
	else:
		print("Process Done Succesfully !")
		time.sleep(1000)