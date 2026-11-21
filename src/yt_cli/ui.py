from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

console = Console()
error_console = Console(stderr=True)

class UI:
    def success(self, text: str) -> None:
        console.print(f'[green][+] {text}[/green]')

    def warning(self, text: str) -> None:
        console.print(f'[yellow][!] {text}[/yellow]')

    def error(self, text: str) -> None:
        error_console.print(f'[red][!] {text}[/red]')
    
    def info(self, text: str) -> None:
        console.print(f'[cyan][*] {text}[/cyan]')
    
    def create_panel(self, text: str, title: str) -> None:
        console.print(
            Panel(
                text,
                title=title,
                title_align='center',
                border_style='green',
                expand=False,
                padding=(1, 2)
            )
        )

    def progress_bar(self) -> Progress:
        return Progress(
            SpinnerColumn(),
            TextColumn('[bold blue]{task.description}'),
            BarColumn(bar_width=None),
            '[progress.percentage]{task.percentage:>3.1f}%',
            '•',
            DownloadColumn(),
            '•',
            TransferSpeedColumn(),
            '•',
            TimeRemainingColumn(),
            console=console,
            transient=False, 
        )
    
    def show_video_info(self, title: str, channel: str, duration: str, views: str = '') -> None:
        table = Table.grid(padding=(1,2))

        table.add_column(style='bold cyan', justify='right')
        table.add_column(style='white')
        
        table.add_row('Title', title)
        table.add_row('Channel', channel)
        table.add_row('Duration', duration)
        if views:
            table.add_row('Views', views)

        console.print(
            Panel(
                table,
                title='[bold green]Information on video[/bold green]',
                border_style='cyan',
                expand=False,
                padding=(1, 2),
            )
        )

        