# FileNuggets Telegram Bot 📄➡️📜

Welcome to FileNuggets, the Telegram bot that converts your DOC files to shiny PDFs! This was a fun little side project of mine—I’ve always wanted to convert files on the fly, so why not build a bot to do just that? 😄

## What Does It Do?

FileNuggets makes it super easy to convert DOC files to PDF directly through Telegram. Just upload your DOC file, and the bot will handle the rest, delivering a neat PDF right back to you!

## Features

- **Seamless File Conversion**: Upload a DOC file, and get a PDF in return. It’s that simple!
- **Instant Gratification**: The bot processes your files quickly and sends them back to you in no time.
- **Personal Touch**: Created with love by Basith. 😊

## How to Use

1. **Start the Bot**: Type `/start` or `/hello` to begin.
2. **Upload Your DOC File**: Simply send the bot your DOC file.
3. **Receive Your PDF**: Sit back and relax while the bot converts your file and sends you the PDF.

## Behind the Scenes

- **Python & Telebot**: The bot is powered by Python with the `telebot` library.
- **ConvertAPI**: Uses ConvertAPI to work its magic and transform your DOC files into PDFs.
- **Secure & Simple**: Your files are processed securely and are automatically cleaned up after the job is done.

## Getting Started

1. Clone this repository.
2. Install the required packages:
   ```bash
   pip install python-dotenv pyTelegramBotAPI requests
   ```
3. Set up your environment variables by creating a `.env` file:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   CONVERT_API_SECRET=your_convertapi_secret_here
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```
5. Open Telegram and interact with your bot!

## Why I Built This

I’ve always been fascinated by file conversions and wanted to create something that’s both useful and fun. Building this bot was a great way to combine both interests—plus, it’s super handy for anyone who needs to convert files on the go!

## License

Feel free to play around with this code and use it as you like. Just remember, have fun with it! 🎉
