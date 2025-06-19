import os
import requests
from pathlib import Path
from zipfile import ZipFile

# Dataset URLs and output names
datasets = [
    {
        "name": "Detection Dataset",
        "url": "https://zenodo.org/records/15642838/files/Dataset.zip?download=1",
        "filename": "detection-dataset.zip"
    },
    {
        "name": "Harvesting Classification Dataset",
        "url": "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/kjrsb7ztr9-1.zip",
        "filename": "harvesting-classification-dataset.zip"
    },
    {
        "name": "Expert Opinion Dataset",
        "url": "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/kk88rgfr55-1.zip",
        "filename": "expert-opinion-dataset.zip"
    }
]

def download_file(url: str, output_path: Path):
    print(f"Downloading from {url} -> {output_path.name}")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Saved: {output_path}")


def main():
    data_dir = Path("datasets")
    data_dir.mkdir(exist_ok=True)

    for dataset in datasets:
        output_path = data_dir / dataset["filename"]
        if not output_path.exists():
            download_file(dataset["url"], output_path)
        else:
            print(f"Already downloaded: {output_path.name}")

if __name__ == "__main__":
    main()
