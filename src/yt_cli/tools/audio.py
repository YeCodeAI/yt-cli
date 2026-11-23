from ..base import BaseDownloader

class AudioDownloader(BaseDownloader):
    def _get_opts(self):
        return {
            'format': 'bestaudio/best',
            'writethumbnail': False,
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
        }