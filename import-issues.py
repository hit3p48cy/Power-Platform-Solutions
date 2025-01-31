import csv
import requests
import Github, Issue, Project



GITHUB_TOKEN = "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"
REPO_OWNER = "hit3p48cy"
REPO_NAME = "Power-Platform-Solutions"

# Replace with your project details (if adding to a project)
PROJECT_NAME = "TaskManagement"

def main():
    # Authenticate with GitHub
    g = Github(GITHUB_TOKEN)

    # Get the repository
    repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

    # Get the project (if adding issues to a project)
    project = None
    projects = repo.get_projects()
    for proj in projects:
        if proj.name == PROJECT_NAME:
            project = proj
            break

    if not project:
        print(f"Project '{PROJECT_NAME}' not found.")
        return

    # Import issues

    with open("issue_csv_project.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            issue = repo.create_issue(
                title=row["title"],
                body=row["body"],
                labels=row["labels"]
            )
        print(f"Issue created: {issue.title} (#{issue.number})")

        # Add the issue to the project (optional)
        if project:
            project.create_card(content_id=issue.id, content_type="Issue")
            print(f"Issue added to project: {PROJECT_NAME}")

if __name__ == "__main__":
    main()
