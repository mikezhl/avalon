from django.db import models


class Game(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    room = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    op = models.CharField(max_length=255, blank=True, null=True)
    players = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    record = models.TextField(blank=True, null=True)
    secret = models.TextField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'

