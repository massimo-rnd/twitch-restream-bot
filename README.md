<div align="center">

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/massimo-rnd/twitch-restream-bot?include_prereleases)

![.NET Version](https://img.shields.io/badge/stability-testing-yellow)
![GitHub last commit](https://img.shields.io/github/last-commit/massimo-rnd/twitch-restream-bot)

  <br>

  ![GitHub All Releases](https://img.shields.io/github/downloads/massimo-rnd/twitch-restream-bot/total)
  ![GitHub closed issues](https://img.shields.io/github/issues-closed/massimo-rnd/twitch-restream-bot)
  ![GitHub issues](https://img.shields.io/github/issues/massimo-rnd/twitch-restream-bot)
  
  <h1>Twitch Restream Bot</h1>
  <p>
    A Python script that automatically starts a restream of a Twitch stream using OBS<br>
  </p>
</div>

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About

Twitch Restream Bot is A Python script that automatically starts a restream of a Twitch stream using OBS. It uses Twitch's to detect if a channel is live and OBS's Websocket Plugin to send the Start/Stop Streaming Command.

---

## Features

- ✅ Detect if a Channel starts a Livestream
- ✅ Automatically Starts/Stops the Stream in OBS

---

## Installation

### Download the latest version

To start off, please head to the [releases page](https://github.com/massimo-rnd/twitch-restream-bot/releases) and download the latest release version.

### Setting Up OBS
Please make sure to have the OBS Websocket Plugin installed.

Set up your OBS Streaming credentials as you always would and Enable the Websocket Plugin.

### Entering credentials
Register for a Twitch Developer Account and optain your Client ID and Client Secret.

Open the twitch-restream-bot.py in a text editor of your choice and enter TWITCH_CLIENT_ID and TWITCH_CLIENT_SECRET for Twitch's API, TWITCH_CHANNEL_ID for your Source-Channel ID and OBS_WEBSOCKET_PASSWORD.


### Launch the application

Launch the application in terminal using python3 twitch-restream-bot.py

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

- **massimo-rnd** - [@massimo_rnd](https://x.com/massimo_rnd) - hi@massimo.gg
- **Project Link** - https://github.com/massimo-rnd/twitch-restream-bot

Feel free to reach out if you have any questions or suggestions!

---
