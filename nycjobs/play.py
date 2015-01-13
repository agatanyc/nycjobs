import json
import requests

def salary_level(jobs):
    """(list) -> list of tuples of `minimum qual requirerments`,
    `salary range from`, `salary range to`"""
    return[(job['minimum_qual_requirements'],
            job['salary_range_from'],
            job['salary_range_to'])
            for job in jobs if 'minimum_qual_requirements' in job]

def salary_level_url(url):
    """(url) -> list of tuples"""
    return salary_level(requests.get(url).json())

def render(salaries):
    """(list of tuples) -> None"""
    for qual, range_from, range_to in salaries:
        print(qual, range_from, range_to)
        print()

def render_url(url):
    """(url) -> None"""
    render(salary_level_url(url))

if __name__== '__main__':
    url='https://data.cityofnewyork.us/resource/kpav-sd4t.json'
    data = requests.get(url).json()
    render_url(url)

