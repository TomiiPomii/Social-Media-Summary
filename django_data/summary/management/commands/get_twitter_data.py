from django.core.management.base import BaseCommand
from summary.collectors.collect import twitter_data


class Command(BaseCommand):
    help = "Runs the twitter_data function to test it"

    def handle(self, *args, **options):
        url = "https://twitter.com/elonmusk"
        user = twitter_data(url)
        print(user)
