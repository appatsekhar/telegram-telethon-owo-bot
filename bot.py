#!/usr/bin/env python3

# Import settings
import env

# Import important modules
import sys
from telethon import TelegramClient,events

# parse account from cli
if len(sys.argv) < 3:
	print("You need to specify an account name and a phone number!")
	exit()

account_file = sys.argv[1]
telephone_number = sys.argv[2]
	
client = TelegramClient(account_file, env.api_id, env.api_hash)
						
async def main():
    await client.send_message(env.chat_id if len(sys.argv) == 3 else int(sys.argv[3]), 'owo')

with client:
    client.loop.run_until_complete(main())