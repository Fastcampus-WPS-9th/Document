from django.db import models


class Ancestor(models.Model):
    name = models.CharField(
        max_length=10,
        db_column='name',
    )


class Child(Ancestor):
    name2 = models.CharField(
        max_length=20,
        db_column='name',
    )
