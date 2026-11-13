from ..core.downloaders import DownloaderAudio
from ..core import Config

data = Config().get_path()
downloader = DownloaderAudio(data['download_dir'])

def audio_download_command(url: str) -> None:
    downloader.download(url)

def audio_playlist_download_command(playlist_url: str) -> None:
    downloader.download_playlist(playlist_url)