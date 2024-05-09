import os
import requests

def download_model(url, save_path):
    response = requests.get(url)
    if not save_path.endswith('.pth'):
        save_path = os.path.join(save_path, url.split("/")[-1])

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Model downloaded successfully.")
    else:
        print("Failed to download the model.")

    return save_path