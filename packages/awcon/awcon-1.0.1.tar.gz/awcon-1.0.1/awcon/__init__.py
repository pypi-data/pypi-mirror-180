__awc__ = []

def awfun(texts):
    def wrapper(func):
        __awc__.append([texts, func.__code__.co_name, func])

        return func
    
    return wrapper