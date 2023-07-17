from datetime import datetime


def print_name():
    try:
        print(f"Rob --> {datetime.now()}")
        return {"name": "Rob",
                "time": datetime.now()}
    except Exception as err:
        return {
            "error": err
        }
