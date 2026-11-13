import pathlib

from ..ui import UI
from ..core import Config
from ..core.downloaders import DownloaderAudio, DownloaderVideo

ui = UI()
data = Config().get_path()
downloader_audio = DownloaderAudio(data['download_dir'])
downloader_video = DownloaderVideo(data['download_dir'])

def batch_command(file_path: str, only_audio: bool):
    path = pathlib.Path(file_path)
    if not path.exists():
        ui.error(f'File not found: {file_path}')

    lines = path.read_text(encoding='utf-8').splitlines()
    urls = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]

    if not urls:
        ui.error('The file does not contain any valid URLs')

    ui.success(f'Found {len(urls)} URLs to download.')

    downloader = downloader_audio if only_audio else downloader_video

    for index, url in enumerate(urls, 1):
        ui.info(f'\n({index}/{len(urls)}) Processing: {url}')
        try:
            downloader.download(url)
        except Exception as e:
            ui.error(f'Failed to download {url}: {e}')