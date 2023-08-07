from fastapi import BackgroundTasks
from datetime import datetime


def print_user_date(name):
    print(f"{name} --> {datetime.now()}")


def print_name(background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(print_user_date, "rob")
        # print_user_date("Roberto")

        return {"name": "Rob", "time": datetime.now()}
    except Exception as err:
        return {"error": err}
