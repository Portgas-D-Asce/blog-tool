import requests

url = "https://github.com/Portgas-D-Asce"

resp = requests.get(url)

print(resp.text.encode())


