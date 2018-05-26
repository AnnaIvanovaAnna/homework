def log(function):
    def new_function(*args,**kwargs):
        name=function.__name__
        arguments=args
        print('Имя функции:{}\nАргументы функции:{}'.format(name,arguments))
        result=function(*args,**kwargs)
        return result
    return new_function