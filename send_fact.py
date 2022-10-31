import randfacts
import os
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(os.environ.get('WEBHOOK_URL'))

fact = randfacts.get_fact()

embed = DiscordEmbed(title='Fact of the day!',
                     description=f'{fact}', color='03b2f8')
embed.set_timestamp()

webhook.add_embed(embed)

response = webhook.execute()