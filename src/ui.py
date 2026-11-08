from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeRemainingColumn,
)

console = Console()


class Status:
    @staticmethod
    def success(text: str) -> None:
        """Prints a success message in green with a '+' prefix."""
        console.print(f'[green][+] {text}[/green]')

    @staticmethod
    def error(text: str) -> None:
        """Prints an error message in red with a '-' prefix."""
        console.print(f'[red][-] {text}[/red]')

    @staticmethod
    def create_progress() -> Progress:
        """
        Creates and returns a configured Rich Progress instance

        with a spinner, description, progress bar, percentage, and remaining time.
        """
        return Progress(
            SpinnerColumn(),
            TextColumn('[progress.description]{task.description}'),
            BarColumn(),
            TextColumn('[progress.percentage]{task.percentage:>3.0f}%'),
            TimeRemainingColumn(),
            console=console,
        )
