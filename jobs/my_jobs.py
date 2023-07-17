from apscheduler.schedulers.background import BackgroundScheduler
from jobs.tasks import print_name

scheduler = BackgroundScheduler()

# assigning jobs to scheduler
# scheduler.add_job(print_name, 'interval', seconds=20)
scheduler.add_job(print_name, 'cron', hour=15, minute=36, second=0)
