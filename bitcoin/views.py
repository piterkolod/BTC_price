from django.shortcuts import render
from django.views import View
import GDAX


class PriceView(View):
    def get(self, request):

        publicClient = GDAX.PublicClient()
        price = publicClient.getProductTicker(product="BTC-USD")
        time = publicClient.getTime()

        history = publicClient.getProductHistoricRates(granularity=60)[0:10]

        avg = 0
        for i in history:
            avg += (i[1] + i[2]) / 2
        avg = round(avg/10, 2)

        ctx = {
            'time': time["iso"],
            'price': price['price'],
            'history': history,
            'avg': avg
        }

        return render(request, 'bitcoin/index.html', ctx)

