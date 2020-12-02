from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Location(models.Model):
    "Generated Model"
    address1 = models.CharField(
        max_length=256,
    )
    address2 = models.CharField(
        max_length=256,
    )
    city = models.CharField(
        max_length=256,
    )
    state = models.CharField(
        max_length=256,
    )
    zip = models.CharField(
        max_length=256,
    )


class Name(models.Model):
    "Generated Model"
    name = models.BigIntegerField()
    event = models.BigIntegerField()
    location = models.ForeignKey(
        "home.Location",
        on_delete=models.CASCADE,
        related_name="name_location",
    )
