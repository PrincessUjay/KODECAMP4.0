import os
import sys
import subprocess



command = ["vagrant", "ubuntu/focal64"]
command2 = ["vagrant", "up"]

dirPath = "\Users\onyek\Documents\KODECAMP4.0\python4devops"

sp = subprocess.Popen(command,shell=False,stdout=subprocess,PIPE,stderr=subprocess,PIPE,universal_newlines=True)
sp2 = subprocess.Popen(command,shell=False,stdout=subprocess,PIPE,stderr=subprocess,PIPE,universal_newlines=True)


def get_version():
    print("\nExecuting get_version() Function....\n")

    version = sys.version

    versionID = version[0:6]
    return versionID


    def create_folder():

        print("\nExecuting create_folder() Function....\n")


        vid = get_version()


        if "3" in vid:
            