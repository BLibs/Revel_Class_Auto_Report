import requests
from datetime import timedelta, datetime
from config import API_KEY, ESTABLISHMENT_MAPPING, ESTABLISHMENT_NAME
import pandas as pd


# Returns the date in mm/dd/yy format after taking an offset
def get_dates(offset):
    today_date = datetime.now().date()
    adjusted_date = today_date - timedelta(offset)
    # Changing the format to fit the query param requirements of URL
    return adjusted_date.strftime('%m/%d/%y')


# Getting the data from the API product_mix endpoint
def get_data():
    # Used to hold the data that we will return
    data_container = []

    # Starting establishment
    est = 1

    # Get the dates that we will pass to the data endpoint (1 week in example here)
    range_from = get_dates(7)
    range_to = get_dates(0)

    # For _ in range of 21 (max establishment number)
    for _ in range(21):
        # As long as it is not est 2 or est 3 (these establishments are not applicable)
        if est != 2 and est != 3:

            # Establishment name redacted
            url = f"https://{ESTABLISHMENT_NAME}.revelup.com/reports/product_mix/data/"

            # Pass the est and date range in the query string. Other required values set as well
            querystring = {"establishment": est, "range_from": range_from, "range_to": range_to,
                           "posstation": "",
                           "employee": "", "show_unpaid": "1", "show_irregular": "1", "format": "json"}

            headers = {
                "API-AUTHENTICATION": API_KEY
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            response = response.json()
            data = response.get("productmix")

            for product in data:
                name = product.get("product_name")
                total = product.get("price")
                data_container.append({'Establishment': est, 'Class': name, 'Total': total})

        est += 1

    df = pd.DataFrame(data_container)
    # Map the establishment names to the data (variable held in config.py)
    df['Establishment'] = df['Establishment'].map(ESTABLISHMENT_MAPPING).fillna(df['Establishment'])

    return df
