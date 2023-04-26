from apscheduler.schedulers.background import BackgroundScheduler

# Вариант №1 https://russianblogs.com/article/78281604497/

'''
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

# Включить работу по расписанию
scheduler_plan = BackgroundScheduler () ## Создание экземпляра планировщика
try:
         # Планировщик использует DjangoJobStore ()
    scheduler_plan.add_jobstore(DjangoJobStore(), "default")
         # Установить задачи по времени, метод выбора - интервал, временной интервал - 15 минут
         # Другой способ - выполнить задачу в фиксированное время с понедельника по пятницу, соответствующий код:
    # @register_job(scheduler_plan, 'cron', day_of_week='mon-fri', hour='8', minute='30', second='10',id='task_time')
    # @register_job(scheduler_plan,"interval", minutes=15)
    @register_job(scheduler_plan, 'cron', second='10',id='task_time')
    def my_job():
                 # Напишите здесь задачу, которую хотите выполнить
        print ('10 секунд прошло')
        #pass
    register_events(scheduler_plan)
    scheduler_plan.start()
except Exception as e:
    print(e)
         # Остановить таймер в случае ошибки
    scheduler_plan.shutdown()
'''

# Вариант №2 https://www.youtube.com/watch?v=Lzy4G1wZ7NQ
    
def scheduler_api():
        print ('Прошло 5 секунд')
    
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduler_api, 'interval', seconds=5)
    scheduler.start()
