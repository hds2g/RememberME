import json
from datetime import datetime, timedelta
from django.db import models
from core import models as core_models
from django_editorjs import EditorJsField
from taggit.managers import TaggableManager


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

    remember = EditorJsField(
        editorjs_config={
            "tools": {
                "Link": {"config": {"endpoint": "/linkfetching/"}},
                "Image": {
                    "config": {
                        "endpoints": {
                            "byFile": "/remembers/uploadi/",
                            "byUrl": "/remembers/uploadi/",
                        },
                        "addtionalRequestHeader": [
                            {"Content-Type": "multipart/form-data"}
                        ],
                    }
                },
                "Attaches": {"config": {"endpoint": "/uploadf/"}},
            }
        }
    )

    # slug = models.SlugField(unique=True, max_length=100) does it need?
    tags = TaggableManager(blank=True)

    def __str__(self):
        rem = json.loads(self.remember)
        # print(rem)
        # print(rem["time"])
        # return self.user
        return self.user.username + "-" + str(rem["time"])
