import os
from crontab import CronTab
 
dirpath = os.getcwd()

papermill_path = "/Users/isidro/anaconda3/bin/papermill"
input = dirpath + "/Untitled.ipynb"
output = dirpath + "/output.ipynb"

my_cron = CronTab(user='isidro')
job = my_cron.new(command='papermill_path input output')
job.minute.every(1)
 
my_cron.write()