#!/usr/bin/python3
"""This script is used to export a data as csv"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """the script runs if not imported"""
    url = 'https://jsonplaceholder.typicode.com/'
    req = requests.get(url + "users/" + argv[1]).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()
    tasks = []

    for i in todo:
        newDict = {"USER_ID": "", "USERNAME": "",
                   "TASK_COMPLETED_STATUS": "",
                   "TASK_TITLE": ""}

        newDict["USER_ID"] = i["userId"]
        newDict["USERNAME"] = req["username"]
        newDict["TASK_COMPLETED_STATUS"] = i["completed"]
        newDict["TASK_TITLE"] = i["title"]
        # Used to append each dictionaries to the list
        tasks.append(newDict)

    with open("{}.csv".format(argv[1]), "w", encoding="utf-8") as excelfile:
        fieldnames = tasks[0].keys()
        writer = csv.DictWriter(excelfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for names in tasks:
            writer.writerow(names)
