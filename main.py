from fastapi import FastAPI
from jobs.my_jobs import scheduler
from jobs.tasks import print_name


app = FastAPI(
    title="Fast API -w- apscheduler",
    description="Setting up and testing apscheduler"
)

# start scheduler
scheduler.start()


@app.get("/")
def name_task():
    try:
        return print_name()
    except Exception as err:
        return {
            "error": err
        }
