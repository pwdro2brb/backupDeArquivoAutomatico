import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/User/Desktop/marketing"
destination_dir = "C:/Users/User/Desktop/backup"

def copy_folder_to_directtory(source, dest):
    today =  datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Pasta copiada para: {dest_dir}")
    except FileExistsError:
        print(f"A pasta já existe no: {dest}")

def l():
    copy_folder_to_directtory(source_dir, destination_dir)

schedule.every().day.at("08:05").do(l)

while True:
    schedule.run_pending()
    time.sleep(60)