import requests
import bs4

response = []

def getDetail(tag, key):
    values = tag.text.strip().replace(key + "\n", "")
    result = values.split("\n")
    #print(result)
    return result


def getDepartmentDetail(source_url, deptData):

    domain = "http://info.sjsu.edu"

    res = requests.get(source_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    tags = soup.select(".info_wrapper p")


    for tag in tags:

        if tag.text.strip().find("Office") > -1:
            deptData["office"] = getDetail(tag, "Office")

        elif tag.text.strip().find("Telephone") > -1:
            deptData["telephone"] = getDetail(tag, "Telephone")

        elif tag.text.strip().find("Email") > -1:
            deptData["email"] = getDetail(tag, "Email")

        elif tag.text.strip().find("WWW") > -1:
            deptData["website"] = getDetail(tag, "WWW")

        elif tag.text.strip().find("Associate Professors") > -1:
            deptData["associateProfessors"] = getDetail(tag, "Associate Professors")

        elif tag.text.strip().find("Assistant Professors") > -1:
            deptData["assistantProfessors"] = getDetail(tag, "Assistant Professors")

        elif tag.text.strip().find("Professors") > -1:
            deptData["professors"] = getDetail(tag, "Professors")

        elif tag.text.strip().find("Curricula") > -1:
            deptData["curricula"] = getDetail(tag, "Curricula")


    #print(deptData)



