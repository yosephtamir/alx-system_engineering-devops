#!/usr/bin/python3
"""This is used to export a json file of a user"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """the script runs if not imported"""
    url = 'https://jsonplaceholder.typicode.com/'
    req = requests.get(url + "users/" + argv[1]).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()
    tasks = []
    dictfile = {}

    for i in todo:
        newDict = {"task": "", "completed": "", "username": ""}

        newDict["task"] = i["title"]
        newDict["completed"] = i["completed"]
        newDict["username"] = req["username"]
        # Used to add each dictionaries to list
        tasks.append(newDict)
    dictfile["{}".format(argv[1])] = tasks

    with open("{}.json".format(argv[1]), "w", encoding="utf-8") as jfile:
        json.dump(dictfile, jfile)
