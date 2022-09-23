from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from investment.views import make_data

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.add_job(make_data , 'cron', hour = '09')
    scheduler.start()