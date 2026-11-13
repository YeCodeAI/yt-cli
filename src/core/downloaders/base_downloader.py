import pathlib

from abc import ABC, abstractmethod

from yt_dlp import YoutubeDL

from ...core import Config
from ...ui import UI

class BaseDownloader(ABC):
    """Base abstract class for downloading content using yt-dlp."""

    def __init__(self, path: str):
        self.output_dir = pathlib.Path(path)
        self.data = Config().get_path()
        self.ui = UI()

    def _download(self, url: str, ytdl_options: dict, start_message: str, success_message: str) -> None:
        with self.ui.create_progress() as progress:
            task_id = progress.add_task(f'[cyan]{start_message}[/cyan]', total=100)

            ytdl_options['progress_hooks'] = [
                self.ui.progress_hook(progress, task_id, 'Post-processing...')
            ]
            ytdl_options['ffmpeg_location'] = self.data['ffmpeg_path']

            try:
                with YoutubeDL(ytdl_options) as ytd:
                    ytd.download([url])
                self.ui.success(text=success_message)
            except Exception as e:
                self.ui.error(text=f'Download error: {e}')

    @abstractmethod
    def download(self, url: str) -> None:
        """Abstract method for downloading content. Must be implemented in subclasses."""
    
    @abstractmethod
    def download_playlist(self, playlist_url: str) -> None:
        """Abstract method for downloading playlist. Must be implemented in subclasses."""