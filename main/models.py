from email.policy import default
from django.db import models


class todo(models.Model):
    text= models.CharField(max_length=100)
    date= models.DateTimeField(auto_now_add=True)
    is_closed= models.BooleanField(default=False)
    is_favorite= models.BooleanField(default=False)

