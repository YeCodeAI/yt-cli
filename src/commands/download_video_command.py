from ..core.downloaders import DownloaderVideo
from ..core import Config

data = Config().get_path()
downloader = DownloaderVideo(data['download_dir'])

def video_download_command(url: str) -> None:
    downloader.download(url)

def video_playlist_download_command(playlist_url: str) -> None:
    downloader.download_playlist(playlist_url)