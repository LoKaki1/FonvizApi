import threading


class SetInterval:
    def __init__(self, func, sec, *args, **kwargs):
        def func_wrapper():
            self.timer = threading.Timer(sec, func_wrapper)
            self.timer.start()
            func(*args, **kwargs)

        self.timer = threading.Timer(sec, func_wrapper)
        self.timer.start()

    def cancel(self):
        self.timer.cancel()
