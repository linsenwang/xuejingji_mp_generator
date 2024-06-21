import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_delay, stop_after_attempt
import add_current

@retry(stop=(stop_after_delay(15) | stop_after_attempt(5)))
def get_requests_data(url):
    requests_data = requests.get(url)
    soup_data = BeautifulSoup(requests_data.text, 'html.parser')
    return soup_data

def get(url):
    try:
        data = get_requests_data(url)
        return data
    except:
        add_current.add_error(url)