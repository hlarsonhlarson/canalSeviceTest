from google_api_worker import google_creds_getter, get_info_spreadsheets

if __name__ == '__main__':
    creds = google_creds_getter()
    x = get_info_spreadsheets(creds)
    print(x)
