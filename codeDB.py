import os
import subprocess
import json
from gitScraper import Scraper

DBDIRECTORY: str = "db"
DATAFILE: str = "repositories.json"

class CREATEDB:
    def __init__(self, username: str) -> None:
        self.username = username
        self.base_url = "https://github.com/"
        scraper: Scraper = Scraper(self.username)
        self.repos, self.forked_repos = scraper.git_scrape()
        self.repo_data = []  # List to hold repository data

    def createdir(self):
        if not os.path.exists(DBDIRECTORY):
            os.makedirs(DBDIRECTORY)
        os.chdir(DBDIRECTORY)

    def cloning_repos(self):
        for repo in self.repos:
            repo_url: str = self.base_url + repo + ".git"
            print(f"Cloning {repo_url}\n")
            subprocess.run(["git", "clone", repo_url])
            self.store_repo_data(repo)

    def store_repo_data(self, repo: str):
        # Create a dictionary for the repository
        repo_info = {
            "username": self.username,
            "repo_name": repo.split('/')[-1],
            "repo_url": self.base_url + repo + ".git",
            "file_path": os.path.join(os.getcwd(), repo.split('/')[-1])
        }
        # Append the dictionary to the repo_data list
        self.repo_data.append(repo_info)

    def save_to_json(self):
        # Write the repository data to a JSON file
        with open(DATAFILE, 'w') as json_file:
            json.dump(self.repo_data, json_file, indent=4)
        print(f"Repository data saved to {DATAFILE}")

    def createDB(self):
        self.createdir()
        self.cloning_repos()
        self.save_to_json()
        print(f"Forked Repos: {[self.base_url + repo + '.git' for repo in self.forked_repos]}")

if __name__ == "__main__":
    username: str = input("Enter username: ")
    db: CREATEDB = CREATEDB(username)
    db.createDB()
