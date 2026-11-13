from .base_downloader import BaseDownloader

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
    
    def download_playlist(self, playlist_url: str):
        """Downloads video or a full playlist from the specified URL."""
        options = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': str(self.output_dir / '%(playlist_title)s' / '%(title)s.%(ext)s'),
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