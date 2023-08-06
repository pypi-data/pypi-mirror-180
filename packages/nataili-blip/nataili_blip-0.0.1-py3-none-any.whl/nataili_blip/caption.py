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
import torch
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode

from .util import performance


class Caption:
    def __init__(self, model, device):
        self.model = model
        self.device = device

    @performance
    def __call__(
        self, image, sample=True, num_beams=3, max_length=30, min_length=10, top_p=0.9, repetition_penalty=1.0
    ):
        gpu_image = (
            transforms.Compose(
                [
                    transforms.Resize((512, 512), interpolation=InterpolationMode.BICUBIC),
                    transforms.ToTensor(),
                    transforms.Normalize(
                        mean=[0.48145466, 0.4578275, 0.40821073],
                        std=[0.26862954, 0.26130258, 0.27577711],
                    ),
                ]
            )(image)
            .unsqueeze(0)
            .to(self.device)
        )
        with torch.no_grad():
            caption = self.model.generate(
                gpu_image,
                sample=sample,
                num_beams=num_beams,
                max_length=max_length,
                min_length=min_length,
                top_p=top_p,
                repetition_penalty=repetition_penalty,
            )[0]
        return caption
