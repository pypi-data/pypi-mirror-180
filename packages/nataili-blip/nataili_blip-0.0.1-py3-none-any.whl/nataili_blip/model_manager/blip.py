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
import sys
from pathlib import Path

if sys.version_info < (3, 9):
    # importlib.resources either doesn't exist or lacks the files()
    # function, so use the PyPI version:
    import importlib_resources
else:
    # importlib.resources has files(), so use that:
    import importlib.resources as importlib_resources

import torch

from ..util.blip import blip_decoder
from ..util.logger import logger
from .base import ModelManager


class BlipModelManager(ModelManager):
    def __init__(self):
        super().__init__()
        self.path = f"{Path.home()}/.cache/nataili/blip"
        self.models = {}
        self.available_models = []
        self.loaded_models = {}
        self.pkg = importlib_resources.files("nataili_blip")
        self.init()

    def load_blip(
        self,
        model_name="",
        precision="half",
        gpu_id=0,
        blip_image_eval_size=512,
        vit="large",
    ):
        # vit = 'base' or 'large'
        vit = "base" if model_name == "BLIP" else "large"
        model_path = self.get_model_files(model_name)[0]["path"]
        model_path = f"{self.path}/{model_path}"
        device = torch.device(f"cuda:{gpu_id}" if torch.cuda.is_available() else "cpu")
        logger.info(f"Loading model {model_name} on {device}")
        logger.info(f"Model path: {model_path}")
        with importlib_resources.as_file(self.pkg / "med_config.json") as med_config:
            logger.info(f"Med config path: {med_config}")
            model = blip_decoder(
                pretrained=model_path,
                med_config=med_config,
                image_size=blip_image_eval_size,
                vit=vit,
            )
        model = model.eval()
        model.to(device)
        model = model if precision == "full" or device.type == "cpu" else model.half()
        self.loaded_models[model_name] = {"model": model, "device": device}
        return True
