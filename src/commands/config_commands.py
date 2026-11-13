import typer

from rich.text import Text

from ..ui import UI
from ..core import Config

config = Config()
ui = UI()

def get_path_command() -> None:
    content = Text()
    data = config.get_path()

    content.append('Downlod dir path: ', style='cyan')
    content.append(f'{data['download_dir']} \n')
    
    content.append('FFMPEG dir path : ', style='cyan')
    content.append(f'{data['ffmpeg_path']} \n')

    ui.print_panel(content, title='Paths')

def update_command(new_path_download_dir: str | None = None, new_path_ffmpeg: str | None = None) -> None:
    content = Text()

    if new_path_download_dir is None and new_path_ffmpeg is None:
        ui.error('Please provide at least one option: --download-dir or --ffmpeg-dir')
        raise typer.Exit(code=1)

    config.update_path(
        new_path_download_dir=new_path_download_dir,
        new_path_ffmpeg=new_path_ffmpeg,
    )

    data = config.get_path()

    content.append('Downlod dir path: ', style='cyan')
    content.append(f'{data['download_dir']} \n')
    
    content.append('FFMPEG dir path : ', style='cyan')
    content.append(f'{data['ffmpeg_path']} \n')

    ui.print_panel(content, title='Update paths')
