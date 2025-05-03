import os
import logging
from telethon import TelegramClient, events
import asyncio

# Set up logging to show info and error messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load your credentials from environment variables for safety
api_id = int(os.environ.get('API_ID', '24923438'))
api_hash = os.environ.get('API_HASH', '5e23caf28e25b279e9099fa04442a9b7')
bot_token = os.environ.get('BOT_TOKEN', '7701437063:AAGAgt_YUFYpOOz1BMHoHHw6OXpTQyJ9u0E')  # Your bot token

async def main():
    try:
        # Create the Telegram client and start it as a bot
        client = TelegramClient('bot', api_id, api_hash)
        await client.start(bot_token=bot_token)

        # Event handler when a new message is received
        @client.on(events.NewMessage)
        async def handler(event):
            await event.respond('Hello! I am your bot.')

        logging.info("Bot is running...")
        await client.run_until_disconnected()
    except Exception as e:
        logging.error(f"Failed to start bot: {e}")

if __name__ == '__main__':
    asyncio.run(main())