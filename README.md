# BTC_price

1. Basic informations
It is a simply web application showing bitcoin (BTC) price in US dollars from GDAX in real time. You can find there also BTC rates from last 10 minutes (lowest and highest tickers) and the average price calculated from them as well.

2. Storing data in database
After you configure settings with your mySQL database, you can send data from API into the database (it is a set: BTC price with corresponding time). You need to write the command in the shell:
$ python manage.py store
