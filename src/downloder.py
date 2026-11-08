import pathlib
from abc import ABC, abstractmethod

from yt_dlp import YoutubeDL

from .config import Config
from .ui import Status


class BaseDownloader(ABC):
    """Base abstract class for downloading content using yt-dlp."""

    def __init__(self, path: str):
        self.output_dir = pathlib.Path(path)
        self.data = Config().get_path()

    def _get_progress_hook(self, progress, task_id):
        def hook(d):
            if d['status'] == 'downloading':
                downloaded = d.get('downloaded_bytes', 0)
                total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0

                if total > 0:
                    progress.update(task_id, total=total, completed=downloaded)

            elif d['status'] == 'finished':
                progress.update(task_id, description='[yellow]Конвертация в MP3...')

        return hook

    def _download(
        self, url: str, ytdl_options: dict, start_message: str, success_message: str
    ) -> None:
        with Status.create_progress() as progress:
            task_id = progress.add_task(f'[cyan]{start_message}[/cyan]', total=100)

            ytdl_options['progress_hooks'] = [
                self._get_progress_hook(progress, task_id, 'Post-processing...')
            ]
            ytdl_options['ffmpeg_location'] = self.data['ffmpeg_path']

            try:
                with YoutubeDL(ytdl_options) as ytd:
                    ytd.download([url])
                Status.success(text=success_message)
            except Exception as e:
                Status.error(text=f'Download error: {e}')

    @abstractmethod
    def download(self, url: str) -> None:
        """Abstract method for downloading content. Must be implemented in subclasses."""


class DownloaderAudio(BaseDownloader):
    """Handles audio extraction and downloading from supported platforms."""

    def download(self, url: str) -> None:
        """Downloads audio from the specified URL and converts it to MP3 format."""
        options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.output_dir.as_posix()}/%(title)s.%(ext)s',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
            'logger': None,
            'quiet': True,
            'no_warnings': True,
        }

        self._download(
            url=url,
            ytdl_options=options,
            start_message='Preparing to download audio...',
            success_message=f'Audio from {url} successfully downloaded!',
        )


class DownloaderVideo(BaseDownloader):
    """Handles video downloading with combined best video and audio streams."""

    def download(self, url: str) -> None:
        """Downloads video and best audio streams combined from the specified URL."""
        options = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'logger': None,
            'quiet': True,
            'no_warnings': True,
        }
        self._download(
            url=url,
            ytdl_options=options,
            start_message='Preparing to download video...',
            success_message=f'Video from {url} successfully downloaded!',
        )
