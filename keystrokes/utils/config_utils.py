import os
from pathlib import Path
import yaml


class Config:
    DEFAULT_CONFIG_FILE = "config.yaml"
    DEFAULT_DATA_URL = "https://userinterfaces.aalto.fi/136Mkeystrokes/data/Keystrokes.zip"
    DEFAULT_KEYSTROKES_DATA_ZIPFILE = "data.zip"
    DEFAULT_WORKING_DIRECTORY = "~/.keystrokes"

    def __init__(self, config_file=None):
        self.config_file = config_file or self.DEFAULT_CONFIG_FILE
        self.config = self._load_from_file()

    def _load_from_file(self):
        """Load configuration from the yaml file."""
        config_path = self._get_config_file_path()
        if not config_path.exists():
            if self.config_file != self.DEFAULT_CONFIG_FILE:
                raise FileNotFoundError(f"No configuration file found at {config_path}")
            else:
                self._create_default_config_file(config_path)
        with open(config_path, "r") as file:
            config_data = yaml.safe_load(file)
        return config_data

    def _get_config_file_path(self):
        """Retrieve the path to the configuration file."""
        working_folder = os.environ.get('KEYSTROKES_WORKING_FOLDER')
        if working_folder is None:
            home_dir = Path("~").expanduser()
            working_folder = home_dir / ".keystrokes"
        config_path = Path(working_folder) / "configs" / self.config_file
        return config_path

    def _create_default_config_file(self, config_path):
        """Create a default configuration file if none exists."""
        config_path.parent.mkdir(parents=True, exist_ok=True)
        default_config = {
            "data_url": self.DEFAULT_DATA_URL,
            "keystrokes_data_zipfile": self.DEFAULT_KEYSTROKES_DATA_ZIPFILE,
            "working_directory": self.DEFAULT_WORKING_DIRECTORY
        }
        with open(config_path, "w") as file:
            yaml.dump(default_config, file)


def get_config(config_file=None):
    """Retrieve configuration."""
    return Config(config_file).config
