import os
import datetime




def check_cpu(command):
    print(os.system(command))

def show_date():
   print(datetime.datetime.today())
# def check_date(command):
#     print(os.system(command))    

# check_cpu("time /t")
# check_cpu("df -h")

show_date()