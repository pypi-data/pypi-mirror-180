import traceback
import sys

def py_classic_error():
    """
    py_classic_error is a classic way to show errors

    how to use it

    from py_classic_error import py_classic_error

    example:
    numbers = [1,2,3,4]

    try:
        print(numbers[8])
    except:
        py_classic_error()
    """
    exc_type, exc_value, exc_traceback = sys.exc_info()
    errorsall = traceback.format_tb(exc_traceback)[0].split(",")
    errs = [refact.split(" ") for refact in errorsall for k in ['line','File'] if k in refact]
    dis = [errs[x][y] for x in range(0, len(errs)) for y in range(0, len(errs[x])) if len(errs[x][y]) != 0 and errs[x][y] != 'File' and errs[x][y] != 'line']
    files, linesno, type, showst, codescause = dis[0], dis[1], exc_type, exc_value, errorsall[2].split(" ")[-1].strip("\n")
    print("py_classic_error".center(30,"-"),"\nerrtype: {}\nerr: {}\nPath: {}\n=> {} {}".format(type, showst, files, linesno,codescause))

