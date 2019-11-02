from crontab import CronTab
 
my_cron = CronTab(user='isidro')
job = my_cron.new(command='jupyter nbconvert --to notebook --execute Untitled.ipynb')
job.minute.every(1)
 
my_cron.write()
