import subprocess
import shlex
import os


def color_print(message, info=True):
    if info:
        print(f"\033[1;40m{message}", "\033[1;0m")
    else:
        print(f"\033[1;31m{message}", "\033[1;0m")


def make_abs_path(*paths):
    out = []
    for path in paths:
        if not os.path.isabs(path):
            path = os.path.abspath(os.path.expanduser(path))
        out.append(path)

    if len(out) == 1:
        return out[0]

    return out


def create_folder(path: str):
    """Accepts absolute path only"""
    if not os.path.isabs(path):
        OSError("Can't create a folder with reletive paths")

    if os.path.exists(path):
        raise OSError(f"Directory already exists at {path}")
    else:
        os.mkdir(path)


def execute_cmd(cmd: str, cwd: str = None) -> bytes:
    return subprocess.check_output(shlex.split(cmd), cwd=cwd, universal_newlines=True)
