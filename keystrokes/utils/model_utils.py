import requests
from joblib import load
from urllib.parse import urlparse
import tempfile


def load_model(location):
    # If the location is a URL, download the model
    if urlparse(location).scheme in ["http", "https"]:
        response = requests.get(location)

        if response.status_code == 200:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=True) as tmp:
                tmp.write(response.content)
                tmp.seek(0)
                print("Model downloaded successfully.")

                # Load the model from the temporary file
                model = load(tmp.name)
        else:
            raise ValueError(f"Failed to download the model from {location}")
    else:
        # If the location is a file path, load the model directly
        model = load(location)

    return model
