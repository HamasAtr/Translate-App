import requests

url = "https://text-translator2.p.rapidapi.com/translate"
try:
	
	with open("contry-name.txt", "r") as f:
		lines = f.readlines()

	contrydict = {}

	for line in lines:
		try:
			parsed = line.split('\t')
			print(parsed[1])
		except Exception as e:
			print("These languages available are")

	inp = input("\nThese languages are available. \nEnter text you want to translate:- ")
	inp.replace(" ", "%20")
	FirstLang = input("\nEnter the current language code you that you want to translate:- ")
	SecondLang = input("\nEnter language code that you want to translate- ")
except:
	print("Invalid Language code")


payload = f"source_language={FirstLang}&target_language={SecondLang}&text={inp}%3F"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "Your-Api-Key",
	"X-RapidAPI-Host": "Your-Api-Key"
}

response = requests.request("POST", url, data=payload, headers=headers)
datas = response.json()
try: 
	b = datas['data']
	print(f"\n\nTranslated text is:- \n  {b}")
except:
	print("Currently Unavailable.")
