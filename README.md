# YT-CLI🚀

A lightweight and fast command-line interface (CLI) tool built with Python to easily download audio and videos from YouTube with support progress bar and FFMPEG.

## Featurs:
- **Audio Download**: Extract and download audio directly to MP3 format
- **Video Download:** Download the best combined video and audio streams.
- **Progress Tracking:** Real-time progress bars powered by the `rich` library.
- **Customizable Paths:** Easily configure and manage download directories and FFmpeg locations.
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

1. Download Audio:
```bash
yt-cli download audio "<YouTube_URL>"
```

2. Download Video:
```bash
yt-cli download video "<YouTube_URL>"
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