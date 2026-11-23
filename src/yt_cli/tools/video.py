from ..base import BaseDownloader

class VideoDownloader(BaseDownloader):
    def _get_opts(self):
        return {
            'format': 'bestvideo[height<=1080]+bestaudio',
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegMetadata',
                }
            ],
        }