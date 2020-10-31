import datetime

datetime.datetime.now



def add(x,y):
    return x+y

    


def exec_function(anonymous_func, x, y):
    return anonymous_func(x, y)

exec_function(add, 10, 12)
