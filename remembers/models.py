import json
from datetime import datetime, timedelta
from django.db import models
from core import models as core_models

from taggit.managers import TaggableManager
from martor.models import MartorField


class Stage(core_models.TimeStampedModel):
    pass


class Remember(core_models.TimeStampedModel):
    """Remember Model"""

    user = models.ForeignKey(
        "users.User", related_name="remembers", on_delete=models.CASCADE
    )

    STAGE_1WEEK = "7"
    STAGE_2WEEK = "14"
    STAGE_1MONTH = "30"
    STAGE_2MONTH = "60"
    STAGE_3MONTH = "90"
    STAGE_6MONTH = "180"
    STAGE_1YEAR = "360"

    REMEMBER_STAGE = (
        (STAGE_1WEEK, "1 Week"),
        (STAGE_2WEEK, "2 Week"),
        (STAGE_1MONTH, "1 Month"),
        (STAGE_2MONTH, "2 Month"),
        (STAGE_3MONTH, "3 Month"),
        (STAGE_6MONTH, "6 Month"),
        (STAGE_1YEAR, "1 Year"),
    )

    stage = models.CharField(max_length=7, choices=REMEMBER_STAGE, default=STAGE_1WEEK)

    showing_date = models.DateField(
        "Showing Date", default=datetime.today() + timedelta(days=7)
    )
    remember = MartorField()

    # slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager(blank=True)

    # def __str__(self):
    #     time = self.remember["time"]
    #     print(time)
    #     print(self.remember)
    #     print(type(self.remember))
    #     # print(rem)
    #     # print(rem["time"])
    #     # return self.user

    #     # return "test"
    #     return self.user.username + "-" + str(time)


class RememberMeta(models.Model):
    remember = models.ForeignKey(Remember, on_delete=models.CASCADE)
    text = MartorField()

    def __str__(self):
        return self.text
