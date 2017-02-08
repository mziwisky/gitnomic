from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor


def resolve_round ():
    print "round resolved"


def init_scheduler (mongoclient):
    jobstore = {'default' : MongoDBJobStore(collection='scheduler', client=mongoclient)}
    executor = {'default' : ThreadPoolExecutor(max_workers = 1)}
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(jobstores=jobstore, executors=executor, job_defaults=job_defaults)
    
    scheduler.add_job(resolve_round, id='resolve round', trigger='cron', second='*', replace_existing=True)
    
    scheduler.start()
    return scheduler
