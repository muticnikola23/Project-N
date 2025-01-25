from django.core import mail
from django.test import TestCase
from .utilities import send_email

class EmailSendTest(TestCase):
    def test_send_email(self):
        send_email('Subjected', 'Here is the message.', ['nikolamuta97@gmail.com'])

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subjected')
