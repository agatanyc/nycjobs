from itertools import groupby
import json
import pprint
import requests
import sys

class Job:

    def __init__(self, min_salary, max_salary, business_title, job_id):
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.business_title = business_title
        self.job_id = job_id

    def __repr__(self):
        return "Job({}, {}, {}, {})".format(
            repr(self.min_salary),
            repr(self.max_salary),
            repr(self.business_title),
            repr(self.job_id))

    def __str__(self):
        return self.business_title

def make_jobs(jobs):
    """(list of dicts) -> list of Jobs"""
    return [Job(job['salary_range_from'],
                job['salary_range_to'],
                job['business_title'],
                job['job_id']) for job in jobs]

def render(jobs):
    """(list of job instances) -> NoneType"""
    print('\n\n'.join((job) for job in jobs))

if __name__== '__main__':

    if "--fetch" in sys.argv:
        url = 'https://data.cityofnewyork.us/resource/kpav-sd4t.json'
        data = requests.get(url)
        with open("jobs.js", "w") as f:
            f.write(data.text)

    with open("jobs.js") as f:
        data = f.read()

    jobs = make_jobs(json.loads(data))

    print(len(jobs), "jobs found")

    # Remove duplicates.
    uniq = [next(xs) for _, xs in groupby(jobs, lambda x: x.job_id)]
    print(len(uniq), "after deduping")
