import os

import yaml
from yaml.loader import SafeLoader
import schedule
import time
import glob
import shutil
from zipfile import ZipFile


def read_yaml(path):
    with open(path,'r') as f:
        data = yaml.load(f,Loader = SafeLoader)
        return data


def Timer(job,interval):
    schedule.every(interval).seconds.do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)

def zipping():
    main_dir = "D:\\maza karbhar\\Schedular_Project\\data\\"
    files = os.listdir(main_dir)

    if files:
        os.makedirs(main_dir + "Load\\Load")
        destination = main_dir + ("Load\\Load\\")

        for file in files:
            if os.path.isfile(main_dir+file):
                shutil.move(main_dir+file,destination+file)

        zip_file = "D:\\maza karbhar\\Schedular_Project\\data\\Load\\Load"
        root_file = "D:\\maza karbhar\\Schedular_Project\\data\\Load\\Load"
        shutil.make_archive(zip_file,'zip',root_dir=root_file)
        print("\nzipping done")
        return True
    else:
        return False


def flush():
    path = "D:\\maza karbhar\\Schedular_Project\\data\\Load"
    try:
        shutil.rmtree(path)
        print("\nflush done")
    except:
        pass






if __name__ == "__main__":
    pass
