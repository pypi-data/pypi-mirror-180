__awc__ = []

def awfun(texts, name=None):
    def decor(fun):
        if not name:
            name = fun.__code__.co_name
        
        __awc__.append([texts, name, fun])
        return fun
    
    return decor