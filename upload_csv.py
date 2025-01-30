import csv
import requests

# Replace with your GitHub info
GITHUB_TOKEN = "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"
REPO_OWNER = "hit3p48cy"
REPO_NAME = "Power-Platform-Solutions"

def create_issue(title, body, labels):
    url = f"https://api.github.com/repos/hit3p48cy/Power-Platform-Solutions/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"title": title, "body": body, "labels": labels.split(",")}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Read issues from CSV and create them in GitHub
with open("issue_final.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        result = create_issue(row["title"], row["body"], row["labels"])
        print(f"Issue created: {result.get('html_url', 'Error')}")

print("All issues imported!")
