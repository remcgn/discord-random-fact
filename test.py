import unittest
import randfacts
import os
from discord_webhook import DiscordWebhook

if "WEBHOOK_URL" not in os.environ:
    raise Exception("WEBHOOK_URL is not set!")
else:
    WEBHOOK_URL = os.environ.get('WEBHOOK_URL')


class TestFact(unittest.TestCase):

    def test_fact(self):
        fact = randfacts.get_fact()
        self.assertNotEqual(fact, None)

    def test_hook(self):
        webhook = DiscordWebhook(url=f"{WEBHOOK_URL}",
                                 content="This is a test message!")
        send_response = webhook.execute()
        delete_response = webhook.delete(send_response)

        self.assertEqual(send_response.status_code, 200)
        self.assertEqual(delete_response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
