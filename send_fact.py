import randfacts
import os
from discord_webhook import DiscordWebhook, DiscordEmbed

if "WEBHOOK_URL" not in os.environ:
    raise Exception("WEBHOOK_URL is not set!")
else:
    WEBHOOK_URL = os.environ.get('WEBHOOK_URL')

webhook = DiscordWebhook(WEBHOOK_URL)

fact = randfacts.get_fact()

embed = DiscordEmbed(title='Fact of the day!',
                     description=f'{fact}', color='03b2f8')
embed.set_timestamp()

webhook.add_embed(embed)

response = webhook.execute()