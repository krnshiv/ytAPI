from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from fetch import fetchAPI

def start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(fetchAPI.fetch,'interval',seconds=10)
    print('start')
    scheduler.start()
