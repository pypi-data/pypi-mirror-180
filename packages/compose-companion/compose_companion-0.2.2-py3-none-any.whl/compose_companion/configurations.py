import configparser
from pathlib import Path
from os import path as ospath
import typer
import yaml_env_var_parser as yaml
from dotenv import load_dotenv
from rich import print
from rich.console import Console

err_console = Console(stderr=True)


load_dotenv()


class Configurations:
    _instance = None

    current_path = Path(__file__).parent.resolve()

    config_keys = ["companion_file", "compose_file"]
    config_parser = configparser.ConfigParser()
    config_file = f"{current_path}/config.cfg"

    scripts = dict()
    services = []
    volumes = dict()
    _companion_file = ""
    _compose_file = ""

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # initialization
            cls._load_config_file(cls._instance)
            cls._load_compose_files(cls._instance)

        return cls._instance

    @staticmethod
    def _resolve_path(value):
        return Path(ospath.expandvars(value.replace('~', '$HOME'))).resolve()

    def _save(self):
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)

    def get_config(self, key: str):
        return self.config_parser["DEFAULT"][key]

    def set_config(self, key: str, value: str):
        self.config_parser["DEFAULT"][key] = value
        self._save()

    @property
    def companion_file(self) -> str:
        try:
            self._companion_file = self.get_config("companion_file")
        except KeyError:
            self.set_config("companion_file", "")
            self._companion_file = ""
        return self._companion_file

    @companion_file.setter
    def companion_file(self, value: str) -> None:
        if not value:
            self._companion_file = ""
        else:
            self._companion_file = f"{self._resolve_path(value)}"
        self.set_config("companion_file", self._companion_file)

    @property
    def compose_file(self) -> str:
        try:
            self._compose_file = self.get_config("compose_file")
        except KeyError:
            self.set_config("compose_file", "")
            self._compose_file = ""
        return self._compose_file

    @compose_file.setter
    def compose_file(self, value: str) -> None:
        if not value:
            self._compose_file = ""
        else:
            print(value)
            self._compose_file = f"{self._resolve_path(value)}"
        self.set_config("compose_file", self._compose_file)

    def _load_config_file(self):
        try:
            with open(self.config_file, "r") as file:
                self.config_parser.read_file(file)
        except FileNotFoundError:
            self._save()

    def _request_compose_file(self):
        local_compose_file_yaml = Path("docker-compose.yaml").resolve()
        local_compose_file_yml = Path("docker-compose.yml").resolve()

        if local_compose_file_yaml.is_file():
            self.compose_file = str(local_compose_file_yaml)
            return
        elif local_compose_file_yml.is_file():
            self.compose_file = str(local_compose_file_yml)
            return

        compose_file_input = typer.prompt(
            "Please informe the path to your docker compose file (including filename)"
        )

        compose_file_path = self._resolve_path(compose_file_input)
        if not compose_file_path.is_file():
            err_console.print("The informed path is invalid.\n")
            return

        self.compose_file = str(compose_file_path)
        print("Your file path has been saved!\n")

    def _request_companion_file(self):
        local_companion_file_yaml = Path("compose-companion.yaml").resolve()
        local_companion_file_yml = Path("compose-companion.yml").resolve()

        if local_companion_file_yaml.is_file():
            self.companion_file = str(local_companion_file_yaml)
            return
        if local_companion_file_yml.is_file():
            self.companion_file = str(local_companion_file_yml)
            return
        elif Path(self.compose_file).is_file():
            use_compose = typer.confirm(
                "I didn't find your companion file, but I do have your docker-compose file. Would you like to use it for your companion scripts?"
            )
            if use_compose:
                self.companion_file = self.compose_file
                return

        companion_file_input = typer.prompt(
            "Please informe the path to your companion scripts file (including filename)"
        )

        companion_file_path = self._resolve_path(companion_file_input)
        if not companion_file_path.is_file():
            err_console.print("The informed path is invalid.\n")
            return
        self.companion_file = str(companion_file_path)
        print("Your file path has been saved!\n")

    def _load_compose_files(self):
        if not self.compose_file or not Path(self.compose_file).is_file():
            self._request_compose_file()
            self._load_compose_files()
            return

        if not self.companion_file or not Path(self.companion_file).is_file():
            self._request_companion_file()
            self._load_compose_files()
            return

        try:
            with open(self.compose_file, "r") as file:
                parsed = yaml.load(file)                
                if parsed:
                    services_dict = dict(parsed).get("services", {})
                    volumes_dict = dict(parsed).get("volumes", {})

                self.services = list(services_dict.keys())
                for service_name in self.services:
                    self.volumes[service_name] = []

                volumes_list = list(volumes_dict.keys())
                for key, value in services_dict.items():
                    service_vols = value.get("volumes", [])
                    for service_vol in service_vols:
                        if service_vol.split(":")[0] in volumes_list:
                            self.volumes[key].append({'host': service_vol.split(":")[0], 'container': service_vol.split(":")[1]})

                
        except (FileNotFoundError, IsADirectoryError) as err:
            err_console.print("Docker Compose file path is invalid")
            self.compose_file = ""
            self._load_compose_files()
            return
        except ValueError as err:
            compose_file_dir = Path(self.compose_file).parent.resolve()
            dotenv_file_path = Path(f"{compose_file_dir}/.env")
            if dotenv_file_path.is_file():
                load_dotenv(dotenv_file_path)
                self._load_compose_files()
                return
        except TypeError as err:
            err_console.print(
                "Invalid syntax somewhere on your docker compose file. Please make sure you have a valid yaml file!"
            )
            err_console.print(
                "To check or change the current file path run compose config."
            )

        try:
            with open(self.companion_file, "r") as file:
                parsed = yaml.load(file)
                if parsed:
                    self.scripts = dict(parsed)
        except (FileNotFoundError, IsADirectoryError) as err:
            err_console.print("Scripts file path is invalid")
            self.companion_file = ""
            self._load_compose_files()
            return
        except ValueError as err:
            companion_file_dir = Path(self.companion_file).parent.resolve()
            dotenv_file_path = Path(f"{companion_file_dir}/.env")
            if dotenv_file_path.is_file():
                load_dotenv(dotenv_file_path)
                self._load_compose_files()
                return
        except TypeError as err:
            err_console.print(
                "Invalid syntax somewhere on your scripts file. Please make sure you have a valid yaml file!"
            )
            err_console.print(
                "To check or change the current file path run compose config."
            )
