class MyStrError(ValueError):
    pass


class StrTooShort(MyStrError):
    pass

class A:
    def __init__(self,text):
        '''
        hi
        :param text:
        '''
        if len(text) <=2 :

            raise StrTooShort(text)
        else:
            self.describe = text
            print(self.__init__.__doc__)

a=A('sdd')
a=A('sd')