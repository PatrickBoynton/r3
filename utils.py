import threading

def set_interval(func, seconds, app):
    def func_wrapper():
        try:
            with app.app_context():
                set_interval(func, seconds, app)
                func()
        except:
            print("Func cannot run.")
    
    t = threading.Timer(seconds, func_wrapper)
    
    t.start()
    
    return t