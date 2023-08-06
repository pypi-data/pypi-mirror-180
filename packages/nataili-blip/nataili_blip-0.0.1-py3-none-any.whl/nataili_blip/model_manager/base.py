# This file is part of nataili_blip ("Homepage" = "https://github.com/Sygil-Dev/nataili_blip").

# Copyright 2022 hlky and Sygil-Dev
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import hashlib
import json
import os
import requests
from tqdm import tqdm
import git
import shutil
from ..util.logger import logger
from pathlib import Path
import sys

if sys.version_info < (3, 9):
    # importlib.resources either doesn't exist or lacks the files()
    # function, so use the PyPI version:
    import importlib_resources
else:
    # importlib.resources has files(), so use that:
    import importlib.resources as importlib_resources


class ModelManager:
    def __init__(self):
        self.path = f"{Path.home()}/.cache/nataili/"
        self.models = {}
        self.available_models = []
        self.loaded_models = {}
        self.pkg = importlib_resources.files("nataili_blip")

    def init(self):
        self.models = json.loads((self.pkg / "models.json").read_text())
        models_available = []
        for model in self.models:
            if self.check_available(self.get_model_files(model)):
                models_available.append(model)
        self.available_models = models_available

    def get_model_files(self, model_name):
        return self.models[model_name]["config"]["files"]

    def get_model_download(self, model_name):
        return self.models[model_name]["config"]["download"]

    def get_available_models(self):
        return self.available_models

    def get_loaded_models(self):
        return self.loaded_models

    def get_loaded_models_names(self):
        return list(self.loaded_models.keys())

    def get_loaded_model(self, model_name):
        return self.loaded_models[model_name]

    def is_model_loaded(self, model_name):
        return model_name in self.loaded_models

    def unload_model(self, model_name):
        if model_name in self.loaded_models:
            del self.loaded_models[model_name]
            return True
        return False

    def unload_all_models(self):
        for model in self.loaded_models:
            del self.loaded_models[model]
        return True

    def load_model(self, model_name="", precision="half", gpu_id=0):
        if model_name not in self.available_models:
            return False
        if self.models[model_name]["type"] == "unknown":
            pass
        else:
            return False

    def validate_model(self, model_name, skip_checksum=False):
        files = self.get_model_files(model_name)
        for file_details in files:
            if not self.check_file_available(file_details["path"]):
                return False
            if not skip_checksum and not self.validate_file(file_details):
                return False
        return True

    def validate_file(self, file_details):
        if "md5sum" in file_details:
            full_path = f"{self.path}/{file_details['path']}"
            logger.debug(f"Getting md5sum of {full_path}")
            with open(full_path, "rb") as file_to_check:
                file_hash = hashlib.md5()
                while True:
                    chunk = file_to_check.read(8192)  # Changed just because it broke pylint
                    if not chunk:
                        break
                    file_hash.update(chunk)
            if file_details["md5sum"] != file_hash.hexdigest():
                return False
        return True

    def check_file_available(self, file_path):
        full_path = f"{self.path}/{file_path}"
        return os.path.exists(full_path)

    def check_available(self, files):
        available = True

        for file in files:
            if not self.check_file_available(file["path"]):
                available = False
        return available

    def download_file(self, url, file_path):
        # make directory
        full_path = f"{self.path}/{file_path}"
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        pbar_desc = full_path.split("/")[-1]
        r = requests.get(url, stream=True, allow_redirects=True)
        with open(full_path, "wb") as f:
            with tqdm(
                # all optional kwargs
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                miniters=1,
                desc=pbar_desc,
                total=int(r.headers.get("content-length", 0)),
            ) as pbar:
                for chunk in r.iter_content(chunk_size=16 * 1024):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))

    def download_model(self, model_name):
        if model_name in self.available_models:
            logger.info(f"{model_name} is already available.")
            return True
        download = self.get_model_download(model_name)
        files = self.get_model_files(model_name)
        for i in range(len(download)):
            file_path = (
                f"{download[i]['file_path']}/{download[i]['file_name']}"
                if "file_path" in download[i]
                else files[i]["path"]
            )

            if "file_url" in download[i]:
                download_url = download[i]["file_url"]
            if "file_name" in download[i]:
                download_name = download[i]["file_name"]
            if "file_path" in download[i]:
                download_path = download[i]["file_path"]

            if "manual" in download[i]:
                logger.warning(
                    f"The model {model_name} requires manual download from {download_url}. "
                    f"Please place it in {download_path}/{download_name} then press ENTER to continue..."
                )
                input("")
                continue
            # TODO: simplify
            if "file_content" in download[i]:
                file_content = download[i]["file_content"]
                logger.info(f"writing {file_content} to {file_path}")
                # make directory download_path
                os.makedirs(download_path, exist_ok=True)
                # write file_content to download_path/download_name
                with open(os.path.join(download_path, download_name), "w") as f:
                    f.write(file_content)
            elif "symlink" in download[i]:
                logger.info(f"symlink {file_path} to {download[i]['symlink']}")
                symlink = download[i]["symlink"]
                # make directory symlink
                os.makedirs(download_path, exist_ok=True)
                # make symlink from download_path/download_name to symlink
                os.symlink(symlink, os.path.join(download_path, download_name))
            elif "git" in download[i]:
                logger.info(f"git clone {download_url} to {file_path}")
                # make directory download_path
                os.makedirs(file_path, exist_ok=True)
                git.Git(file_path).clone(download_url)
                if "post_process" in download[i]:
                    for post_process in download[i]["post_process"]:
                        if "delete" in post_process:
                            # delete folder post_process['delete']
                            logger.info(f"delete {post_process['delete']}")
                            try:
                                shutil.rmtree(post_process["delete"])
                            except PermissionError as e:
                                logger.error(
                                    f"[!] Something went wrong while deleting the `{post_process['delete']}`. "
                                    "Please delete it manually."
                                )
                                logger.error("PermissionError: ", e)
            else:
                if not self.check_file_available(file_path) or model_name in self.tainted_models:
                    logger.debug(f"Downloading {download_url} to {file_path}")
                    self.download_file(download_url, file_path)
        if not self.validate_model(model_name):
            return False
        self.init()
        return True

    def download_all_models(self):
        for model in self.get_filtered_model_names(download_all=True):
            if not self.check_model_available(model):
                logger.init(f"{model}", status="Downloading")
                self.download_model(model)
            else:
                logger.info(f"{model} is already downloaded.")
        return True

    def check_model_available(self, model_name):
        if model_name not in self.models:
            return False
        return self.check_available(self.get_model_files(model_name))
