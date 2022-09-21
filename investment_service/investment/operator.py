from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from investment.views import make_data

def start():
    scheduler=BackgroundScheduler(timezone='Asia/Seoul')
    @scheduler.scheduled_job('cron', hour = '23', name = 'make_data')
    def auto_check():
        make_data()
    scheduler.start()