import sys
import tomli
import os
import argparse
from dataclasses import dataclass
import subprocess


@dataclass
class State:
    action: str
    branch: str
    service: str
    stack_name: str
    config: dict
    docker_dir: str = ""
    stack_file: str = "stack.yml"

    def get_dockerfile_path(self) -> str:
        return f'{os.getcwd()}/{self.config["docker_dir"]}/{self.service}/Dockerfile'

    def get_stack_path(self) -> str:
        return f'{os.getcwd()}/{self.config["docker_dir"]}/stack.yml'

    def get_image_tag(self):
        return f"127.0.0.1:5000/{self.service}"

    def run_build(self):
        # docker build  -f <path_para_dockerfile> -t <tag da imagem> <diretorio de contexto>
        dockerfile_path: str = self.get_dockerfile_path()
        os.system(f"docker build -f {dockerfile_path} -t {self.get_image_tag()} .")

    def run_deploy(self):
        # docker stack deploy -c docker/production/stack.yml dashboard
        stack_path: str = self.get_stack_path()
        os.system(f"docker stack deploy -c {stack_path} {self.stack_name}")


def get_config():
    dir_path: str = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/config.toml", mode="rb") as fp:
        config = tomli.load(fp)
    return config


def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        description="Install a stack file on docker swarm."
    )
    parser.add_argument(
        "--command", type=str, help="wich docker command execute [build, deploy]"
    )
    parser.add_argument(
        "--branch",
        type=str,
        dest="branch",
        help="the branch to clone inside Dockerfile",
    )
    parser.add_argument(
        "--service",
        type=str,
        dest="service",
        help="the stack service to build image",
    )
    parser.add_argument(
        "--stack",
        type=str,
        dest="stack_name",
        help="the cluster stack name",
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_cli_arguments()
    config = get_config()
    state = State(args.command, args.branch, args.service, args.stack_name, config)
    state.run_build()


if __name__ == "__main__":
    main()
