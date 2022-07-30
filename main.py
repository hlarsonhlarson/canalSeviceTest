from google_api_worker import google_creds_getter, get_info_spreadsheets
from dollar_exchange_rate import dollar_currency
from db_worker import insert_info_db, create_deliveries_instance
from datetime import datetime
import time

def dollar_time_converter(row, dollar_ruble):
    return (row[0], \
            datetime.strptime(row[3], '%d.%m.%Y'), \
            row[1], \
            float(row[2].replace(',', '.')), \
            float(row[2].replace(',', '.'))*dollar_ruble)


def combine_all_functions(creds, deliveries, session):
    info = get_info_spreadsheets(creds)
    while info is None:
        info = get_info_spreadsheets(creds)
    dollar_ruble = dollar_currency()
    while dollar_ruble is None:
        dollar_ruble = dollar_currency()
    info.pop(0)
    info = tuple(map(lambda x: dollar_time_converter(x, dollar_ruble), info))
    insert_info_db(info, deliveries, session)


if __name__ == '__main__':
    creds = google_creds_getter()
    x = get_info_spreadsheets(creds)
    deliveries, session = create_deliveries_instance()
    while True:
        combine_all_functions(creds, deliveries, session)
        time.sleep(5)

