from typing import Annotated

import typer
from rich.console import Console

from .config import Config
from .downloder import DownloaderAudio, DownloaderVideo
from .ui import Status

app = typer.Typer(
    help='YT-CLI - CLI for comfortable downloading of audio or video from YouTube.',
    add_completion=False,
)

download_app = typer.Typer(help='Commands for downloading audio or video')
config_app = typer.Typer(help='Commands for managing application configurations.')

app.add_typer(download_app, name='download')
app.add_typer(config_app, name='config')

config = Config()
data = config.get_path()

downloader_audio = DownloaderAudio(path=data['download_dir'])
downloader_video = DownloaderVideo(path=data['download_dir'])

console = Console()


@download_app.command(
    'audio', help='Download audio from a YouTube video URL and convert it to MP3.'
)
def download_audio(
    url: Annotated[str, typer.Argument(help='The YouTube URL of the video to download as audio.')],
):
    """Downloads audio from the specified YouTube URL."""
    downloader_audio.download(url)


@download_app.command(
    'video', help='Download video and best audio streams combined from a YouTube URL.'
)
def download_video(
    url: Annotated[str, typer.Argument(help='The YouTube URL of the video to download.')],
):
    """Downloads video from the specified YouTube URL."""
    downloader_video.download(url)


@config_app.command(
    'get',
    help='Display current configuration paths (download directory and FFmpeg location).',
)
def get_path():
    """Retrieves and prints current configuration paths."""
    console.print(f'[cyan]Download directory path:[/cyan] {data["download_dir"]}')
    console.print(f'[cyan]FFmpeg path:[/cyan] {data["ffmpeg_path"]}')


@config_app.command('update', help='Update configuration paths for downloads and/or FFmpeg.')
def update_path(
    new_path_download_dir: Annotated[
        str | None,
        typer.Option('--download-dir', help='New path for the download directory.'),
    ] = None,
    new_path_ffmpeg: Annotated[
        str | None,
        typer.Option('--ffmpeg-dir', help='New path for the FFmpeg executable directory.'),
    ] = None,
):
    """Updates download or FFmpeg configuration paths in the config file."""
    if new_path_download_dir is None and new_path_ffmpeg is None:
        Status.error('Please provide at least one option: --download-dir or --ffmpeg-dir')
        raise typer.Exit(code=1)

    config.update_path(
        new_path_download_dir=new_path_download_dir,
        new_path_ffmpeg=new_path_ffmpeg,
    )
