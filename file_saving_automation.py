from watchdog import observers
from watchdog.events import FileSystemEventHandler
import json
import time
import os

class File_Handler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(home):
            source = home + "/" + filename
            new_folder = destination + "/" + filename
            os.renames(source,new_folder)


home = "/Users/עומר מלכה/Desktop/New folder"
destination ="/Users/עומר מלכה/Desktop/New folder2"


event_handler = File_Handler()
observer = observers.Observer()
observer.schedule(event_handler,home,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()