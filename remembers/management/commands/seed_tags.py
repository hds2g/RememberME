import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from taggit.managers import TaggableManager


class Command(BaseCommand):

    help = "This command creates tags"

    def handle(self, *args, **options):
        tags = [
            "latesttech",
            "ilovemygadgets",
            "techie",
            "gadgetsgalore",
            "apple",
            "android",
            "applevsandroid",
            "wearabletech",
            "VR",
            "mobile",
            "makinglifeeasier",
            "tech",
            "technology",
            "technews",
            "gadgets",
            "instatech",
            "software",
            "innovation",
        ]

        tagManager = TaggableManager()
        print(dir(tagManager))
        # for t in tags:
        #    tagManager.tags.add(t)

        self.stdout.write(self.style.SUCCESS(f"tags created!"))
