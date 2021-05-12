
# extension to search for on the web page.
all_currency = 'all.json'
# dict file for saving all exchange rate data based on user input
currency_dict = {}
# weblink to search for data
url = 'http://www.floatrates.com/daily/{}'.format(all_currency)
response = requests.get(url)
content = response.json()
# extract usd and eur rate and save in a dict
currency_dict['usd'] = content['usd']['rate']
currency_dict['eur'] = content['eur']['rate']
# currency_dict = {'usd': content['usd']['rate'], 'eur': content['eur']['rate']}
user_currency = input()
key_list = content.keys()
# convert dict to list
currency_list = []
for key in key_list:
    currency_list.append(key)
# while loop that keep running as long as user enter expected a valid input
while True:
    expected_currency = input()
    # Check is expected currency prompt has nothing as input
    # This will end the converter script
    if expected_currency == "":
        exit()
    else:
        pass
    # user prompt for Amount to be exchanged
    user_amount = float(input())
    user_rate = content[user_currency]['rate']
    if expected_currency in currency_dict:
        expected_rate = currency_dict.get(expected_currency, "null")
        amount = round((user_amount * expected_rate / user_rate), 2)
        expected_currency = expected_currency.upper()
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print("You received {} {}.".format(amount, expected_currency))
    elif expected_currency in currency_list:
        expected_rate = content[expected_currency]['rate']
        amount = round((user_amount * expected_rate / user_rate), 2)
        currency_dict[expected_currency] = content[expected_currency]['rate']
        currency_list.pop(currency_list.index(expected_currency)).lower()
        expected_currency = expected_currency.upper()
        print("Checking the cache...")
        print("Sorry, but it is not in the cache!")
        print("You received {} {}.".format(amount, expected_currency))
    else:
        exit()


