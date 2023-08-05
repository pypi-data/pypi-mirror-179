### Run code asynchronously to the main code execution

```python
pip install interval-repeat-decorator

from interval_repeat_decorator import repeat_action
from threading import Lock
lock = Lock()
@repeat_action(
    print_exception=True,
    exception_value="FTW",
    break_on_exceptions=False,
    interval=.1,
    threadlock=lock,
    kill_thread="ctrl+x",
    number_of_executions=10,
)
def testest(number):
    if number == 0:
        print(number)
        return True
    elif number == 1:
        print(number / 0)
    return True
@repeat_action(
    print_exception=True,
    exception_value="FTW",
    break_on_exceptions=False,
    interval=.2,
    threadlock=lock,
    kill_thread="ctrl+y",
    number_of_executions=5,
)
def testest2(number):
    if number == 0:
        print(number)
        return True
    elif number == 1:
        print(number / 0)
    return True
testex = testest(number=0)
testex2 = testest2(number=1)
print(f"{testex=}\n{testex2=}") #returns the first result only, but will keep on executing!  
0
division by zero
testex=True
testex2='FTW'
0
division by zero
0
0
division by zero
0
0
division by zero
0
0
division by zero
0
0
testex
Out[3]: True
testex2
Out[4]: 'FTW'


```

