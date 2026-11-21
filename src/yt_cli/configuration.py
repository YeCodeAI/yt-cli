import configparser
import pathlib

from dataclasses import dataclass

@dataclass
class ConfigResult:
    download_dir: str
    ffmpeg_dir: str

class ConfigManager:
    def __init__(self):
        self.home = pathlib.Path().home() / '.yt-cli'
        self.home.mkdir(parents=True, exist_ok=True)

        self.CONFIG_PATH = self.home / 'config.ini'

        self.config = configparser.ConfigParser()

    def _init_config(self):
        if not self.CONFIG_PATH.exists():
            self.config['Path'] = {
                'download_dir': str(pathlib.Path('~/YT-CLI Download').expanduser()),
                'yt_dlp_and_ffmpeg_path': str(self.home / 'yt-dlp and ffmpeg')
            }

            with open(self.CONFIG_PATH, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        
    def read_config(self) -> ConfigResult:
        self._init_config()
        self.config.read(self.CONFIG_PATH)

        return ConfigResult(
            download_dir=self.config['Path']['download_dir'],
            ffmpeg_dir=self.config['Path']['yt_dlp_and_ffmpeg_path']
        )
    
    def update_config(self, new_path_download_dir: str | None = None, new_path_yt_dlp_and_ffmpeg_path: str | None = None):
        self._init_config()
        self.config.read(self.CONFIG_PATH)

        if new_path_download_dir is not None:
            pathlib.Path(new_path_download_dir).mkdir(parents=True, exist_ok=True)
            self.config['Path']['download_dir'] = str(new_path_download_dir)

        if new_path_yt_dlp_and_ffmpeg_path is not None:
            pathlib.Path(new_path_yt_dlp_and_ffmpeg_path).mkdir(parents=True, exist_ok=True)
            self.config['Path']['yt_dlp_and_ffmpeg_path'] = str(new_path_yt_dlp_and_ffmpeg_path)

        with open(self.CONFIG_PATH, 'w', encoding='utf-8') as f:
            self.config.write(f)

