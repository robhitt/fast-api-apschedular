from fastapi import FastAPI
import os
from jobs.my_jobs import scheduler

# from jobs.tasks import print_name


app = FastAPI(
    title="Fast API -w- apscheduler", description="Setting up and testing apscheduler"
)

# start scheduler
scheduler.start()


@app.get("/")
async def root():
    return {
        "name": "Portal API",
        "version": "1.0.0",
        "environment": os.environ.get("FASTAPI_CONFIG"),
    }
