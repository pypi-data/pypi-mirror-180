import os
import sys

from jumpstart_projects.utils import (
    color_print,
    create_folder,
    execute_cmd,
    make_abs_path,
)


def vscode_init(project_path: str, virtual_env_path: str, python: str):
    import json

    color_print("$ Initializing VsCode")
    try:
        create_folder(make_abs_path(os.path.join(project_path, ".vscode")))
    except OSError:
        color_print("Code settings already exists!")
    if os.path.exists(virtual_env_path):
        with open(os.path.join(project_path, ".vscode", "settings.json"), "w") as f:
            configs = {
                "python.defaultInterpreterPath": os.path.join(
                    virtual_env_path, "bin", python
                ),
            }
            f.write(json.dumps(configs, indent=2))

    open_code = f"code {project_path}"
    execute_cmd(open_code)


def main(
    project_path: str,
    *,
    create_env: bool = True,
    python: str = "python3.10",
    virtual_env_path: str = None,
    venv_options: list = None,
    code: bool = False,
):
    project_name = (
        project_path.rstrip("/").split("/")[-1] if "/" in project_path else project_path
    )
    virtual_env_path = (
        virtual_env_path if virtual_env_path else f"~/virtualenvs/{project_name}"
    )
    project_path, virtual_env_path = make_abs_path(project_path, virtual_env_path)
    if project_path == virtual_env_path:
        raise ValueError("Project path and environment path can't be same")

    if not create_env:
        color_print(
            f"$ Creating project direcotry: {project_path} and exiting",
        )
        create_folder(path=project_path)
        sys.exit(0)

    color_print(f"$ Initializing project and environment")

    create_folder(project_path)

    create_env_cmd = f"{python} -m venv {virtual_env_path} {' '.join(venv_options) if venv_options else ''}"
    return_code = execute_cmd(create_env_cmd)
    if return_code:
        color_print(
            f"$ {create_env_cmd} failed with return code {return_code}", info=False
        )
        sys.exit(return_code)

    if code:
        vscode_init(
            project_path=project_path,
            virtual_env_path=virtual_env_path,
            python=python,
        )
