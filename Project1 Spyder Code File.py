import requests
import json
import pandas as pd

# there are a few endpoints on this site. Check docs to see what it does
# url = "https://api.opensea.io/api/v1/events?only_opensea=false&offset=0&limit=20"
# url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=40"
url = "https://api.opensea.io/api/v1/events"

response = requests.request("GET", url)
opensea_data_pull = json.loads(response.text)

# %%

# bbb = opensea_data_pull["assets"][5]["asset_contract"]["default_to_fiat"]
# price = opensea_data_pull["asset_events"][0]["payment_token"]["usd_price"]
# bid = opensea_data_pull["asset_events"][0]["bid_amount"]

# %%

data_list = opensea_data_pull["asset_events"]

listing_date_list = []
listing_price_list = []

# iterate through each item in list
for each in data_list:
    
    # grab the id
    listing_date = each["asset"]["asset_contract"]["created_date"]
    listing_date = listing_date[0:10]  # reformat dates to be cleaner

    listing_price = int(each["bid_amount"])
    listing_price = listing_price / 10000000000000

    # append id to list of ids
    listing_date_list.append(listing_date)
    listing_price_list.append(listing_price)


# %%

# cleaner method. give column headers
df = pd.DataFrame(
    {'listing_date': listing_date_list,
     'listing_price': listing_price_list
     })