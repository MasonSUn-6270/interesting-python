def times(time):
    def w(func):
        def wrapper(*args,**kwargs):
            return func(*args,**kwargs) * time

        return wrapper
    return w

@times(88)
def var():
    return 1000


print(var())
'88000'
