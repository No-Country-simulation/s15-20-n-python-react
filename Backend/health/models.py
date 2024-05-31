from django.db import models

from django.contrib.auth import get_user_model

# Instance of User model
User = get_user_model()

# Create your models here.


class HealthTest(models.Model):
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'health'
        verbose_name = 'salud'
