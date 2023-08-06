import argparse


def add_project_init_commands(project_init: argparse.ArgumentParser):
    project_init.add_argument("project_path", help="Path to the project")
    project_init.add_argument(
        "--no-new-env",
        help="When passed no new environment is created",
        action="store_false",
        dest="create_env",
    )
    project_init.add_argument(
        "--python",
        help="Python version to be used in the new environment",
        default="python3.10",
    )
    project_init.add_argument(
        "--env-path", help="Path to new environment", default=None
    )
    project_init.add_argument(
        "--venv-options",
        help="Options passed to venv",
        type=lambda name: "--" + name,
        nargs="+",
    )
    project_init.add_argument(
        "--code",
        help="Launch and initialize code with the new environment created",
        action="store_true",
    )


def add_create_remote_repository_commands(
    create_remote_repository: argparse.ArgumentParser,
):
    create_remote_repository.add_argument(
        "--project-path", help="Path to project", type=str
    )
    create_remote_repository.add_argument(
        "--repo-name",
        help="Name of the remote repository",
        type=str,
        required=True,
    )
    create_remote_repository.add_argument(
        "--visibility",
        choices=["private", "public"],
        help="Visibility status of the repository",
        required=False,
        default="private",
    )
    create_remote_repository.add_argument(
        "--pat",
        required=False,
        default="GITHUBTOKEN",
        help="Environment variable name to pick up PAT from,",
    )
    create_remote_repository.add_argument(
        "--using-ssh",
        required=False,
        default=False,
        action="store_true",
        help="Set remote using ssh or https",
    )


def cli():
    parser = argparse.ArgumentParser(
        prog="Jumpstart",
        description="Jumpstart all project requirements.",
        epilog="That's how to use jumpstart",
    )
    subparser = parser.add_subparsers(dest="command")
    project_init = subparser.add_parser(
        "project-init", help="Set up commands to jumpstart project settings"
    )
    create_remote_repository = subparser.add_parser(
        "create-remote-repository", help="Utility for creating remote repository"
    )
    add_project_init_commands(project_init=project_init)
    add_create_remote_repository_commands(
        create_remote_repository=create_remote_repository
    )

    args = parser.parse_args()
    if args.command == "project-init":
        from jumpstart_projects.src.project_init import main

        main(
            project_path=args.project_path,
            create_env=args.create_env,
            python=args.python,
            virtual_env_path=args.env_path,
            venv_options=args.venv_options,
            code=args.code,
        )

    elif args.command == "create-remote-repository":
        from jumpstart_projects.src.git_init import create_repository

        create_repository(
            project_path=args.project_path,
            repo_name=args.repo_name,
            visibility=args.visibility,
            pat=args.pat,
            using_ssh=args.using_ssh,
        )
