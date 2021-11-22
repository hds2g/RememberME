import json
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

    REMEMBER_STAGE = (
        ("1W", "1Week"),
        ("2W", "2Week"),
        ("1M", "1Month"),
        ("3M", "3Months"),
        ("6M", "6Months"),
        ("1Y", "1Year"),
        ("2Y", "2Years"),
    )
    stage = models.CharField(
        max_length=2, choices=REMEMBER_STAGE, default=REMEMBER_STAGE[0][0]
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

    # slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
        rem = json.loads(self.remember)
        # print(rem)
        # print(rem["time"])
        # return self.user
        return str(rem["time"])
