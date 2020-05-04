#!/usr/bin/python3
"""  """
if __name__ == "__main__":
    import requests as req
    from sys import argv

    emplo_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    emplo_info = req.get(url + "/{}".format(emplo_id)).json()
    emplo_tasks = req.get(url + "/{}/todos".format(emplo_id)).json()
    list_tasks = []
    for task in emplo_tasks:
        if task["completed"] is True:
            list_tasks.append(task.get("title"))

    print("Employee " + emplo_info.get("name") + " is done with tasks ({}/{}):"
          .format(len(list_tasks), len(emplo_tasks)))
    for task in list_tasks:
        print("\t {}".format(task))
