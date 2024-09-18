import requests

url = "https://ekantipur.com/"

response = requests.get(url)
print(response.text)
