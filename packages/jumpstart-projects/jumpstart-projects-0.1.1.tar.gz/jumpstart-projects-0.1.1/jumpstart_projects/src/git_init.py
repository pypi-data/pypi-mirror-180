import os
import urllib.request
import json

from jumpstart_projects.utils import execute_cmd, make_abs_path, color_print


def set_remote(project_path: str, remote_url: str):
    if ".git" not in os.listdir(project_path):
        color_print(f"$ Initializing a Git repository here {project_path}")
        git_init(project_path=project_path)

    if not remote_url.endswith(".git"):
        remote_url += ".git"

    color_print(f"$ Setting remote origin to {remote_url}")
    execute_cmd(f"git remote add origin {remote_url}", cwd=project_path)


def git_init(project_path: str):
    project_path = make_abs_path(project_path)
    if not os.path.exists(project_path):
        raise OSError("Project path is invalid")
    color_print(f"$ Initializing git repository here {project_path}")
    execute_cmd(cmd="git init", cwd=project_path)


def create_repository(
    project_path: str,
    repo_name: str,
    visibility: str = "private",
    pat: str = "GITHUBTOKEN",
    using_ssh: bool = False,
):
    """Requires a GitHub Personal Access Token (PAT) to be setup in the environment"""
    initialized_repository = False
    project_path = make_abs_path(project_path)
    if not os.path.exists(project_path):
        raise OSError(f"Project does not exist here {project_path}")

    url = f"https://api.github.com/user/repos"
    token = os.getenv(pat)
    if not token:
        raise OSError(f"No token {pat} found in the environment")

    payload = {
        "name": repo_name,
        "private": "true" if visibility == "private" else "false",
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    request = urllib.request.Request(
        url=url, data=json.dumps(payload).encode(), headers=headers
    )
    color_print(
        f"$ Creating a {visibility if visibility == 'private' else 'public'} repository for project {repo_name}"
    )
    try:
        with urllib.request.urlopen(request) as req:
            status_code, response = req.status, json.loads(req.read())
        if not status_code == 201:
            raise Exception(
                f"Returned status code \
                    {status_code} {response if status_code == 400 else ''}"
            )

        color_print(f"$ Repository created at {response['html_url']}")
        initialized_repository = True
    except Exception as e:
        color_print(f"$ Error occurred during creation of repository: {e}", info=False)

    if initialized_repository:
        remote_url = response["ssh_url"] if using_ssh else response["html_url"]
        set_remote(project_path=project_path, remote_url=remote_url)
