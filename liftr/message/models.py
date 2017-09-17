from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MessageManager(models.Manager):
    def history(self, curr_user, chat_buddy):
        messages = Message.objects.get(from_user=curr_user,to_user=chat_buddy)

        return (message.message_details+"\n" for message in messages)


class Message(models.Model):
    from_user = models.OneToOneField(User, related_name="sender")
    to_user = models.OneToOneField(User, related_name="receiver")
    sent_at = models.DateField(default=timezone.now)
    message = models.TextField()

    @property
    def message_details(self):
        return "{} \tSent by: {} (@ {})".format(self.message, self.from_user, self.sent_at)
