import typer

from typing import Annotated

from .ui import UI
from .commands import (
    get_path_command,
    update_command,
    audio_download_command,
    audio_playlist_download_command,
    video_download_command,
    video_playlist_download_command,
    batch_command
)

ui = UI()

app = typer.Typer(
    help='YT-CLI - CLI for comfortable downloading of audio or video from YouTube.',
    add_completion=False,
)

download_app = typer.Typer(help='Commands for downloading audio or video')
config_app = typer.Typer(help='Commands for managing application configurations.')
download_playlist_app = typer.Typer(help='Commands for downloading playlist')

app.add_typer(download_app, name='download')
app.add_typer(config_app, name='config')
download_app.add_typer(download_playlist_app, name='playlist')


@download_app.command('audio')
def download_audio(url: Annotated[str, typer.Argument(help='The YouTube URL of the video to download as audio.')]):
    """Downloads audio from the specified YouTube URL."""
    audio_download_command(url)

@download_app.command('video')
def download_video(url: Annotated[str, typer.Argument(help='The YouTube URL of the video to download.')],):
    """Downloads video from the specified YouTube URL."""
    video_download_command(url)


@download_app.command('batch')
def download_batch(
    file_path: Annotated[str, typer.Argument(help='Path to the .txt file with URLs')],
    only_audio: Annotated[bool, typer.Option('--audio', '-a', help='Download as audio (MP3) instead of video.')] = False,
):
    """Downloads a batch of URLs listed in a text file."""
    batch_command(file_path, only_audio)

@download_playlist_app.command('audio')
def download_audio_playlist(playlist_url: Annotated[str, typer.Argument(help='The Youtube playlist of the videos to download audio')]) -> None:
    """Downloads audios from playlists"""
    audio_playlist_download_command(playlist_url)

@download_playlist_app.command('video')
def download_audio_playlist(playlist_url: Annotated[str, typer.Argument(help='The Youtube playlist of the videos to download')]) -> None:
    """Downloads videos from playlists"""
    video_playlist_download_command(playlist_url)

@config_app.command('get')
def get_path():
    """Retrieves and prints current configuration paths."""
    get_path_command()

@config_app.command('update')
def update_path(
    new_path_download_dir: Annotated[str | None,typer.Option('--download-dir', help='New path for the download directory.'),] = None,
    new_path_ffmpeg: Annotated[str | None,typer.Option('--ffmpeg-dir', help='New path for the FFmpeg executable directory.'),] = None,
):
    """Updates download or FFmpeg configuration paths in the config file."""
    update_command(new_path_download_dir, new_path_ffmpeg)