"""
Scraping Github repositories using a profile name: 
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from typing import Any, AnyStr
class Scraper:
    def __init__(self, profile) -> None:
        self.profile = profile
        self.base_url =  "http://github.com/"+self.profile
        self.repos = self.base_url+"?tab=repositories"

    def git_scrape(self) -> list:
        response = requests.get(self.repos)
        if response:
            soup = BeautifulSoup(response.content, "html.parser")
            pattern = r'"\/psypherion\/[\w-]+\" itemprop=\"name codeRepository'
            links = [re.sub(r'^"|"$', '',link.split(" ")[0])
                    for link in re.findall(pattern, str(soup))]
            return links

if __name__ == "__main__":
    profile: str = input("Enter profile name: ")
    scraper = Scraper(profile)
    print(scraper.git_scrape())
