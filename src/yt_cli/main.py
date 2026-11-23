from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from .tools import AudioDownloader, VideoDownloader, ConfigManager
from .ui import UI

def main() -> None:
    ui = UI()

    audio_downloader = AudioDownloader()
    video_downloader = VideoDownloader()
    config_manager = ConfigManager()

    ui.show_banner()

    select_main_action = inquirer.select(
        message='Choice action',
        choices=[
            'Audio download',
            'Video download',
            'Config manager',
            'Exit'
        ],
        pointer='>'
    ).execute()

    if select_main_action == 'Audio download':
        select_audio_action = inquirer.select(
            message='Choice action with audio:',
            choices=[
                'Download audio via url'
            ],
            pointer='>'
        ).execute()

        if select_audio_action == 'Download audio via url':
            url = inquirer.text(
                message='Enter url:',
                default='https://youtube.com/'
            ).execute()

            audio_downloader.download(url)
            ui.success('Audio successfully download!')
    
    elif select_main_action == 'Video download':
        select_video_action = inquirer.select(
            message='Choice action with config',
            choices=[
                'Download video via url'
            ],
            pointer='>'
        ).execute()

        if select_video_action == 'Download video via url':
            url = inquirer.text(
                message='Enter url:',
                default='https://youtube.com/'
            ).execute()
            video_downloader.download(url)
            ui.success('Video successfully download!')
    
    elif select_main_action == 'Config manager':
        select_config_action = inquirer.select(
            message='Choice action with config',
            choices=[
                'Check all paths',
                'Update paths'
            ],
            pointer='>'
        ).execute()

        if select_config_action == 'Check all paths':
            config_manager.get_path()
        elif select_config_action == 'Update paths':
            config_manager.update_path()

    elif select_main_action == 'Exit':
        return



if __name__ == '__main__':
    main()