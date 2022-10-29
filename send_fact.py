import randfacts
import os
from discord_webhook import DiscordWebhook

WEBHOOK_URL = os.environ.get('WEBHOOK_URL')

fact = randfacts.get_fact()

webhook = DiscordWebhook(url=f"{WEBHOOK_URL}",
                            content=f"Fact of the day: {fact}")

response = webhook.execute()

print(response)