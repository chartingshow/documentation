# Telegram Signal Scrapper BOT

This tool extract's spot orders from a Telegram channel that provides crypto signals. The bot saves and executes these orders on Binance and sends notifications to a private Telegram channel. Although the bot fulfilled its purpose, after a few months, we realized that the signals from the channel were not very profitable, so we stopped testing the bot.

## Features

- Extracts values such as pair, entries, exits, stop loss and take profit from a signal message like this one:

<p align="center><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/telegram-signal-scrapper/1.png" alt="telegram scraper">

- Saves the pairs and orders placed in Binance as .json files when the orders are executed. This prevents placing more than one order per pair and provides a proper record of orders.

- Sends the buy/sell order at the same time as their respective SL/TP orders. If the SL or TP orders are manually cancelled, the buy/sell orders are cancelled as well. Conversely, it avoids placing orders without SL/TP.

- Has a notification system that sends updates on each step performed to a private Telegram channel.

<p align="center><img src="https://github.com/chartingshow/documentation/blob/master/assets/images/telegram-signal-scrapper/2.png" alt="telegram scraper">

## libraries required - Python 3.7 or later

To run the bot, you need the following Python libraries:

- telethon
- binance
