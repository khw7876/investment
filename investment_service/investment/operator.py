from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import make_data


def start():
    scheduler=BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    # scheduler.add_job(start, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
    register_events(scheduler)
    @scheduler.scheduled_job('cron', minute = '*/5', name = 'make_data')
    def auto_check():
        make_data()
    scheduler.start()