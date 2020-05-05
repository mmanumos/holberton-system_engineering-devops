#!/usr/bin/python3
""" Exporting data of an API to a Json file """
if __name__ == "__main__":
    import requests as req
    from sys import argv
    import json

    emplo_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    emplo_info = req.get(url + "/{}".format(emplo_id)).json()
    emplo_tasks = req.get(url + "/{}/todos".format(emplo_id)).json()

    list_task = []
    for task in emplo_tasks:
        dict_task = {}
        dict_task["task"] = task.get("title")
        dict_task["completed"] = task.get("completed")
        dict_task["username"] = emplo_info.get("username")
        list_task.append(dict_task)

    dict_task_emplo = {emplo_id: list_task}

    with open(emplo_id + ".json", "w") as file:
        json.dump(dict_task_emplo, file)
