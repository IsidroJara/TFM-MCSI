from crontab import CronTab
 
my_cron = CronTab(user='isidro')
job = my_cron.new(command='/Users/isidro/anaconda3/bin/papermill /Users/isidro/Desktop/TFM/TFM-MCSI/Scheduler/my_notebook.ipynb /Users/isidro/Desktop/TFM/TFM-MCSI/Scheduler/output.ipynb')
job.minute.every(1)
 
my_cron.write()
