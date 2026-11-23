from abc import ABC, abstractmethod
from typing import Any, Dict
from pathlib import Path

from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

from yt_dlp import YoutubeDL

from .configuration import Config
from .ui import UI

class BaseDownloader(ABC):
    def __init__(self):
        self._progress: Progress | None = None
        self._task_id: TaskID | None = None
        self.config = Config().read_config()
        self.ui = UI()

    @abstractmethod
    def _get_opts(self) -> Dict[str, Any]:
        pass

    def _build_opts(self) -> Dict[str, Any]:
        opts = self._get_opts().copy()

        opts.setdefault('paths', {})['home'] = self.config.download_dir
        opts.setdefault('outtmpl', '%(title)s.%(ext)s')

        if self.config.ffmpeg_dir:
            opts['ffmpeg_location'] = self.config.ffmpeg_dir

        opts.setdefault('progress_hooks', []).append(self._progress_hook)
        opts.setdefault('quiet', True)
        opts.setdefault('no_warnings', True)

        return opts

    def _progress_hook(self, d: Dict[str, Any]) -> None:
        status = d.get('status')

        if self._progress is None:
            self._progress = Progress(
                TextColumn('[bold blue]{task.description}'),
                BarColumn(),
                DownloadColumn(),
                TransferSpeedColumn(),
                TimeRemainingColumn(),
            )
            self._progress.start()
            filename = d.get('info_dict', {}).get('title')
            self._task_id = self._progress.add_task(filename, total=None)

        if status == 'downloading' and self._task_id is not None:
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)
            if self._progress is not None:
                self._progress.update(self._task_id, total=total, completed=downloaded)
        
        elif status in ('finished', 'error'):
            if status == 'finished' and self._task_id is not None:
                total = d.get('total_bytes') or d.get('total_bytes_estimate')
                if total:
                    self._progress.update(self._task_id, completed=total)

            self._progress.stop()
            self._progress = None
            self._task_id = None

    def download(self, url: str) -> None:
        Path(self.config.download_dir).mkdir(parents=True, exist_ok=True)
        opts = self._build_opts()

        try:
            with YoutubeDL(opts) as ydl:
                ydl.download([url])
        finally:
            if self._progress is not None:
                self._progress.stop()
                self._progress = None
                self._task_id = None

