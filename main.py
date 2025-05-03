import os
from telethon import TelegramClient
import asyncio

# Your credentials from environment variables
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')

async def send_message_to_friend():
    async with TelegramClient('aff', api_id, api_hash) as client:
        try:
            await client.send_message('@me', "Hello! This is a message to you from my script.")
            print("Message sent to friend successfully.")
        except Exception as e:
            print(f"Failed to send message: {e}")

# Run the async function
asyncio.run(send_message_to_friend())