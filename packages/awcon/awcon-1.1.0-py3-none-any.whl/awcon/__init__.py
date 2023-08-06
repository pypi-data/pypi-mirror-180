__awc__ = []
__awvar__ = {}

def awfun(texts):
    def wrapper(func):
        __awc__.append([texts, func.__code__.co_name, func])

        return func
    
    return wrapper

def awvar(name, val):
    global __awvar__
    __awvar__[name] = val
