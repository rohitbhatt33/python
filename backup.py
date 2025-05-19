import shutil
import datetime
import os

def backup_utils(source,dest):
    today=datetime.date.today()
    backup_file= os.path.join(dest ,f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file.replace('.tar.gz', ''),'gztar',source)

source = "C:/Users/rohit/Desktop/python"

dest="C:/Users/rohit/Desktop/python/backups"

backup_utils(source,dest)