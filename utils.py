import threading


def set_interval(func, seconds, app):
    def func_wrapper():
        try:
            with app.app_context():
                func()
                set_interval(func, seconds, app)
        except:
            print("Func cannot run.")
            set_interval(func, seconds, app)

    t = threading.Timer(seconds, func_wrapper)

    t.start()

    return t
