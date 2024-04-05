from django.db import models
from django.db.models.signals import post_s
from django.contrib.auth.models import User

class Followers(models.Model):
    owner = models.ForeignKey(on_delete=CASCADE, related_name='following')
    followed = models.ForeignKey(on_delete=CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


