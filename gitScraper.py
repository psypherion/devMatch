"""
Scraping Github repositories using a profile name: 
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from typing import Any, AnyStr
profile: str = input("Enter profile name: ")

base_url: str = "http://github.com/"+profile+"?tab=repositories"

response: Any = requests.get(base_url)

soup = BeautifulSoup(response.content, "html.parser")

pattern: str = r'"\/psypherion\/[\w-]+\" itemprop=\"name codeRepository'

links: list = [link.split(" ")[0] for link in re.findall(pattern, str(soup))]

print(links)

