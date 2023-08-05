from jpype import *
import chardet
import threading
import subprocess
import os
import imp
from subprocess import PIPE, Popen

lock = threading.Lock()

tika_path = ""
for top, dirs, files in os.walk(imp.find_module('apachetika')[1]+'/data'):
        for nm in files:
            if nm[-4:] == ".jar":
                tika_path = os.path.join(top, nm)

class Extractor(object):
    extractor = None

    def __init__(self, **kwargs):
        try:
            lock.acquire()
            self.extractor = subprocess.Popen(["java", "-jar", tika_path, "-x"],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        finally:
            lock.release()

    def getHTML(self,data):
        return self.extractor.communicate(input=data)
