import threading
from functools import wraps
import keyboard as keyboard__x


def repeat_action(
    f_py=None,
    print_exception=True,
    exception_value=None,
    break_on_exceptions=False,
    interval=5,
    threadlock=None,
    kill_thread=None,
    number_of_executions=None,
    deamon=False,
):
    """
    based on:
    https://stackoverflow.com/questions/5929107/decorators-with-parameters
    https://stackoverflow.com/a/3393759/15096247

    """
    last_execution_value = None

    def kill_function():
        nonlocal killthisfunction
        killthisfunction = True

    killthisfunction = False
    if kill_thread is not None:
        keyboard__x.add_hotkey(kill_thread, kill_function)

    assert callable(f_py) or f_py is None
    maxexecutions = 0

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal maxexecutions
            if number_of_executions is not None:
                maxexecutions += 1
                if maxexecutions > number_of_executions:
                    return last_execution_value
            if break_on_exceptions is False:
                try:
                    if killthisfunction:
                        return exception_value
                    t = threading.Timer(interval, wrapper, args=args, kwargs=kwargs)
                    if deamon:
                        t.setDaemon(True)
                    t.start()
                    if threadlock is not None:
                        threadlock.acquire()
                    baxas = func(*args, **kwargs)
                    if threadlock is not None:
                        threadlock.release()
                    return baxas
                except Exception as fe:
                    if print_exception:
                        print(fe)
                    if threadlock is not None:
                        threadlock.release()

                    return exception_value
            else:
                if killthisfunction:
                    return exception_value
                t = threading.Timer(interval, wrapper, args=args, kwargs=kwargs)
                if deamon:
                    t.setDaemon(True)
                t.start()
                if threadlock is not None:
                    threadlock.acquire()
                try:
                    baxas = func(*args, **kwargs)
                finally:
                    if threadlock is not None:
                        threadlock.release()
                return baxas

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator

