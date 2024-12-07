import csv
from telethon import TelegramClient

# Replace with your API credentials
api_id = "21500155"
api_hash = "22bc01dbbb9e16793139522712ef5d3d"
phone_number = "+919692326598"  # Replace with your phone number
password = "969232"      # Replace with your Telegram password if 2FA is enabled

client = TelegramClient("session_name", api_id, api_hash)
async def fetch_messages(group_name, limit=100):
    # Connect to Telegram
    await client.start(phone=phone_number, password="969232")
    print("Client created")

    # Get the group/channel
    try:
        group = await client.get_entity(group_name)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Fetch messages
    messages = []
    async for message in client.iter_messages(group, limit=limit):
        messages.append({
            "date": message.date,
            "sender_id": message.sender_id,
            "text": message.text
        })

    # Save messages to a CSV file
    with open("telegram_messages.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["date", "sender_id", "text"])
        writer.writeheader()
        writer.writerows(messages)

    print(f"Saved {len(messages)} messages to telegram_messages.csv")

# Provide the group name or username of the Telegram group
group_name = "https://t.me/STOCKGAINERSS"

# Run the client and fetch messages
with client:
    client.loop.run_until_complete(fetch_messages(group_name, limit=200))
