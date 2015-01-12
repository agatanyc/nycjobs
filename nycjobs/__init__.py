import json

import requests

def summarize(jobs):
    """(list) -> list of pairs of job IDs and titles"""
    return [(job['job_id'], job['business_title']) for job in jobs]

def summarize_file(fname):
    """(str) -> list of pairs of job IDs and titles"""
    with open(fname) as file:
        return summarize(json.load(file))

def summarize_url(url):
    return summarize(requests.get(url).json())

def render(summary):
    for id, title in summary:
        print("{:8s}".format(id), title)

def render_url(url):
    render(summarize_url(url))

if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
       render_url('https://data.cityofnewyork.us/resource/kpav-sd4t.json')
    else:
        for arg in argv[1:]:
            render(summarize_file(arg))
