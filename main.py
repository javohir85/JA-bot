import ccxt
binance = ccxt.binance({
'apiKey': "TNUL5yKBySpLH8sMZ2909iJCqFOCPMtglixlYDA3UoSDwTHIUmtldJEctfhhZnrV"    'secret': "E1LJpcX6BQwV4ugVjZiSTbIFBYy8l6K6H1pcSt8wv1UaPQvmyHbieisKmEjBjejy"
balance = binance.fetch_balance()
print(balance)
