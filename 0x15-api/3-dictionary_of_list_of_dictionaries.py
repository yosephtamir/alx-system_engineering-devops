#!/usr/bin/python3
"""This is used to export a json file of a user"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """the script runs if not imported"""
    url = 'https://jsonplaceholder.typicode.com/'
    tasks = []
    dictfile = {}
    allDict = {}
    urlLength = 'https://jsonplaceholder.typicode.com/users'
    reqLength = requests.get(urlLength).json()

    for count in range(len(reqLength)):
        req = requests.get(url + "users/" + str(count + 1)).json()
        todo = requests.get(url + "todos",
                            params={"userId": str(count + 1)}).json()
        tasks = []
        for i in todo:
            newDict = {"username": "", "task": "", "completed": ""}
            newDict["username"] = req["username"]
            newDict["task"] = i["title"]
            newDict["completed"] = i["completed"]
            # Used to add each dictionaries to list
            tasks.append(newDict)
        dictfile["{}".format(count + 1)] = tasks

    with open("todo_all_employees.json", "w", encoding="utf-8") as jfile:
        json.dump(dictfile, jfile)
