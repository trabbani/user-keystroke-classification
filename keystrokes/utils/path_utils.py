from pathlib import Path
from keystrokes.utils.config_utils import get_config


def get_data_folder():
    """Returns the data folder path. If not specified in config, defaults to working_directory / data."""
    config = get_config()

    data_folder_path = config.get("data_folder_path")
    if data_folder_path:
        return Path(data_folder_path).expanduser()

    working_directory = config.get("working_directory")
    default_data_folder_path = Path(working_directory).expanduser() / "data"
    default_data_folder_path.mkdir(
        parents=True, exist_ok=True
    )  # Ensure the directory exists

    return default_data_folder_path


def get_specific_data_folder(subdirectory):
    """Returns the path to a specific subdirectory within the main data folder."""
    data_folder_path = get_data_folder()
    specific_data_folder_path = data_folder_path / subdirectory
    specific_data_folder_path.mkdir(
        parents=True, exist_ok=True
    )  # Ensure the directory exists

    return specific_data_folder_path


ZIP_FILEPATH = get_specific_data_folder("raw") / get_config()["keystrokes_data_zipfile"]
DATA_URL = get_config()["data_url"]

DATA_PREPROCESSED_FOLDER = get_specific_data_folder("preprocessed")
ARTIFACTS_FOLDER = get_specific_data_folder("artifacts")
