from django.core.management.base import BaseCommand, CommandError
from BTC_price.settings import *
from bitcoin.models import Price
import GDAX

class Command(BaseCommand):
    help = "Stores the BTC set - price&time in the database"

    def handle(self, *args, **options):
        publicClient = GDAX.PublicClient()
        price = publicClient.getProductTicker(product="BTC-USD")
        time = publicClient.getTime()
        BTC_set = Price(price=price["price"], time=time.get("iso")[0:18])
        BTC_set.save()
        self.stdout.write(self.style.SUCCESS("Succesfully added BTC_set to the database"))