import configparser

from pathlib import Path
from dataclasses import dataclass

@dataclass
class ConfigResult:
    download_dir: str
    ffmpeg_dir: str

class Config:
    def __init__(self):
        self.home = Path.home() / '.yt-cli'
        self.home.mkdir(parents=True, exist_ok=True)

        self.CONFIG_PATH = self.home / 'config.ini'

        self.config = configparser.ConfigParser()

    def _init_config(self) -> None:
        if not self.CONFIG_PATH.exists():
            self.config['Path'] = {
                'download_dir': str(self.home / 'Download dir'),
                'ffmpeg_dir' : str(self.home / 'FFMPEG dir')
            }

            with open(self.CONFIG_PATH, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

    def read_config(self) -> ConfigResult:
        self._init_config()
        self.config.read(self.CONFIG_PATH)

        return ConfigResult(
            download_dir=self.config['Path']['download_dir'],
            ffmpeg_dir=self.config['Path']['ffmpeg_dir']
        )
    
    def update_config(self, download_dir: str, ffmpeg_dir: str) -> ConfigResult:
        self._init_config()
        self.config.read(self.CONFIG_PATH)
        
        if download_dir and ffmpeg_dir:
            Path(download_dir).mkdir(parents=True, exist_ok=True)
            Path(ffmpeg_dir).mkdir(parents=True, exist_ok=True)

            self.config['Path']['download_dir'] = download_dir
            self.config['Path']['ffmpeg_dir'] = ffmpeg_dir

            with open(self.CONFIG_PATH, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

            return ConfigResult(
                download_dir=self.config['Path']['download_dir'],
                ffmpeg_dir=self.config['Path']['ffmpeg_dir']
            )