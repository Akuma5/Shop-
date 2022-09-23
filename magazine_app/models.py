from django.db import models


class Magazine_app(models.Model):
    name = models.CharField(max_length=255, db_index=True,)


