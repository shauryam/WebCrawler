import requests
import json
import bs4


domain = "http://info.sjsu.edu"

departments = json.load(open('departments.json'))

print(departments)

coursesData = {}

def getCourseDescription(url, courseData, courseCode):

    courseDescriptionHTML = requests.get(url)

    soup = bs4.BeautifulSoup(courseDescriptionHTML.text, 'lxml')

    tags = soup.select(".info_wrapper p")

    for tag in tags:
        if tag.text.strip().find("Description") > -1:
            courseData[courseCode]["description"] = tag.text.strip().replace("Description" + "\n", "")

        if tag.text.strip().find("Grading") > -1:
            courseData[courseCode]["grading"] = tag.text.strip().replace("Grading" + "\n", "")

        if tag.text.strip().find("Units") > -1:
            courseData[courseCode]["units"] = tag.text.strip().replace("Units" + "\n", "")

def getCourses(dept_url):

    source_url = dept_url.replace(".html", "-courses.html")

    res = requests.get(source_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    coursesTags = soup.select(".info_wrapper table:nth-of-type(2) tr")

    department = ""

    for tag in coursesTags:

        if(tag.select("h3")):
            department = (tag.select("h3"))[0].text
            continue

        courseCode = tag.text.split(":")[0]

        try:
            courseName = (tag.text.split(":"))[1].strip()

        except:
            continue


        linkTag = tag.select("a")
        url = linkTag[0].get("href")



        coursesData[courseCode] = {
            "courseName": courseName,
            "courseCode": courseCode,
            "department": department,
            "url": domain + url
        }

        getCourseDescription(domain + url, coursesData, courseCode)

        print(coursesData[courseCode])


for department in departments:
    print(department["url"])
    getCourses(department["url"])

#getCourses("http://info.sjsu.edu/web-dbgen/catalog/departments/CMPE.html")
print(coursesData)

with open('courses.json', 'w') as fp:
    json.dump(coursesData, fp)




