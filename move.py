import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/Admin/Downloads"
to_dir = "C:/Users/Admin/Desktop/Newfolder"

class FileMovementHandler(FileSystemEventHandler):

    def on_deleted(self, event):
        print(f"Opps! Someone deleted from :"+ from_dir)
    
    def on_created(self, event):
        print(f"Someone created in :"+ from_dir)
    
    def on_modified(self, event):
        print(f"Someone modified in :"+ from_dir)

    def on_moved(self, event):
        print(f"Someone moved in :"+ from_dir)

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
        observer.stop()