# Extracting a Subset of a Dictionary
# 1.17.1

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = { key:value for key, value in prices.items() if value > 200}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key,value in prices.items() if key in tech_names}

# Discussion

p1 = dict((key, value) for key, value in prices.items() if value > 200)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:prices[key] for key in prices.keys() & tech_names }
