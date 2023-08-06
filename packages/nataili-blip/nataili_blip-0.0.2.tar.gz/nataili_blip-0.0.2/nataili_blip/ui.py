import os

import pandas as pd
import panel as pn
import param
from bokeh.themes import DARK_MINIMAL
from panel.template.theme import Theme

from nataili_blip.caption import Caption
from nataili_blip.model_manager import BlipModelManager
from nataili_blip.util import logger

model_manager = BlipModelManager()
caption = None

files = []


class DarkTheme(Theme):
    bokeh_theme = param.ClassSelector(class_=(Theme, str), default=DARK_MINIMAL)


class MaterialDarkTheme(DarkTheme):
    _template = pn.template.MaterialTemplate


dark_material = pn.template.MaterialTemplate(title="Nataili BLIP", theme=DarkTheme)


def load():
    gpu_id = ui.model.gpu_id if model_manager.cuda_available else 0
    precision = ui.model.precision if model_manager.cuda_available else "full"
    model_name = ui.model.model_name[0]
    blip_image_eval_size = ui.model.blip_image_eval_size

    if model_name not in model_manager.available_models:
        logger.warning(f"{model_name} not available")
        logger.info(f"Downloading {model_name}")
        ui.loading_status.value = f"Downloading {model_name}"
        ui.loading_indicator.value = True
        success = model_manager.download_model(model_name)
        ui.loading_indicator.value = False
        if not success:
            logger.error(f"Unable to download {model_name}")
            ui.loading_status.value = f"Unable to download {model_name}"
            return
        ui.loading_status.value = f"Downloaded {model_name}"
        logger.info(f"Downloaded {model_name}")

    if model_name not in model_manager.loaded_models:
        logger.info(f"Loading {model_name}")
        ui.loading_status.value = f"Loading {model_name}"
        ui.loading_indicator.value = True
        success = model_manager.load_blip(
            model_name,
            precision,
            gpu_id,
            blip_image_eval_size,
            "base" if model_name == "BLIP" else "large",
        )
        if not success:
            logger.error(f"Unable to load {model_name}")
            ui.loading_status.value = f"Unable to load {model_name}"
            ui.loading_indicator.value = False
            return
        ui.loaded_models.value = model_manager.get_loaded_models_names(string=True)
        logger.info(f"Loaded models: {ui.loaded_models.value}")
        ui.loading_indicator.value = False
        ui.loading_status.value = "Idle"

    global caption
    caption = Caption(
        model_manager.loaded_models[model_name]["model"], model_manager.loaded_models[model_name]["device"]
    )
    return


def caption_images(rename=False, txt_file=False):
    global caption, files, ui
    if caption is None:
        logger.warning("Model not loaded")
        ui.loading_status.value = "Model not loaded"
        load()
        if caption is None:
            logger.error("Unable to load model")
            return
    logger.info(f"Captioning images:")
    ui.loading_status.value = "Captioning images"
    ui.loading_indicator.value = True
    idx = 1
    for file in files:
        logger.info(f"Captioning image {idx}")
        ui.loading_status.value = f"Captioning image {idx}"
        result = caption(
            file,
            ui.options.sample,
            ui.options.num_beams,
            ui.options.max_length,
            ui.options.min_length,
            ui.options.top_p,
            ui.options.repetition_penalty,
        )
        logger.info(f"Captioning image {idx}: {result}")
        logger.info(f"Captioning image {idx}: {file}")
        result_message = f"Image {idx} ({file}) - Caption: {result}"

        if rename:
            old_file = file
            ext = os.path.splitext(old_file)[1]
            base_dir = os.path.dirname(old_file)
            file = f"{base_dir}/{result.replace(' ', '_')}{ext}"
            os.rename(old_file, file)
            result_message = f"Image {idx} - Caption: {result} - Renamed to {os.path.basename(file)}"

        if txt_file:
            ext = os.path.splitext(file)[1]
            txt_file = file.replace(ext, ".txt")
            with open(f"{txt_file}.txt", "w") as f:
                f.write(result)
            result_message = f"Image {idx} - Caption: {result} - Caption saved to {os.path.basename(txt_file)}"

        logger.info(result_message)
        ui.results.extend(pn.Row(pn.widgets.StaticText(value=result_message)))
        idx += 1

    ui.loading_status.value = "Idle"
    ui.loading_indicator.value = False
    ui.file_selector.value = []


class BlipModel(param.Parameterized):
    model_name = param.ListSelector(default=["BLIP"], objects=["BLIP", "BLIP_Large"])
    if model_manager.cuda_available:
        gpu_id = param.Integer(default=0, bounds=(0, len(model_manager.cuda_devices)), step=1)
    blip_image_eval_size = param.Integer(default=512, bounds=(256, 1024), step=64)
    load_model = param.Action(lambda x: load(), label="Load Model")


class BlipOptions(param.Parameterized):
    sample = param.Boolean(default=True)
    num_beams = param.Integer(default=3, bounds=(1, 8), step=1)
    max_length = param.Integer(default=30, bounds=(10, 100), step=1)
    min_length = param.Integer(default=10, bounds=(1, 30), step=1)
    top_p = param.Number(default=0.9, bounds=(0.0, 1.0), step=0.1)
    repetition_penalty = param.Number(default=1.0, bounds=(0.0, 2.0), step=0.1)


class BlipCaptionResult(param.Parameterized):
    filename = param.String(default="")
    caption = param.String(default="")


class BlipCaptionResults(param.Parameterized):
    results = param.List(class_=BlipCaptionResult)


class BlipCaption(param.Parameterized):
    caption_button = param.Action(lambda x: caption_images(), label="Caption Images")
    rename_button = param.Action(lambda x: caption_images(rename=True), label="Caption and Rename Images")
    txt_file_button = param.Action(lambda x: caption_images(txt_file=True), label="Caption and Save to Text File")
    clear_button = param.Action(lambda x: ui.results.clear(), label="Clear Results")


class BlipUI(param.Parameterized):
    loaded_models = pn.widgets.StaticText(value="")
    loading_status = pn.widgets.StaticText(value="Idle")
    loading_indicator = pn.indicators.LoadingSpinner(width=24, height=24, value=False, color="info", bgcolor="dark")
    file_selector = pn.widgets.FileSelector(
        file_pattern="*.[pjw][npe][geb]*", root_directory="~", width=600, height=400
    )

    def __init__(self, **params):
        super().__init__(**params)
        self.model = BlipModel()
        self.options = BlipOptions()
        self.caption_images = BlipCaption()
        self.results = pn.Column()

    @param.depends("file_selector.value", watch=True)
    def _update_file_selector(self):
        global files
        files = []
        files = self.file_selector.value

    def view(self):
        dark_material.sidebar.append(
            pn.Column(
                pn.Column(
                    pn.Row(
                        self.loading_indicator,
                        self.loading_status,
                        sizing_mode="stretch_width",
                        align="center",
                        margin=0,
                    ),
                    self.loaded_models,
                ),
                pn.Column(
                    self.model,
                    self.options,
                ),
            )
        )
        dark_material.main.append(
            pn.Pane(
                pn.Column(
                    pn.Row(
                        pn.Column(
                            self.file_selector,
                            align="end",
                        ),
                        pn.Column(
                            self.caption_images,
                        ),
                    ),
                    pn.Row(
                        pn.Column(
                            pn.pane.Markdown("## Results"),
                            self.results,
                        ),
                    ),
                ),
            )
        )
        return dark_material


ui = BlipUI()


def main():
    ui.view().show()


if __name__ == "__main__":
    main()
