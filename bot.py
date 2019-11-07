# Import settings
import env

# Import important modules
import sys
from telethon import TelegramClient,events

# parse account from cli
if len(sys.argv) != 3:
	print("You need to specify an account name and a phone number!")
	exit()

account_file = sys.argv[1]
telephone_number = sys.argv[2]
	
client = TelegramClient(account_file, env.api_id, env.api_hash)
						
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message(env.chat_id, 'owo')

with client:
    client.loop.run_until_complete(main())