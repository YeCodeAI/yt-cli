import configparser
import pathlib

from .ui import Status


class Config:
    """
    Manages application configuration, including directory paths for downloads and FFmpeg,

    stored in an INI file within the user's home directory.
    """

    def __init__(self):
        self.home = pathlib.Path().home() / '.yt-cli'
        self.home.mkdir(parents=True, exist_ok=True)

        self.CONFIG_FILE = self.home / 'config.ini'

        self.config = configparser.ConfigParser()

    def init_config(self):
        """
        Initializes the configuration file with default values if it does not already exist.
        """
        if self.CONFIG_FILE.exists():
            return

        self.config['Path'] = {
            'download_dir': str(pathlib.Path('~/YT-CLI Download').expanduser()),
            'ffmpeg_path': str(self.home / 'ffmpeg'),
        }

        with open(self.CONFIG_FILE, 'w', encoding='utf-8') as f:
            self.config.write(f)

    def get_path(self):
        """
        Retrieves and returns the configuration paths for downloads and FFmpeg.
        """
        self.init_config()
        self.config.read(self.CONFIG_FILE)

        return {
            'download_dir': self.config['Path']['download_dir'],
            'ffmpeg_path': self.config['Path']['ffmpeg_path'],
        }

    def update_path(
        self,
        new_path_download_dir: str | None = None,
        new_path_ffmpeg: str | None = None,
    ):
        """
        Updates the download and/or FFmpeg paths in the configuration file

        and ensures the target directories exist.
        """
        self.init_config()
        self.config.read(self.CONFIG_FILE)

        if new_path_download_dir is not None:
            pathlib.Path(new_path_download_dir).mkdir(parents=True, exist_ok=True)
            self.config['Path']['download_dir'] = str(new_path_download_dir)
            Status.success(f'Updated download path: {new_path_download_dir}')

        if new_path_ffmpeg is not None:
            pathlib.Path(new_path_ffmpeg).mkdir(parents=True, exist_ok=True)
            self.config['Path']['ffmpeg_path'] = str(new_path_ffmpeg)
            Status.success(f'Updated ffmpeg path: {new_path_ffmpeg}')

        with open(self.CONFIG_FILE, 'w', encoding='utf-8') as f:
            self.config.write(f)
