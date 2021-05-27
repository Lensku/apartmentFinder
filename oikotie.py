import requests
from bs4 import BeautifulSoup

url = "https://asunnot.oikotie.fi/myytavat-asunnot"
parameters = {
    "pagination": 1,
    "locations": "Helsinki",
}
res = requests.get(url, params=parameters)
soup = BeautifulSoup(res.content, "html.parser")
