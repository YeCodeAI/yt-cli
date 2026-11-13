# YT-CLI🚀

A lightweight and fast command-line interface (CLI) tool built with Python to easily download audio and videos from YouTube with support progress bar and FFMPEG.

## Featurs:
- **Audio download**: Extract and download audio directly to MP3 format
- **Video download:** Download the best combined video and audio streams.
- **Playlist download**: Downloads audio or video from a playlist
- **Progress tracking:** Real-time progress bars powered by the `rich` library.
- **Customizable paths:** Easily configure and manage download directories and FFmpeg locations.
- **Modern Stack:** Built using `Typer`, `yt-dlp`, and managed with `uv`.


## Instalation
1. Clone the repository:
```bash
git clone [https://github.com/YeCodeAI/yt-cli](https://github.com/YeCodeAI/yt-cli)
cd yt-cli
```
2. Install the package using uv (recommended) or pip:
```bash
uv tool install .
```

## Usage
Run the CLI tool using the yt-cli command:

1. Download audio:
```bash
yt-cli download audio <YOUTUBE_URL>
```

2. Download video:
```bash
yt-cli download video "<YOUTUBE_URL>"
```

3. Batch file:
```bash
yt-cli download batch <FILE_PATH> # download video
yt-cli download batch <FILE_PATH> --audio # download only audio
```

4. Download playlist:
```bash
yt-cli download playlist audio <PLAYLIST_URL> # download audio
yt-cli download playlist video <PLAYLIST_URL> # download video
```

3. View current configuration paths:
```bash
yt-cli config get
```

4. Update download or FFmpeg directories:
```bash
yt-cli config update --download-dir "/path/to/downloads" --ffmpeg-dir "/path/to/ffmpeg"
```

## License
This project is licensed under the MIT License.