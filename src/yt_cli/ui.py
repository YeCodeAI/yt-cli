from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.theme import Theme

from .configuration import ConfigResult

class UI:
    def __init__(self) -> None:
        custom_theme = Theme(
            {
                'info': 'bold cyan',
                'success': 'bold green',
                'warning': 'bold yellow',
                'error': 'bold red',
            }
        )
        self.console = Console(theme=custom_theme)

    def info(self, message: str) -> None:
        self.console.print(f'[info]ℹ[/info] {message}')

    def success(self, message: str) -> None:
        self.console.print(f'[success]✔[/success] {message}')

    def warning(self, message: str) -> None:
        self.console.print(f'[warning]⚠[/warning] {message}')

    def error(self, message: str) -> None:
        self.console.print(f'[error]✖[/error] {message}')

    def show_banner(self, title: str = 'YT-CLI Downloader') -> None:
        self.console.print(
            Panel.fit(f'[bold magenta]{title}[/bold magenta]', border_style='magenta')
        )

    def show_config(self, config: ConfigResult) -> None:
        table = Table(title='Paths', show_header=True, header_style='bold cyan')
        table.add_column('Parameter', style='bold')
        table.add_column('Path', style='green')

        table.add_row('Download dir', config.download_dir)
        table.add_row('FFMPEG dir', config.ffmpeg_dir)

        self.console.print(table)