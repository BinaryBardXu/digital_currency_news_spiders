import schedule
from datetime import datetime
from . import spiders_runner
import time


def job():
    print('\n' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    spiders_runner.run()


def run():
    schedule.every(1).minutes.do(job)
    schedule.run_pending()
    while True:
        schedule.run_pending()
        time.sleep(1)
