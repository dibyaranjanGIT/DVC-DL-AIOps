from src.utils.all_utils import read_config,create_directory
import argparse
import pandas as pd
import os

def get_data(config_path):
    config = read_config(config_path)

    source_data_dir = config["source_data_paths"]
    local_data_dir = config["data_paths"]

    for source_data, local_data in zip(source_data_dir, local_data_dir):
        create_directory(local_data)
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configuration/config.yaml")
    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)
