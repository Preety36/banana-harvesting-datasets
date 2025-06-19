{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import requests\n",
    "import zipfile\n",
    "\n",
    "# Correct dataset URLs with provided DOIs\n",
    "datasets = {\n",
    "    \"detection\": \"https://zenodo.org/record/15642838/files/banana_detection_dataset.zip?download=1\",  \n",
    "    \"classification\": \"https://data.mendeley.com/public-files/datasets/kjrsb7ztr9/1/files/banana_harvest_classification.zip?download=1\",  # Harvesting dataset\n",
    "    \"expert_opinion\": \"https://data.mendeley.com/public-files/datasets/kjrsb7ztr9/1/files/banana_harvest_classification.zip?download=1\"  # Expert opinion dataset\n",
    "}\n",
    "\n",
    "def download_and_extract(name, url, output_dir='datasets'):\n",
    "    os.makedirs(output_dir, exist_ok=True)\n",
    "    local_zip = os.path.join(output_dir, f\"{name}.zip\")\n",
    "    \n",
    "    print(f\"Downloading {name} dataset...\")\n",
    "    with requests.get(url, stream=True) as r:\n",
    "        with open(local_zip, 'wb') as f:\n",
    "            for chunk in r.iter_content(chunk_size=8192):\n",
    "                f.write(chunk)\n",
    "\n",
    "    print(f\"Extracting {name} dataset...\")\n",
    "    with zipfile.ZipFile(local_zip, 'r') as zip_ref:\n",
    "        zip_ref.extractall(os.path.join(output_dir, name))\n",
    "    \n",
    "    print(f\"{name} dataset ready at {os.path.join(output_dir, name)}\")\n",
    "    os.remove(local_zip)  # optional: delete zip after extraction to save space\n",
    "\n",
    "# Run this to download all datasets\n",
    "for name, url in datasets.items():\n",
    "    download_and_extract(name, url)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
