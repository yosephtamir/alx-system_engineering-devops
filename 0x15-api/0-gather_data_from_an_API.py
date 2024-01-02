#!/usr/bin/python3
"""This is used to request an employee task status"""
import requests
from sys import argv


if __name__ == "__main__":
    """the script runs if not imported"""
    url = 'https://jsonplaceholder.typicode.com/'
    req = requests.get(url + "users/" + argv[1]).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()
    completedTaskTitle = []
    completed = 0

    for i in todo:
        if i['completed'] is True:
            completed += 1
            completedTaskTitle.append(i['title'])
    print("Employee {} is done with tasks({}/{}):".format(
                                                          req['name'],
                                                          completed,
                                                          len(todo)))
    for title in completedTaskTitle:
        print(f"\t{title}")
