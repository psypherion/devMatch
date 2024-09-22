import requests
from bs4 import BeautifulSoup
import re
from typing import List

class Scraper:
    def __init__(self, profile: str) -> None:
        self.profile = profile
        self.base_url = f"http://github.com/{self.profile}"
        self.repos_url = f"{self.base_url}?tab=repositories"

    def git_scrape(self) -> List[str]:
        response = requests.get(self.repos_url)
        if response:
            soup = BeautifulSoup(response.content, "html.parser")

            # Pattern to find repositories
            repo_pattern = r'\/' + re.escape(self.profile) + r'\/[\w-]+\" itemprop=\"name codeRepository'
            repos = [re.sub(r'^"|"$', '', link.split(" ")[0]) for link in re.findall(repo_pattern, str(soup))]

            # Pattern to find forked repositories
            forked_pattern = r'Forked from <a class=\"Link--muted Link--inTextBlock\" href=\"/[^\">]+\">([^<]+)</a>'
            forked_repos = [match.split('/')[-1] for match in re.findall(forked_pattern, str(soup))]

            # Remove the forked repositories from the main list
            repos = [repo for repo in repos if repo.split('/')[-1] not in forked_repos]

            return repos, forked_repos
        return []

if __name__ == "__main__":
    profile: str = input("Enter profile name: ")
    scraper = Scraper(profile)
    print("Repositories:", scraper.git_scrape())
