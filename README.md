# APSchedular -w- Fast API

## Docs
[Github](https://github.com/agronholm/apscheduler)  
[Docs](https://apscheduler.readthedocs.io/en/3.x/userguide.html)

## Tutorials
https://www.youtube.com/watch?v=m5H54NcvBRU
https://youtu.be/sRnsR-T0Lxc

## Notes
`hour=` is UTC time

## Example schedules and cron
```python
from datetime import datetime 
scheduler.add_job(func_one, 'interval', seconds="30")  # note plural
scheduler.add_job(func_one, 'date', run_date = datetime(2023, 2, 20, 12, 0 , 0))
scheduler.add_job(func_one, 'date', run_date = "2023-4-30 08:00:00")
scheduler.add_job(func_one, 'cron', hour="13", minute="15", second="30")
scheduler.add_job(func_one, 'cron', hour="13", minute="*")  # every minute during 1pm UTC  
scheduler.add_job(func_one, 'cron', minute="*/5")  # every 5 minutes  
scheduler.add_job(func_one, 'cron', month="1-3,6-8", minute="*/5")  # every 5 minutes during months 1-3 and 6-8 only  
scheduler.add_job(func_two, 'cron', hour="13", minute="15", second="30", args=["Job 2"])
```