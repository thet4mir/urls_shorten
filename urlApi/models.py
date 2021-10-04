from django.db import models
import random
import string


def code_generate(size=6):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(size))

class Urls(models.Model):

    class Meta:
        db_table = "urls"


    url         = models.CharField(max_length=250)
    short_code  = models.CharField(max_length=15, unique=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.short_code = code_generate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_code
