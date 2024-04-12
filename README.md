# YouTube Search Telegram Bot

This Telegram bot allows users to search for YouTube videos, fetch video information, and download videos directly to Telegram.

## Features

- Search for YouTube videos using keywords.
- Get detailed information about a YouTube video by providing its URL.
- Download YouTube videos in either video or audio format and upload them to Telegram.
- Interactive interface with inline keyboard options for easy navigation.

## Commands

1. `/start`: Start the bot and get a brief introduction.
2. `/help`: Get information about how to use the bot and available commands.
3. `/search`: Search for YouTube videos using keywords.
4. `/get`: Get detailed information about a YouTube video by providing its URL.
5. `/download`: Download a YouTube video and upload it to Telegram.

## Setup

To use this bot, you need to follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain API credentials for Telegram by creating a bot on the Telegram platform. You'll need the bot token, API ID, and API hash.
4. Update the `config.py` file with your API credentials.
5. Run the bot script using `python main.py`.

# Deployment On Heroku
- Click <a href="https://dashboard.heroku.com/new?template=https://github.com/sa3ed7asan/YouTube-Telegram-Bot">Here</a> And Enter Your API ID, API HASH And Your Bot Token.

## Usage

1. Start the bot by sending the `/start` command.
2. Use the `/search` command to search for YouTube videos using keywords. Select a video from the results to get detailed information or download it to Telegram.
3. Use the `/get` command to provide a YouTube video URL and get detailed information about the video.
4. Use the `/download` command to provide a YouTube video URL and choose whether to download it in video or audio format.


Feel free to contribute to this project by submitting pull requests or opening issues.

## License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE).
