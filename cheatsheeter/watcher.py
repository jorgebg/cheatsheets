import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from cheatsheeter.__main__ import Cheatsheeter


def start(cheatsheeter: Cheatsheeter):
    #TODO Refactor
    cheatsheeter.build()
    class FileChangesWatcher:
        def __init__(self):
            self.observer = Observer()
    
        def run(self):
            event_handler = Handler()
            self.observer.schedule(event_handler, cheatsheeter.source_path, recursive = True)
            self.observer.schedule(event_handler, os.path.relpath(cheatsheeter.template_env.loader._template_root), recursive = True)
            self.observer.start()
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.observer.stop()
                print("Observer Stopped")
            self.observer.join()
    
    class Handler(FileSystemEventHandler):
        @staticmethod
        def on_any_event(event):
            if event.is_directory:
                return None
            elif event.event_type in ('created', 'modified'):
                print("{} was {}".format(event.src_path, event.event_type))
                try:
                    cheatsheeter.build()
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    print('Error:', e)
    watch = FileChangesWatcher()
    watch.run()