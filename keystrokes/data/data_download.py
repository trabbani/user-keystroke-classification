from keystrokes.data.download_utils import download_data
from keystrokes.utils.path_utils import DATA_URL, ZIP_FILEPATH


if __name__ == "__main__":
    download_data(DATA_URL, ZIP_FILEPATH)
