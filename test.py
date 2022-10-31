import unittest
import randfacts
import os
from discord_webhook import DiscordWebhook
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')


class TestFact(unittest.TestCase):

    def test_fact(self):
        fact = randfacts.get_fact()
        self.assertNotEqual(fact, None)

    def test_hook(self):
        webhook = DiscordWebhook(url=f"{WEBHOOK_URL}",
                                 content="This is a test message!")
        response = webhook.execute()

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
