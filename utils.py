import threading
import zoneinfo
from datetime import datetime

def set_interval(func, seconds, app):
    def func_wrapper():
        try:
            with app.app_context():
                func()
                set_interval(func, seconds, app)
        except Exception as e:
            print(f"Func cannot run. {e}", flush=True)
        finally:
            print(f'Finish Scan at: {datetime.now(zoneinfo.ZoneInfo("America/New_York")).strftime("%-I:%M %p")}',
                  flush=True)

    t = threading.Timer(seconds, func_wrapper)

    t.start()

    return t
