import requests
import selectorlib
import smtplib
import ssl
import os
import time
from dotenv import load_dotenv

load_dotenv()

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


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = os.getenv('APP10_USER_EMAIL')
    password = os.getenv('APP10_USER_PASSWORD')

    receiver = os.getenv('APP10_RECEIVER')
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email was sent!")


def store_text(extracted):
    with open('data.txt', 'a') as file:
        file.write(extracted + '\n')


def read_text(data_file):
    with open(data_file, 'r') as file:
        return file.read()


if __name__ == '__main__':
    while True:
        scraped_content = scrape_page(URL)
        tour_info = extract_info(scraped_content)
        print(tour_info)

        content = read_text('data.txt')

        if tour_info != "No upcoming tours":
            if tour_info not in content:
                store_text(tour_info)
                send_email(message="New event was found!")

        time.sleep(3600)
