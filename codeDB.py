from gitScraper import Scraper
import os
import subprocess

DBDIRECTORY: str = "db"

class CREATEDB:
    def __init__(self, username: str) -> None:
        global DBDIRECTORY
        self.username = username
        self.base_url =  "https://github.com/"
        scraper: Scraper = Scraper(self.username)
        self.repos = scraper.git_scrape()

    def createdir(self):
        if not os.path.exists(DBDIRECTORY):
            os.makedirs(DBDIRECTORY)
        os.chdir(DBDIRECTORY)

    def cloning_repos(self):
        for repo in self.repos:
            repo_url: str = self.base_url + repo + ".git"
            subprocess.run(["git", "clone", repo_url])

    def createDB(self):
        self.createdir()
        self.cloning_repos()

if __name__ == "__main__":
    username: str = input("Enter username: ")
    db: CREATEDB = CREATEDB(username)
    db.createDB()