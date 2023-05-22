import os
import requests
from tqdm import tqdm

def download_data(url, target_path):
    # Deduce the target_folder from the target_path
    target_folder = os.path.dirname(target_path)

    # Create target directory if it does not exist
    os.makedirs(target_folder, exist_ok=True)
    
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        response = requests.get(url, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

        with open(target_path, 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")

