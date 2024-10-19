from bs4 import BeautifulSoup
import requests
import time

print('Put some skills that you are not familiar with')
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}')

job_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=react&txtLocation="

def find_jobs(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text.strip()
        # filter jobs with 'few days ago' job post
        if('few' in published_date):
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skillsData = job.find('span', class_='srp-skills').text.strip().split()
            skills = ', '.join(skillsData)
            # get href attribute
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name} \n")
                    f.write(f"Required Skills: {skills} \n")
                    f.write(f"More Info: {more_info}")
                    print(f'File saved {index}.txt ')

# this function will run only this file as main file otherwise this function will not run as imported file
if __name__ == '__main__':
    while True:
        # this function will run after every 5 minutes
        find_jobs(job_url)
        time_wait = 5
        time.sleep(time_wait * 60)