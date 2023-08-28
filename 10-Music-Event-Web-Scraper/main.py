import requests
import selectorlib

URL = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


def scrape_page(url):
    """ Scrape the page source from the given URL """
    response = requests.get(url, headers=HEADERS)
    page_source = response.text
    return page_source


def extract_info(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract_page.yaml')
    extracted_content = extractor.extract(source)['tours']
    return extracted_content


if __name__ == '__main__':
    scraped_content = scrape_page(URL)
    tour_info = extract_info(scraped_content)
    print(tour_info)
