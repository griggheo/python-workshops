# Inspired from https://realpython.com/python-web-scraping-practical-introduction/

from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import re

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_jobs(page_number):
    """
    Downloads a job board page from https://www.python.org/jobs/?page=page_number
    and returns a list of tuples containing the company info and location
    """
    url = 'https://www.python.org/jobs/?page=' + str(page_number)
    response = simple_get(url)
    jobs=[]
    #response = 1
    if response is not None:
        #raw_html = open('job-board-page-1.html').read()
        #html = BeautifulSoup(raw_html, 'html.parser')        
        html = BeautifulSoup(response, 'html.parser')
        jobs = []
        company_info = ''
        location = ''
        # example of select (used for CSS selectors)
        for li in html.select('li'):
            # example of find
            h2 = li.find('h2', class_='listing-company')
            if not h2:
                continue

            # example of find_all
            spans_company_info = li.find_all(class_='listing-company-name')
            if not len(spans_company_info):
                continue
            span_company_info = spans_company_info[0]
            # example of string replace
            company_info = span_company_info.text.strip().replace('\n', ' ').replace('\t', ' ')
            # example of regular expression substitution
            company_info = re.sub('\s\s+', ', ', company_info)

            # example of find
            span_location = li.find(class_='listing-location')
            if not span_location:
                continue
            location = span_location.text.strip()
            jobs.append((company_info, location))
        return jobs

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


if __name__ == '__main__':
    print('Getting a list of jobs from the Python job board...')
    jobs = []
    pages = 4
    for i in range(pages):
        jobs_for_page = get_jobs(i+1)
        jobs += jobs_for_page

    for i, job in enumerate(jobs):
        print(f'#{i+1}: Info: {job[0]}\t\tLocation: {job[1]}')

