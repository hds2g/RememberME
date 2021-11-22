import json
from django.db import models
from core import models as core_models
from django_editorjs import EditorJsField


class Tag(core_models.TimeStampedModel):

    """Photo Model Definition"""

    tag = models.CharField(max_length=80)
    remember = models.ForeignKey(
        "Remember", related_name="tag", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.tag


class Remember(core_models.TimeStampedModel):
    """Remember Model"""

    user = models.ForeignKey(
        "users.User", related_name="remembers", on_delete=models.CASCADE
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

    def __str__(self):
        rem = json.loads(self.remember)
        # print(rem)
        # print(rem["time"])
        # return self.user
        return str(rem["time"])
