#!/usr/bin/python3
"""  """
if __name__ == "__main__":
    import requests as req
    from sys import argv
    import json

    url = "https://jsonplaceholder.typicode.com"
    emplo_tasks = req.get(url + "/todos").json()
    emplos = req.get(url + "/users").json()

    dict_list = {}
    emplo_info = {}
    for user in emplos:
        user_id = user.get("id")
        dict_list[user_id] = []
        emplo_info[user_id] = user.get("username")

    for task in emplo_tasks:
        dict_task = {}
        dict_task["task"] = task.get("title")
        dict_task["completed"] = task.get("completed")
        dict_task["username"] = emplo_info.get(task.get("userId"))
        dict_list[task.get("userId")].append(dict_task)

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_list, file)
