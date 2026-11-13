from .base_downloader import BaseDownloader

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

    def download_playlist(self, playlist_url: str):
        """Downloads audio with full playlist from the specified URL and converts files to MP3 format."""

        options = {
            'format': 'bestaudio/best',
            'outtmpl': str(self.output_dir / '%(playlist_title)s' / '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': None,
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False
        }

        self._download(
            url=playlist_url,
            ytdl_options=options,
            start_message='Preparing to download playlist...',
            success_message=f'Playlist from {playlist_url} successfully downloaded!'
        )