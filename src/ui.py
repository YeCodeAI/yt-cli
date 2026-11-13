from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich.panel import Panel

console = Console()

class UI:
    def success(self, text: str) -> None:
        console.print(f'[green][+] {text}[/green]')

    def warning(self, text: str) -> None:
        console.print(f'[yellow][!] {text}[/yellow]')

    def error(self, text: str) -> None:
        console.print(f'[red][-] {text}[/red]')

    def info(self, text: str) -> None:
        console.print(f'[cyan][!] {text}[/cyan]')

    def log(self, text: str) -> None:
        console.log(text)

    def print_panel(self, content: str, title: str):
        panel = Panel(
            content,
            title=title,
            title_align='center',
            border_style='green',
            expand=False
        )

        console.print(panel)

    def progress_hook(self, progress: Progress, task_id: int, status_message: str):
        def hook(d):
            if d['status'] == 'downloading':
                downloaded = d.get('downloaded_bytes', 0)
                total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0

                if total > 0:
                    progress.update(task_id, total=total, completed=downloaded)

            elif d['status'] == 'finished':
                progress.update(task_id, description=f'[yellow]{status_message}[/yellow]')

        return hook
    
    def create_progress(self) -> Progress:
        return Progress(
            SpinnerColumn(),
            TextColumn('[progress.description]{task.description}'),
            BarColumn(),
            TextColumn('[progress.percentage]{task.percentage:>3.0f}%'),
            TimeRemainingColumn(),
            console=console,
        )