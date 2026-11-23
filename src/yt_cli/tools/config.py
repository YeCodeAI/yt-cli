from InquirerPy import inquirer
from InquirerPy.validator import PathValidator

from ..configuration import Config
from ..ui import UI

class ConfigManager:
    def __init__(self):
        self.ui = UI()
        self.config = Config()

    def get_path(self) -> None:
        result = self.config.read_config()

        self.ui.show_config(result)

    def update_path(self) -> None:
        current = self.config.read_config()

        download_dir = inquirer.filepath(
            message='Specify a new folder for downloads (press Enter to keep the current one):',
            default=current.download_dir,
            only_directories=True,
            validate=PathValidator(is_dir=True, message='Specify the correct path to the folder'),
        ).execute()

        ffmpeg_dir = inquirer.filepath(
            message='Specify the path to the folder containing FFmpeg (press Enter to keep the current one):',
            default=current.ffmpeg_dir,
            only_directories=True,
            validate=PathValidator(is_dir=True, message='Specify the correct path to the folder'),
        ).execute()

        updated = self.config.update_config(
            download_dir=download_dir,
            ffmpeg_dir=ffmpeg_dir,
        )

        self.ui.success('Settings successfully updated!')
        self.ui.show_config(updated)