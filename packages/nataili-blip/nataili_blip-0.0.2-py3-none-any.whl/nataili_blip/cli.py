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
import time

import click
import PIL
from .model_manager import BlipModelManager
from .caption import Caption
from .util import logger


@click.command()
@click.option("--model_name", default="BLIP", type=click.Choice(["BLIP", "BLIP_Large"]), show_default=True)
@click.option("--precision", default="half", type=click.Choice(["half", "full"]), show_default=True)
@click.option("--gpu_id", default=0, show_default=True)
@click.option("--blip_image_eval_size", default=512, show_default=True)
@click.option("--sample", default=True, is_flag=True, show_default=True)
@click.option("--num_beams", default=3, show_default=True)
@click.option("--max_length", default=30, show_default=True)
@click.option("--min_length", default=10, show_default=True)
@click.option("--top_p", default=0.9, show_default=True)
@click.option("--repetition_penalty", default=1.0, show_default=True)
@click.argument("image_path", type=click.Path(exists=True))
def caption_image(
    image_path,
    model_name,
    precision,
    gpu_id,
    blip_image_eval_size,
    vit,
    sample,
    num_beams,
    max_length,
    min_length,
    top_p,
    repetition_penalty,
):
    mm = BlipModelManager()
    if model_name not in mm.available_models:
        logger.error(f"{model_name} not available")
        logger.info(f"Downloading {model_name}")
        mm.download_model(model_name)

    if model_name not in mm.loaded_models:
        tic = time.time()
        logger.info(f"Loading {model_name}")
        success = mm.load_blip(model_name, precision, gpu_id, blip_image_eval_size, vit)
        if not success:
            logger.error(f"Unable to load {model_name}")
            return
        toc = time.time()
        logger.info(f"Loading {model_name}: Took {toc-tic} seconds")

    start = time.time()

    blip = Caption(mm.loaded_models[model_name]["model"], mm.loaded_models[model_name]["device"])

    image = PIL.Image.open(image_path).convert("RGB")

    caption = blip(
        image,
        sample=sample,
        num_beams=num_beams,
        max_length=max_length,
        min_length=min_length,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
    )

    end = time.time()

    logger.info(f"Caption: {caption}")
    logger.info(f"Time: {end-start}")


if __name__ == "__main__":
    caption_image()
