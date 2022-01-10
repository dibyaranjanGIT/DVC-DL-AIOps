from src.utils.all_utils import read_config,create_directory
import argparse
import pandas as pd
import os
import shutil
from tqdm import tqdm

def copy_file(source_path, destination_path):
    list_file = os.listdir(source_path)
    N = len(list_file)

    for file in tqdm(list_file, total=N, desc=f"copying file .."):
        src = os.path.join(source_path, file)
        dest = os.path.join(destination_path, file)
        shutil.copy(src, dest)

def get_data(config_path):
    config = read_config(config_path)

    source_data_dir = config["source_data_paths"]
    local_data_dir = config["data_paths"]

    for source_data, local_data in zip(source_data_dir, local_data_dir):
        create_directory(local_data)
        copy_file(source_data, local_data)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)
