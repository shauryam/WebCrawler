import bs4
import requests
import deptDetails
import json

source_url = "http://info.sjsu.edu/web-dbgen/catalog/departments/all-departments.html"
domain = "http://info.sjsu.edu"

res = requests.get(source_url)

jsonResponse = []

soup = bs4.BeautifulSoup(res.text, 'lxml')
departmentTags = soup.select(".info_wrapper table:nth-of-type(2) a")
for tag in departmentTags:

    departmentDetails = {
        "name": tag.text,
        "url" : domain + tag.get("href")
    }

    deptDetails.getDepartmentDetail(domain + tag.get("href"), departmentDetails)

    jsonResponse.append(departmentDetails)
    print(departmentDetails)

print(jsonResponse)
with open('departments.json', 'w') as fp:
    json.dump(jsonResponse, fp)