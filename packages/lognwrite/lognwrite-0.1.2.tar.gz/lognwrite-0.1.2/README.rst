Log N Write
===========

:Author: Muhammad Alif Putra Yasa

Log function executions and variables. Output to `stdout`.

Example
****

Use `log_function` decorator to log functions and `log_variable` to log values.

>>> from lognwrite.log_to_out import LogToOut
@LogToOut.log_function
def addition(a, b):
    LogToOut.log_variable(a, "a")
    LogToOut.log_variable(b, "b")
    return a + b
addition(3, 50)

Executing the example will output:

>>> `malifpy@malifpy:~$ python main.py`
+ addition( 3, 50 )
  a = 3
  b = 50
- addition -> 53