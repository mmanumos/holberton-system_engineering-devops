#!/usr/bin/python3
"""  """
if __name__ == "__main__":
    import requests as req
    from sys import argv
    import csv

    emplo_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    emplo_info = req.get(url + "/{}".format(emplo_id)).json()
    emplo_tasks = req.get(url + "/{}/todos".format(emplo_id)).json()

    with open(emplo_id + ".csv", "w", newline="") as csvfile:
        file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in emplo_tasks:
            file.writerow([emplo_id,
                           emplo_info.get("username"),
                           task.get("completed"),
                           task.get("title")])
