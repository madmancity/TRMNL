from bs4 import BeautifulSoup
import requests
import re
from test import regex
url = 'https://flightaware.com/live/flight/UAE523'
r = requests.get(url)
print(r.text)
