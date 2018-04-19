import xml.etree.ElementTree as ET
import json
import re


xml_path = "events.xml"
root = ET.parse(xml_path)

response = []

for event in list(root.getroot()):
    eventName = event.find("EventName")
    eventDescription = event.find("EventDescription")
    contactName = event.find("ContactName")
    contactPhone = event.find("ContactPhone")
    contactEmail = event.find("ContactEmail")
    categorization = event.find("Categorization")
    location = event.find("Location")
    building = event.find("Building")
    room = event.find("Room")
    startDate = event.find("StartDate")
    endDate = event.find("endDate")
    startTime = event.find("StartTime")
    endTime = event.find("endTime")

    record = {}

    if eventName is not None and eventName.text is not None:
        print("Event Name: " + eventName.text)
        record["eventName"] = eventName.text

    if eventDescription is not None and contactName.text is not None:
        print("Event Description: " + eventDescription.text)
        record["eventDescription"] = re.sub(r'<.*?>', "", eventDescription.text)

    if contactName is not None and contactName.text is not None:
        print("Contact Name: " + contactName.text)
        record["contactName"] = contactName.text

    if contactPhone is not None and contactPhone.text is not None:
        print("Contact Phone: " + contactPhone.text)
        record["contactPhone"] = contactPhone.text

    if categorization is not None and categorization.text is not None:
        print("Categorization: " + categorization.text)
        record["categorization"] = categorization.text

    if location is not None and location.text is not None:
        print("Location: " + location.text)
        record["location"] = location.text

    if building is not None and building.text is not None:
        print("Building:" + building.text)
        record["building"] = building.text

    if room is not None and room.text is not None:
        print("Room: " + room.text)
        record["room"] = room.text

    if startDate is not None and startDate.text is not None:
        print("Start Date:  " + startDate.text)
        record["startDate"] = startDate.text

    if endDate is not None and endDate.text is not None:
        print("End Date: " + endDate.text)
        record["endDate"] = endDate.text

    if endTime is not None and endTime.text:
        print("End Time: " + endTime.text)
        record["endTime"] = endTime.text

    print("\n")

    response.append(record)

    print(record)

    with open('response.json', 'w') as fp:
        json.dump(response, fp)
